from typing import Dict


class DataMixin:

	def get_user_context(self, **kwargs) -> Dict:
		context = kwargs

		return context