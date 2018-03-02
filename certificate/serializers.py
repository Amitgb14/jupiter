# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from .models import (Certificate,
                        CertificateInfo, 
                        CertificateAssign, 
                        CertificateActive)


class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Certificate
        fields =  ('id', 'certificate_name', 'status')


class CertificateInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CertificateInfo
        fields =  ('id', 'certificate', 'duration', 'cost', 'status')


class CertificateAssignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CertificateAssign
        fields =  ('id', 'client', 'certificate_unique_id', 'certificate', 'created_date', 'activate', 'status')


class CertificateActiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CertificateActive
        fields =  ('id', 'certificate', 'certificate_text', 'issued_by', 'issued_date', 'expired_date', 'status')

