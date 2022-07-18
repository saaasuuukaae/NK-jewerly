
from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
	path('', IndexView.as_view()),
	path('index', IndexView.as_view()),
	path('main', IndexView.as_view()),
	path('home', IndexView.as_view()),
	path('base', IndexView.as_view()),

]