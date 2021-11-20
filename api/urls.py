from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("Material_List",views.MatlView)

urlpatterns = [
   path('',include(router.urls))]
