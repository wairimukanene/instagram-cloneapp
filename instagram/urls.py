from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.landing, name='landing'),
    url(r'^new/post/$', views.new_post, name='new-post'),
    url(r'^new/profile/$', views.new_profile, name='new-profile'),
    url(r'^profile/(?P<profile_id>\d+)', views.profile, name='profile'),
    url(r'^user_profile/(?P<username>\w+)', views.user_profile, name='user_profile'),
    url(r'^post/(?P<id>\d+)', views.post_comment, name='comment'),
    url(r'^search/', views.search_profile, name='search'),
]