from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class BlackListTokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(data={'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)
