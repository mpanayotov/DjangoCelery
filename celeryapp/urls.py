from django.conf.urls import url

from celeryapp.views import landing_page, run_async_tasks, run_sync_tasks

urlpatterns = [
    url(r'^$', landing_page, name = 'home'),
    url(r'^async_tasks/$', run_async_tasks, name='async'),
    url(r'^sync_tasks/$', run_sync_tasks, name='sync'),
]