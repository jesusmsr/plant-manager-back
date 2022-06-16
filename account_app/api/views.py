from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib import auth

@api_view(['POST'])
def login_view(request):
    data = {}
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        
        account = auth.authenticate(email=email, password=password)
        if account is not None:
            data['response'] = '200'
            data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            
            return Response(data, status=status.HTTP_200_OK)
        else:
            data['error'] = 'bad credentials'
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)