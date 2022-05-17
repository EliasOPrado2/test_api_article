from django.urls import include, path
from rest_framework import routers
from tourism.api.viewsets import DestinationsViewset, CommentViewset

router = routers.DefaultRouter()
router.register(r"destinations", DestinationsViewset, basename="destinations")
router.register(r"comments", CommentViewset, basename="comments")

app_name = 'tourism'

urlpatterns = [
    path('', include(router.urls)),
]
