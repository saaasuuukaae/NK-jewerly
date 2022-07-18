from django.views.generic import ListView

from main.models import GalleryImage


class IndexView(ListView):
	template_name = 'main/index.html'
	model = GalleryImage

	context_object_name = 'pics'

	def get_queryset(self):
		return self.model.objects.filter(show=True).order_by('created_at')