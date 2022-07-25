from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

PHOTO_URL = "photos"


class Design(models.Model):
	title = models.CharField(
		max_length=185,
		blank=True,
		verbose_name=_("Title for <<main>> screen.")
	)

	subtitle = models.TextField(
		blank=True,
		verbose_name=_("Subtitle for <<main>> screen.")
	)

	background = models.ImageField(
		upload_to=f"{PHOTO_URL}/BACKGROUND/%y/%m/%d",
		verbose_name=_("Background for <<main>> screen.")
	)

	about_picture = models.ImageField(
		upload_to=f"{PHOTO_URL}/ABOUT-PICS/%y/%m/%d",
		verbose_name=_("About picture for <<about>> screen.")
	)

	about_title = models.CharField(
		max_length=50,
		blank=False,
		verbose_name=_("Title for <<about>> screen.")
	)

	about_subtitle = models.CharField(
		max_length=50,
		blank=False,
		verbose_name=_("Subtitle for <<about>> screen.")
	)

	about_text = models.TextField(
		blank=True,
		verbose_name=_("A huge text for <<about>> screen.")
	)

	footer_text = models.TextField(
		blank=True,
		verbose_name=_("Small text for <<footer>>.")

	)

	display = models.BooleanField(
		db_index=True,
		verbose_name=_("Display this design?"),
	)

	class Meta:
		verbose_name = _("Site design")
		verbose_name_plural = _("Site designs")
		ordering = ('display',)

	@property
	def about_sub(self):
		s = str(self.about_subtitle)
		s1 = s[:len(s) // 2]
		s2 = s[len(s) // 2:]

		print(s)
		print(s1)
		print(s2)
		print([s1, s2])
		return [s1, s2]


class GalleryImage(models.Model):
	Image = models.ImageField(
		upload_to=f"{PHOTO_URL}/GALLERY/%y/%m/%d",
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
		return f"{self.pk:,}"

	def __repr__(self):
		return f'{self.pk:,} - %(visible)s - {self.show}' % {'visible': _("Visible")}
