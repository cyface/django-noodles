"""
Noodles URLs
"""
from django.conf.urls import patterns, url
from django.conf import settings
from django.views.generic import RedirectView
from noodles.views import contact, contact_thanks


urlpatterns = [
    url(r'^contact/$', contact, name='contact'),
    url(r'^contact/thanks/$', contact_thanks, name='contact_thanks'),
]


favicon_patterns = [
    url(r'^favicon\.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico'), name="favicon-ico"),
    url(r'^favicon\.png', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.png'), name="favicon-png"),
    url(r'^apple-touch-icon\.png$', RedirectView.as_view(url=settings.STATIC_URL + 'apple-touch-icon.png'), name="apple-touch-png"),
]
