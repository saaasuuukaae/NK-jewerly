from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import *


# Register your models here.
@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
	list_display = ('pk', 'description')
	readonly_fields = ("get_image_readonly",)

	def get_image_readonly(self, object):
		return mark_safe(f"<img src={object.image.url} style='max-width: 600px; max-height: 650px;'>")

	get_image_readonly.description = _("Image")
