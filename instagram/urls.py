from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^profile/(\d+)$',views.profile,name='profile'),
    url(r'^profile/update/(\d+)$',views.update_profile,name='update_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/image/(\d+)$',views.new_image,name="new_image"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)