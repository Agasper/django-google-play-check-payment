from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^license', 'sg_license_service.views.license', name='license'),
)
