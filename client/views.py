# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, permissions

from .models import User, Message
from .serializers import UserSerializer, MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ClientInfo to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Message to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,

