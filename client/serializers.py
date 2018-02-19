# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from .models import User, Message


#-----------------pod-----------------#
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =  ('id', 'first_name', 'last_name', 'contact_no', 'status')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.CharField(source='user.username')
    class Meta:
        model = Message
        fields = ('id', 'user', 'message', 'read', 'date', 'status')

