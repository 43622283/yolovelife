# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from datetime import datetime, date, timedelta
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response, status
from django.db.models import Q
from scene.permission import workorder as WorkOrderPermission
from .. import models, serializers, filter
from deveops.api import WebTokenAuthentication
from timeline.models import SceneHistory
from timeline.serializers import SceneHistorySerializer
from timeline.decorator import decorator_workorder
from django.conf import settings

__all__ = [
    'WorkOrderPagination', 'SceneWorkOrderCreateAPI', 'SceneWorkOrderDeleteAPI',
    'SceneWorkOrderListByPageAPI', 'SceneWorkOrderUpdateAPI'
]


class WorkOrderPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 60
    page_size_query_param = 'pageSize'
    page_query_param = 'current'


class SceneWorkOrderListAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.WorkOrder
    serializer_class = serializers.WorkOrderSerializer
    queryset = models.WorkOrder.objects.all().order_by('_status')[:7]
    # permission_classes = [WorkOrderPermission.WorkOrderListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]


class SceneWorkOrderMobileDetailAPI(WebTokenAuthentication, generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = models.WorkOrder.objects.all()

    def list(self, request, *args, **kwargs):
        user = request.user

        from django.utils import timezone
        now = timezone.now().date()
        start_day = now - timedelta(days=1)
        end_day = now - timedelta(days=1)

        work_order = user.workorders.filter(
            create_time__gt=start_day, create_time__lt=end_day
        )

        return Response(
            # {
            #     'workorder_total_count': work_order.count(),
            #     'workorder_undone_count': work_order.filter(~Q(_status=2)).count(),
            #     'full_name': user.full_name,
            # },
            {
                'workorder_total_count': 36,
                'workorder_undone_count': 2,
                'full_name': user.full_name,
            }
            , status.HTTP_200_OK
        )


class SceneWorkOrderListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.WorkOrder
    serializer_class = serializers.WorkOrderSerializer
    queryset = models.WorkOrder.objects.all()
    # permission_classes = [WorkOrderPermission.WorkOrderListRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    pagination_class = WorkOrderPagination
    filter_class = filter.WorkOrderFilter


class SceneWorkOrderCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.WorkOrder
    serializer_class = serializers.WorkOrderSerializer
    permission_classes = [WorkOrderPermission.WorkOrderCreateRequiredMixin, IsAuthenticated]
    msg = settings.LANGUAGE.SceneWorkOrderCreateAPI

    @decorator_workorder(timeline_type=settings.TIMELINE_KEY_VALUE['WORKORDER_CREATE'])
    def create(self, request, *args, **kwargs):
        response = super(SceneWorkOrderCreateAPI, self).create(request, *args, **kwargs)
        obj = models.WorkOrder.objects.get(id=response.data['id'], uuid=response.data['uuid'])
        return obj, self.msg.format(
            USER=request.user.full_name,
        ), response


class SceneWorkOrderUpdateAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.WorkOrder
    serializer_class = serializers.WorkOrderSerializer
    queryset = models.WorkOrder.objects.all()
    permission_classes = [WorkOrderPermission.WorkOrderUpdateRequiredMixin, IsAuthenticated]
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"
    msg = settings.LANGUAGE.SceneWorkOrderUpdateAPI

    @decorator_workorder(timeline_type=settings.TIMELINE_KEY_VALUE['WORKORDER_UPDATE'])
    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.duty_user.id != request.user.id:
            return None, '', Response({'detail': u'您修改不是您负责的工单，请先转接工单。'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        response = super(SceneWorkOrderUpdateAPI, self).update(request, *args, **kwargs)
        return obj, self.msg.format(
            USER=request.user.full_name,
        ), response


class SceneWorkOrderActiveAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.WorkOrder
    serializer_class = serializers.WorkOrderActiveSerializer
    queryset = models.WorkOrder.objects.all()
    permission_classes = [AllowAny, ]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    msg = settings.LANGUAGE.SceneWorkOrderActiveAPI

    @decorator_workorder(timeline_type=settings.TIMELINE_KEY_VALUE['WORKORDER_ACTIVE'])
    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        response = super(SceneWorkOrderActiveAPI, self).update(request, *args, **kwargs)
        return obj, self.msg.format(
            USER=request.user.full_name,
        ), response


class SceneWorkOrderAppointAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.WorkOrder
    serializer_class = serializers.WorkOrderAppointSerializer
    queryset = models.WorkOrder.objects.all()
    permission_classes = [AllowAny, ]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    msg = settings.LANGUAGE.SceneWorkOrderAppointAPI

    @decorator_workorder(timeline_type=settings.TIMELINE_KEY_VALUE['WORKORDER_APPOINT'])
    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.duty_user.id != request.user.id:
            return None, '', Response({'detail': u'您无法指派不是您负责的工单。'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        new_duty_user = models.ExtendUser.objects.get(id=request.data['appoint_id'])
        response = super(SceneWorkOrderAppointAPI, self).update(request, *args, **kwargs)
        return obj, self.msg.format(
            USER1=request.user.full_name,
            USER2=new_duty_user.full_name,
            REASON=request.data['reason']
        ), response


class SceneWorkOrderDoneAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.WorkOrder
    serializer_class = serializers.WorkOrderDoneSerializer
    queryset = models.WorkOrder.objects.all()
    permission_classes = [AllowAny,]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    msg = settings.LANGUAGE.SceneWorkOrderDoneAPI

    @decorator_workorder(timeline_type=settings.TIMELINE_KEY_VALUE['WORKORDER_DONE'])
    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.duty_user.id != request.user.id:
            return None, '', Response({'detail': u'您完结不是您负责的工单，请先转接工单。'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        response = super(SceneWorkOrderDoneAPI, self).update(request, *args, **kwargs)
        return obj, self.msg.format(
            USER=request.user.full_name,
        ), response


class SceneWorkOrderDeleteAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.WorkOrder
    serializer_class = serializers.WorkOrderSerializer
    queryset = models.WorkOrder.objects.all()
    # permission_classes = [WorkOrderPermission.WorkOrderDeleteRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny,]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'
    # msg = settings.LANGUAGE.SceneWorkOrderDeleteAPI

    # @decorator_api(timeline_type=settings.TIMELINE_KEY_VALUE['HOST_DELETE'])
    # def update(self, request, *args, **kwargs):
    #     if self.qrcode_check(request):
    #         host = self.get_object()
    #         response = super(SceneWorkOrderDeleteAPI, self).update(request, *args, **kwargs)
    #         return self.msg.format(
    #             USER=request.user.full_name,
    #             HOSTNAME=host.hostname,
    #             CONNECT_IP=host.connect_ip,
    #             UUID=host.uuid,
    #         ), response
    #     else:
    #         return '', self.qrcode_response


class SceneWorkOrderDetailAPI(WebTokenAuthentication, generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = models.WorkOrder.objects.all()
    lookup_field = "uuid"
    lookup_url_kwarg = "pk"

    def list(self, request, *args, **kwargs):
        obj = self.get_object()

        timeline_queryset = SceneHistory.objects.filter(
            workorder=obj
        ).order_by('-id')

        timeline_serializer = SceneHistorySerializer(timeline_queryset, many=True)

        comment_serializer = serializers.CommentSerializer(obj.comments.order_by('create_time'), many=True)

        current_serializer = serializers.WorkOrderSerializer(obj,)

        order_queryset = models.WorkOrder.objects.filter(
            (~Q(phone='') & Q(phone=obj.phone))
            | (~Q(user='') & Q(user=obj.user))
            | (~Q(serial_number='') & Q(serial_number=obj.serial_number))
        ).exclude(id=obj.id).exclude(user='', phone='')[:10]

        order_serializer = serializers.WorkOrderSerializer(order_queryset, many=True)
        return Response(
            {
                'current': current_serializer.data,
                'timeline': timeline_serializer.data,
                'order': order_serializer.data,
                'comment': comment_serializer.data,
            }, status.HTTP_200_OK
        )


class SceneWorkOrderCommentAPI(WebTokenAuthentication, generics.UpdateAPIView):
    module = models.WorkOrder
    serializer_class = serializers.WorkOrderCommentSerializer
    queryset = models.WorkOrder.objects.all()
    # permission_classes = [RepositoryPermission.RepositoryDeleteRequiredMixin, IsAuthenticated]
    permission_classes = [AllowAny, ]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'pk'