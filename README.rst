Utils
=====
This app shall feature reusable utility components.

It provides a template tag ''tags'' that enables navigation bar items to mark
the current list object as active.

To install it simple include utils in the settings:

.. code-blocks:: python

    # settings.py
    ...
    INSTALLED_APPS = (
        ...
        'utils',
        ...
    )

To use it in a Bootstrap base template load the template tags and pass
the ``request`` as well as the name of url to the URL to the active
function. This function will evaluate whether the URL is the current
one and mark it as activate.

.. code-block:: django

    # base.html
    ...
    {% load tags %}
    ...
    <ul class="nav">
        <li class="{% active request 'home' %}"><a href="/">Home</a></li>
        <li class="{% active request 'about' %}"><a href="{% url "about"  %}">About</a></li>
        <li class="{% active request 'contact' %}"><a href="{% url "contact" %}">Contact</a></li>
    <ul>
    ...

Further it provides a view to load a file from disc and its content to the template.
For this just Overwrite the LoadView

.. code-block:: python

    # views.py
    ...
    from utils.views import LoadView
    ...
    class View(LoadView):
        file_name = 'README.rst'
    ...
