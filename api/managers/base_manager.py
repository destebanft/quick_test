from django.db.models import Manager


class BaseManager(Manager):
	def get_or_null(self, *args, **kwargs):
		try:
			return self.get(*args, **kwargs)
		except self.model.DoesNotExist:
			return None