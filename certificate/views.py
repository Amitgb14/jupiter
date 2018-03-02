# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, permissions

from .models import (Certificate,
                        CertificateInfo, 
                        CertificateAssign,
                        CertificateActive)

from .serializers import (CertificateSerializer,
                        CertificateInfoSerializer, 
                        CertificateAssignSerializer, 
                        CertificateActiveSerializer)



class CertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Certificate to be viewed or edited.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,


class CertificateInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CertificateInfo to be viewed or edited.
    """
    queryset = CertificateInfo.objects.all()
    serializer_class = CertificateInfoSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,

class CertificateAssignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CertificateAssign to be viewed or edited.
    """
    queryset = CertificateAssign.objects.all()
    serializer_class = CertificateAssignSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,

class CertificateActiveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CertificateActive to be viewed or edited.
    """
    queryset = CertificateActive.objects.all()
    serializer_class = CertificateActiveSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,
