"""
Test case URLS
"""
from django.conf.urls import url
from django.views.generic import TemplateView
from noodles_tests.views import home
from noodles.views import contact, contact_thanks

urlpatterns = [
    url(r'^$', home, name='test_home'),
    url(r'^contact/$', contact, name='contact', kwargs={"template_name": "noodles_tests/contact.html"}),
    url(r'^contact/thanks/$', contact_thanks, name='contact_thanks', kwargs={"template_name": "noodles_tests/contact_thanks.html"}),
    url(r'^processors/$', TemplateView.as_view(template_name="noodles_tests/all_processors.html"), name='all_processors'),
]
