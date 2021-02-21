from django.http import Http404
from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Order
from .serializers import OrderSerializer


class OrderList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        today = date.today()
        buf = Order.objects.filter(
            order_by=request.user,
            table=request.data['table'],
            created_at__year=today.year,
            created_at__month=today.month,
            created_at__day=today.day
        )
        if buf:
            return Response(
                'Please try another table',
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, format=None):
        order = self.get_object(request.data['id'])
        serializer = OrderSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
