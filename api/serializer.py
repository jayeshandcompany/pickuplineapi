from rest_framework import serializers
from api.models import pickuplines


class pickuplineserializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = pickuplines
    fields = "__all__"
