from django.conf import settings
from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
	path('', cache_page(60)(IndexView.as_view()), name="home"),
	path('index', cache_page(60)(IndexView.as_view())),
	path('main', cache_page(60)(IndexView.as_view())),
	path('home', cache_page(60)(IndexView.as_view())),
	path('base', cache_page(60)(IndexView.as_view())),


]

# if debug add debug urls
if settings.DEBUG:
	# add text-exc patterns
	urlpatterns += [
		path('test_exception', test_exception, name="test_exception"),
	]