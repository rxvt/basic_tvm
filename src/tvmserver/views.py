import json

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from tvmserver.models import Command
from tvmserver.serializers import CrecentialSerializer

from rest_framework import generics


class CommandView(generics.RetrieveAPIView):
    queryset = Command.objects.filter(enabled=True)
    serializer_class = CrecentialSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        command_name = kwargs["command"]
        account = kwargs["account"]
        command = get_object_or_404(queryset, name=command_name)
        instance = {"command": command, "account": account}
        response = self.serializer_class(instance)
        return Response(response.data)
