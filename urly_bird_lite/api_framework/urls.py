from django.conf.urls import include, url
from api_framework.views import UrlListView, UrlDetailView, UserList, UserDetail


urlpatterns = [
    url(r'^url/$', UrlListView.as_view(), name='url_list'),
    url(r'^url/(?P<pk>\d+)/$', UrlDetailView.as_view(), name='url_detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view()),
]
