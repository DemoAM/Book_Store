from rest_framework import viewsets
from .serializers import AuthorSerializer,CategorySerializers
from.models import Author,BookCategory
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.views import LogoutView



class Category(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = CategorySerializers



