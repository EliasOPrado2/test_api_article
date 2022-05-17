from django.forms import modelformset_factory
from rest_framework import serializers
from tourism.models import Destinations, Comment

class DestinationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destinations
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

        