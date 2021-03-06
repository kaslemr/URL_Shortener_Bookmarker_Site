from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.serializers import ModelSerializer
from urlshorten.models import URL
from rest_framework import routers, serializers
from django.contrib.auth.models import User



# Create your views here.
from urlshorten.views import CreateUser


class UrlSerializer(ModelSerializer):

    class Meta:
        model = URL
        fields = ('id', 'url', 'description', 'shortened_url')

class UrlListView(ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = UrlSerializer

    #def get_queryset(self):
        #user = self.request.user
        #return URL.objects.filter(author__id=user)


class UrlDetailView(RetrieveUpdateDestroyAPIView):
    queryset = URL.objects.all()
    serializer_class = UrlSerializer

class UserList(ListAPIView):
    queryset = User.objects.all()

    class Meta:
        model = User
        fields = ('id', 'username', 'urls')

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
