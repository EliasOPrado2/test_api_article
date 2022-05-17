from rest_framework import viewsets
from .serializers import DestinationsSerializer, CommentSerializer
from tourism.models import Destinations, Comment


class DestinationsViewset(viewsets.ModelViewSet):
    queryset = Destinations.objects.all()
    serializer_class = DestinationsSerializer

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer