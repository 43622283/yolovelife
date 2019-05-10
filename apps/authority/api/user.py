# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17-10-25
# Author Yo
# Email YoLoveLife@outlook.com
import pyotp
import os
from django.conf import settings
from qrcode import QRCode, constants
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import Response, status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.views import ObtainJSONWebToken
from deveops.api import WebTokenAuthentication
from deveops.utils import aes
from ..permissions import user as UserPermission
from ..serializers import user as serializer
from .. import models, filter
from timeline.decorator import decorator_base
from timeline.models import UserHistory

__all__ = [
    'UserLoginAPI', 'UserInfoAPI', 'UserListAPI',
    'UserUpdateAPI', 'UserDeleteAPI', 'UserPagination',
    'UserQRCodeAPI', 'UserCreateAPI', 'UserExpireAPI',
]


class UserLoginAPI(ObtainJSONWebToken):
    msg = settings.LANGUAGE.UserLoginAPI

    @decorator_base(UserHistory, timeline_type=settings.TIMELINE_KEY_VALUE['LOGIN'])
    def post(self, request, *args, **kwargs):
        response = super(UserLoginAPI, self).post(request, *args, **kwargs)
        return [None, ], self.msg.format(
            USERNAME=request.data['username']
        ), response


class UserInfoAPI(WebTokenAuthentication, APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        try:
            info_dist = dict()
            info_dist['username'] = request.user.username
            info_dist['name'] = request.user.full_name
            info_dist['info'] = request.user.info
            info_dist['pages'] = list(request.user.get_page_permissions())
            return Response(info_dist, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(dict(), status=status.HTTP_423_LOCKED)


class UserPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 50
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class UserListAPI(WebTokenAuthentication, generics.ListAPIView):
    serializer_class = serializer.UserSerializer
    queryset = models.ExtendUser.objects.filter(_visible=True)
    permission_classes = [UserPermission.UserListRequiredMixin, IsAuthenticated]
    pagination_class = UserPagination
    filter_class = filter.UserFilter


class UserCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    serializer_class = serializer.UserSerializer
    queryset = models.ExtendUser.objects.all()
    permission_classes = [UserPermission.UserCreateRequiredMixin, IsAuthenticated]
    msg = settings.LANGUAGE.UserCreateAPI

    @decorator_base(UserHistory, timeline_type=settings.TIMELINE_KEY_VALUE['USER_CREATE'])
    def create(self, request, *args, **kwargs):
        response = super(UserCreateAPI, self).create(request, *args, **kwargs)
        obj = models.ExtendUser.get(id=response.data['id'], uuid=response.data['uuid'])

        return [obj, ], self.msg.format(
            USER=request.user.full_name,
            USERNAME=response.data['username'],
            FULLNAME=response.data['full_name'],
        ), response


class UserUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.UserSerializer
    queryset = models.ExtendUser.objects.all()
    permission_classes = [UserPermission.UserUpdateRequiredMixin, IsAuthenticated]
    msg = settings.LANGUAGE.UserUpdateAPI

    @decorator_base(UserHistory, timeline_type=settings.TIMELINE_KEY_VALUE['USER_UPDATE'])
    def update(self, request, *args, **kwargs):
        response = super(UserUpdateAPI, self).update(request, *args, **kwargs)
        user = self.get_object()
        return [user, ], self.msg.format(
            USER=request.user.full_name,
            USERNAME=user.username,
            FULLNAME=user.full_name,
        ), response


class UserDeleteAPI(WebTokenAuthentication, generics.UpdateAPIView):
    serializer_class = serializer.UserDeleteSerializer
    queryset = models.ExtendUser.objects.all()
    permission_classes = [UserPermission.UserDeleteRequiredMixin, IsAuthenticated]
    msg = settings.LANGUAGE.UserDeleteAPI

    @decorator_base(UserHistory, timeline_type=settings.TIMELINE_KEY_VALUE['USER_DELETE'])
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        response = super(UserDeleteAPI, self).update(request, *args, **kwargs)
        return [user, ], self.msg.format(
            USER=request.user.full_name,
            USERNAME=user.username,
            FULLNAME=user.full_name,
        ), response


def get_qrcode(user):
    if not user.qrcode:
        user.qrcode = pyotp.random_base32()
        user.save()
    file_name = str(aes.encrypt(user.qrcode), encoding='utf-8')
    file = settings.QCODE_ROOT+'/'+file_name+'.png'
    if not os.path.exists(file):
        data = pyotp.totp.TOTP(user.qrcode).provisioning_uri(user.username, issuer_name='devEops')
        qr = QRCode(
            version=1,
            error_correction=constants.ERROR_CORRECT_L,
            box_size=6,
            border=4,)
        try:
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(file)
            return '/media/qrcode/' + file_name + '.png'
        except Exception as e:
            return '/media/qrcode/' + file_name + '.png'
    else:
        return '/media/qrcode/' + file_name + '.png'


class UserQRCodeAPI(WebTokenAuthentication, APIView):
    permission_classes = [IsAuthenticated, ]
    msg = settings.LANGUAGE.UserQRCodeAPI

    @decorator_base(UserHistory, timeline_type=settings.TIMELINE_KEY_VALUE['USER_QRCODE'])
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.have_qrcode is False:
            response_dist = {
                'url': get_qrcode(request.user)
            }
            user.have_qrcode = True
            user.save()
            response = Response(response_dist, status=status.HTTP_201_CREATED)
            return [None, ], self.msg.format(
                USER=request.user.full_name,
            ), response
        else:
            return [None, ], '', Response({
                'detail': settings.LANGUAGE.UserQRCodeAPIHaveQRCode
            }, status=status.HTTP_406_NOT_ACCEPTABLE)


class UserExpireAPI(WebTokenAuthentication, APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        return Response({
            'isexpire': request.user.is_expire
        }, status=status.HTTP_200_OK)
