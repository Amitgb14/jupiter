# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from client.views import UserViewSet, MessageViewSet
from certificate.views import (CertificateViewSet,
                        CertificateDurationViewSet, 
                        UserCertificateViewSet,
                        UserActivateCertificateViewSet)

router = routers.DefaultRouter()
router.register(r'client/user', UserViewSet)
router.register(r'client/message', MessageViewSet)


router.register(r'certificate/certificate', CertificateViewSet)
router.register(r'certificate/certificateduration', CertificateDurationViewSet)
router.register(r'certificate/usercertificate', UserCertificateViewSet)
router.register(r'certificate/useractivatecertificate', UserCertificateViewSet)

urlpatterns = [

   url(r'^', include(router.urls)),

]