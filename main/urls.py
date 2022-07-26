from django.conf import settings
from django.urls import path
from .views import *


urlpatterns = [
	path('', IndexView.as_view(), name="home"),
	path('index', IndexView.as_view()),
	path('main', IndexView.as_view()),
	path('home', IndexView.as_view()),
	path('base', IndexView.as_view()),


]

# if debug add debug urls
if settings.DEBUG:
	# add text-exc patterns
	urlpatterns += [
		path('test_exception', test_exception, name="test_exception"),
	]