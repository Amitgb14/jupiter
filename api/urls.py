# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from client.views import UserViewSet, MessageViewSet
from certificate.views import (CertificateViewSet,
                        CertificateInfoViewSet, 
                        CertificateAssignViewSet,
                        CertificateActiveViewSet)

router = routers.DefaultRouter()
router.register(r'client/user', UserViewSet)
router.register(r'client/message', MessageViewSet)


router.register(r'certificate/certificate', CertificateViewSet)
router.register(r'certificate/certificateinfo', CertificateInfoViewSet)
router.register(r'certificate/certificateassign', CertificateAssignViewSet)
router.register(r'certificate/certificateactive', CertificateActiveViewSet)

urlpatterns = [

   url(r'^', include(router.urls)),

]
