import sys
from typing import Dict

from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.debug import technical_500_response, technical_404_response
from django.views.generic import ListView

from main.models import GalleryImage, Design
from main.utils import DataMixin


# view to test excpetions
def test_exception(request):
	context = {
		"page_title": _("Bad request"),
		"message": _("Bad request"),
		"exception": None,
		"instruction": _("Go and do something...")
	}
	return render(request, "main/error.html", context)


# Exception view for 400 error
def bad_request(request, exception):
	if request.user.is_superuser:
		return technical_500_response(request, *sys.exc_info())

	context = {
		"message": _("Bad request"),
		"exception": str(exception),
		"instruction": _("try another link")
	}
	return render(request, "main/error.html", context)


# exception view for 403 error


def permission_denied(request, exception):
	if request.user.is_superuser:
		return technical_500_response(request, *sys.exc_info())
	context = {
		"message": _("Permission denied"),
		"exception": str(exception),
		"instruction": _("you are not allowed to access this page")
	}
	return render(request, "main/error.html", context)


# exception view for 404 error
def page_not_found(request, exception):
	if request.user.is_superuser:
		return technical_404_response(request, exception)
	context = {
		"message": _("Page not found"),
		"exception": str(exception),
		"instruction": _("try another link")
	}
	return render(request, "main/error.html", context)


# exception view for 500 error
def server_error(request, exception=None):
	if request.user.is_superuser:
		return technical_500_response(request, *sys.exc_info())
	context = {
		"message": _("Server error occurred"),
		"exception": str(exception),
		"instruction": _("Please contact administrator")
	}
	return render(request, "main/error.html", context)


class IndexView(DataMixin, ListView):
	template_name = 'main/index.html'
	model = GalleryImage

	context_object_name = 'pics'

	@property
	def default_design(self) -> Dict:
		title = _("__text__")
		subtitle = _(
			"__text__")
		background = {'url': "/static/img/bg/04.jpg"}
		about_picture = {'url': "/static/img/about/01.jpg"}
		about_title = _("About me")
		about_subtitle = [_('jewe'), _('lry')]  # NOQA
		about_text = _("__text__")
		footer_text = _(
			"__text__")

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
			page_title=_("Natalia Karetniy"),
			design=self.get_design()
		)

		context = dict(
			list(raw_context.items()) + list(additional_context.items()))
		return context

	def get_queryset(self):
		return self.model.objects.filter(show=True).order_by('pk')
