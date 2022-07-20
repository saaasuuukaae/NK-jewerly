from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import *


# Register your models here.
@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'wide', 'high', 'show')
	list_editable = ('wide', 'high', 'show')
	readonly_fields = ("get_date", "get_image_readonly")

	def get_image_readonly(self, object: GalleryImage):
		return mark_safe(f"<img src={object.Image.url} style='max-width: 600px; max-height: 650px;'>")

	def get_date(self, object):
		return mark_safe(f"<p style='color: #fff; font-size: 20px; font-family: Montserrat, sans-serif;'>{object.created_at}</p>")

	get_image_readonly.description = _("Image")
