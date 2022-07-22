from typing import Dict

from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from main.models import GalleryImage, Design
from main.utils import DataMixin



class IndexView(DataMixin, ListView):
	template_name = 'main/index.html'
	model = GalleryImage

	context_object_name = 'pics'

	@property
	def default_design(self) -> Dict:
		title = _("Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly ")
		subtitle = _(
			"Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly ")
		background = {'url': "/static/img/bg/04.jpg"}
		about_picture = {'url': "/static/img/about/01.jfif"}
		about_title = _("About me")
		about_subtitle = [_('jewe'), _('lry')]  # NOQA
		about_text = _("")
		footer_text = _("Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly " 
		                "Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly Jewerly "
		                "Jewerly Jewerly ")

		return {
			"title": title,
			'subtitle': subtitle,
			'background': background,
			"about_picture": about_picture,
			'about_title': about_title,
			"about_sub": about_subtitle,
			'about_text': about_text,
			'footer_text': footer_text,
		}

	def get_design(self) -> Dict:
		_list = list(Design.objects.filter(display=True))
		if len(_list) < 1:
			return self.default_design

		return _list[0]

	def get_context_data(self, *, object_list=None, **kwargs):
		raw_context = super().get_context_data(**kwargs)
		additional_context = self.get_user_context(
			page_title=_("Nataliya Karetniy"),
			design=self.get_design()
		)

		context = dict(list(raw_context.items()) + list(additional_context.items()))
		return context

	def get_queryset(self):
		return self.model.objects.filter(show=True).order_by('pk')

