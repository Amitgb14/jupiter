# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from .models import (Certificate,
                        CertificateDuration, 
                        UserCertificate, 
                        UserActivateCertificate)


class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Certificate
        fields =  ('id', 'certificate_name', 'status')


class CertificateDurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CertificateDuration
        fields =  ('id', 'certificate', 'duration', 'cost', 'status')


class UserCertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserCertificate
        fields =  ('id', 'client', 'certificate_unique_id', 'certificate', 'created_date', 'activate', 'status')


class UserActivateCertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserActivateCertificate
        fields =  ('id', 'certificate', 'certificate_text', 'issued_by', 'issued_date', 'expired_date', 'status')

