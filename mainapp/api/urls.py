from subapp.views import index,person_crud,PersonViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person',PersonViewSet,basename='person')
urlpatterns = router.urls

urlpatterns = [
    
    path('',include(router.urls)),
    path('index/',index),
    path('person/',person_crud),
   

]