from django.contrib import admin
from django.urls import path,include
from book.views import Category
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

# router.register('',Category,basename='SignUP')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('book.urls')),
    # path('',include(router.urls))
]
