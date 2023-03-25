from django.contrib import messages


class DataMixin(object):
    def get_user_context(self, **kwargs):
        context = kwargs
        return context
