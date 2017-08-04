import os
from io import BytesIO
from PIL import Image
from resizeimage import resizeimage

from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Banner(models.Model):
    title = models.CharField(_("Titulo"), max_length=255)
    description = models.TextField(blank=True, null=True)
    width = models.PositiveIntegerField(_("Largura"))
    height = models.PositiveIntegerField(_("Altura"))

    def __str__(self):
        return str(self.title)


def handle_image_file(instance, filename):
    return "banner_{0}/{1}".format(instance.banner.id, filename)


class BannerImage(models.Model):
    banner = models.ForeignKey(Banner, verbose_name=_("Imagem do Banner"), related_name="images")
    file = models.ImageField(_("Imagem"), upload_to=handle_image_file)

    class Meta:
        verbose_name = _("Imagem")
        verbose_name_plural = _("Imagens")

    def resize_image(self):
        name, extension = os.path.splitext(self.file.name)
        extension = extension.lower()
        pil_image_obj = Image.open(self.file)

        new_image = resizeimage.resize_width(pil_image_obj, self.banner.width)
        new_image = resizeimage.resize_crop(new_image, [self.banner.width, self.banner.height])

        if extension in ['.jpeg', '.jpg']:
            format_type = 'JPEG'
        elif extension == '.png':
            format_type = 'PNG'

        new_image_io = BytesIO()
        new_image.save(new_image_io, format=format_type)
        temp_name = self.file.name
        
        self.file.delete(save=False)

        self.file.save(temp_name, content=ContentFile(new_image_io.getvalue()), save=False)

    def save(self, *args, **kwargs):
        if self.file:
            self.resize_image()
        super(BannerImage, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.id)

    def admin_thumb(self):
        return u'<img width="150" height="100" src="%s" />' % self.file.url
    admin_thumb.short_description = "Imagem"
    admin_thumb.allow_tags = True