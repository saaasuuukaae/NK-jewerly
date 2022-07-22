from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(Design)
class NewsTranslationOptions(TranslationOptions):
	fields = ('title', 'subtitle', 'about_title', 'about_subtitle', 'about_text', "footer_text",)


@register(GalleryImage)
class NewsTranslationOptions(TranslationOptions):
	fields = ('description',)

