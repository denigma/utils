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


class LoadDocs(TemplateView):
    """Loads a README and documentation and passes it to the template.

    To use it overwrite and file_name attribute that specifies the
    location of the file to load.
    """
    template_name = None
    file_name = None
    path_name = None

    def dispatch(self, request, *args, **kwargs):
        if 'name' in kwargs:
            self.file_name = kwargs['name']
        print self.file_name
        return super(LoadDocs, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoadDocs, self).get_context_data(**kwargs)
        files = os.listdir(self.path_name)
        context['files'] = dict([(file.split('.')[0].replace('_', ' ').title(), file) for file in files])
        try:
            context['file'] = urlize(open(os.path.join(settings.BASE_DIR, self.file_name)).read()).replace('\n', '<br>')
        except:
            print(self.file_name)
            context['file'] = urlize(open(os.path.join(settings.BASE_DIR, self.path_name,  context['files'][self.file_name])).read()).replace('\n', '<br>')
        return context


class DocsView(LoadDocs):
    template_name='about.html'
    file_name = 'README.rst'
    path_name = 'docs'