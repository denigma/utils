import os

from django.views.generic import TemplateView
from django.utils.html import urlize
from django.conf import settings


class LoadView(TemplateView):
    """Loads a file and passes it to the template.

    To use it overwrite and file_name attribute that specifies the
    location of the file to load.
    """
    template_name = None
    file_name = None

    def get_context_data(self, **kwargs):
        context = super(LoadView, self).get_context_data(**kwargs)
        context['file'] = urlize(open(os.path.join(settings.BASE_DIR, self.file_name)).read()).replace('\n', '<br>')
        return context

