from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

PHOTO_URL = "GALLERY/"


class GalleryImage(models.Model):
	Image = models.ImageField(
		upload_to=f"{PHOTO_URL}%y/%m/%d",
		verbose_name=_("Image in gallery"),
	)

	description = models.TextField(
		verbose_name=_("Short image description"),
		blank=True,
		validators=[
			MaxLengthValidator(
				350,
				message=_("The text is too long, it should be a maximum of 350 characters.")
			)
		]
	)

	show = models.BooleanField(
		verbose_name=_("Show this picture in the gallery images list?"),
		default=True,
		db_index=True,
		null=False
	)

	wide = models.BooleanField(
		verbose_name=_("Should this picture be given more width in the gallery?"),
		help_text="Any image with this value will automatically get more width in the gallery.",
		default=False,
		null=False,
	)

	high = models.BooleanField(
		verbose_name=_("Should this picture be given more height in the gallery?"),
		help_text="Any image with this value will automatically get more height in the gallery.",
		default=False,
		null=False,
	)

	created_at = models.DateTimeField(
		verbose_name=_("Created at"),
		auto_now=True,

	)

	class Meta:
		verbose_name = _("Gallery image")
		verbose_name_plural = _("Gallery images")
		order_with_respect_to = 'show'

	def __str__(self):
		return str(self.pk)

	def __repr__(self):
		return f'{self.pk:,} - %(visible)s - {self.show}' % {'visible': _("Visible")}
