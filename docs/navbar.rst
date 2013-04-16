Active Navbar
-------------
The are various ways to implement highlighting of the current view as the active one:

* https://groups.google.com/forum/?fromgroups=#!topic/django-users/BteSRv4m7tk
* Added block tags for each page http://ilostmynotes.blogspot.de/2010/03/django-current-active-page-highlighting.html
* https://bitbucket.org/schinckel/django-menus
* https://github.com/hellysmile/django-activeurl
* https://code.djangoproject.com/ticket/18584
* http://stackoverflow.com/questions/340888/navigation-in-django
* http://ilostmynotes.blogspot.de/2010/03/django-current-active-page-highlighting.html
* http://www.martin-geber.com/thought/2007/10/25/breadcrumbs-django-templates/
* http://gnuvince.wordpress.com/2007/09/14/a-django-template-tag-for-the-current-active-page/
* http://gnuvince.wordpress.com/2008/03/19/the-new-and-improved-active-tag/
* http://djangosnippets.org/snippets/1726/
* http://stackoverflow.com/questions/7665514/django-highlight-navigation-based-on-current-page
* http://www.turnkeylinux.org/blog/django-navbar

.. code-block:: python

    #context_pocessor.py
    from django.core.urlresolvers import resolve


    def resolve_urlname(request):
        print("""Allows to se what matched urlname for this request is within the template.""")
        try:
            res = resolve(request.path)
            if res:
                return {'urlname': res.url_name}
        except:
            return {}

    #settings.py
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'apps.render.context_processor.resolve_urlname',
    )

.. code-block:: js

    <script>
        $(document).ready(function(){
            var path = location.pathname;
            $('ul.navbar a.nav[href$]"' + path + '"]').addClass("active");
        });
    </script>

.. code-block:: python

    @register.simple_tag
    def active(request, pattern):
        if re.search(pattern, request.path):
            return 'active'
        return ''

    @register.simple_tag
    def active(parser, token):
        args = token.split_contents()
        template_tag = args[0]
        if len(args) < 2:
            raise template.TemplateSyntaxError, \
                "%r tag requires at least one argument"  % template_tag
        return NavSelectNode(args[1:])


    class NavSelectNode(template.Node):
        def __init__(self, name):
            self.name = name

        def render(self, context):
            if context['request'].path == reverse(self.name[1]):
                return 'active'