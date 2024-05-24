import random
from django.shortcuts import render
from api import serializer
from rest_framework import viewsets
from api.models import pickuplines
from api.serializer import pickuplineserializer
from rest_framework.decorators import action
from rest_framework.response import Response


class pickuplinesviewset(viewsets.ModelViewSet):
  queryset = pickuplines.objects.all()
  serializer_class = pickuplineserializer

  @action(methods=['get'], detail=False)
  def random(self, request):
    r = random.randint(1, 114)
    pickupline = pickuplines.objects.get(id=r)
    serial = pickuplineserializer(pickupline, context={'request': request})
    return Response(serial.data)


# Create your views here.
