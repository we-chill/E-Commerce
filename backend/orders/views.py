from django.http import Http404
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template

from rest_framework import status, generics, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Order
from .serializers import OrderSerializer


class OrderDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user, id):
        try:
            return Order.objects.filter(user=user).get(id=id)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(user=request.user, id=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class OrderListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        # Sending email
        ctx = {
            'user': {
                'username': request.user.username,
                'email': request.user.email
            },
            'order': serializer.data
        }
        message = get_template('mail.html').render(ctx)
        subject = 'CONFIRMATION ORDER DETAILS FROM CHILL CHILL'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email, ]
        msg = EmailMessage(
            subject,
            message,
            email_from,
            recipient_list,
        )
        msg.content_subtype = 'html'
        msg.send()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
