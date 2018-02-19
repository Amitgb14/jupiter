# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, permissions

from .models import (Certificate,
                        CertificateDuration, 
                        UserCertificate, 
                        UserActivateCertificate)

from .serializers import (CertificateSerializer,
                        CertificateDurationSerializer, 
                        UserCertificateSerializer, 
                        UserActivateCertificateSerializer)



class CertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Certificate to be viewed or edited.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,


class CertificateDurationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CertificateDuration to be viewed or edited.
    """
    queryset = CertificateDuration.objects.all()
    serializer_class = CertificateDurationSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,

class UserCertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows UserCertificate to be viewed or edited.
    """
    queryset = UserCertificate.objects.all()
    serializer_class = UserCertificateSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,

class UserActivateCertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows UserActivateCertificate to be viewed or edited.
    """
    queryset = UserActivateCertificate.objects.all()
    serializer_class = UserActivateCertificateSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,
