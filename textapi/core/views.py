from django.shortcuts import render

# DRF core classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

import re   # For word tokenization

# Authentication and session tools
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.shortcuts import redirect

# Swagger documentation helpers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import UserSerializer
from .models import Paragraph, WordIndex
from .models import User

# Home view: shows a welcome message if user is authenticated
def home_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user.name
    return render(request, 'core/base.html', {'user_name': user})

# Logout the user and redirect to homepage
def logout_view(request):
    logout(request)
    return redirect('/')

# Render the user registration page
def register_view(request): 
    return render(request, 'core/register.html')

# Render the login page
def login_view(request): 
    return render(request, 'core/login.html')

# Render paragraph upload page; requires login
@login_required(login_url='/login/')
def upload_view(request): 
    return render(request, 'core/upload.html', {'user_name': request.user.name})

# Render search page; requires login
@login_required(login_url='/login/')
def search_view(request): 
    return render(request, 'core/search.html', {'user_name': request.user.name})

# Handles user registration via API
class RegisterView(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=201)
        return Response(serializer.errors, status=400)


# Authenticates user and returns token
class LoginView(APIView):
    @swagger_auto_schema(
        operation_summary="Login with email and password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email", "password"],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format='password')
            }
        ),
        responses={
            200: openapi.Response(
                description="Login successful",
                examples={"application/json": {"token": "string", "name": "User Name"}}
            ),
            401: openapi.Response(description="Invalid credentials")
        }
    )
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'name': user.name})  
        return Response({'error': 'Invalid credentials'}, status=401)


#paragraph upload

@swagger_auto_schema(
    method='post',
    operation_summary="Upload multiple paragraphs",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["text"],
        properties={
            "text": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Multiple paragraphs separated by two newlines"
            )
        }
    ),
    responses={200: openapi.Response(description="Paragraphs stored successfully")},
    security=[{'Token': []}]
)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def upload_paragraphs(request):
    text = request.data.get('text', '')
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]   # Split by double newlines

    for p in paragraphs:
        para_obj = Paragraph.objects.create(text=p)
        words = re.findall(r'\b\w+\b', p.lower())       # Tokenize paragraph into lowercase words
        for word in words:
            WordIndex.objects.create(word=word, paragraph=para_obj)
    return Response({"message": "Paragraphs stored successfully"})


# Word search

@swagger_auto_schema(
    method='get',
    operation_summary="Search a word in stored paragraphs",
    manual_parameters=[
        openapi.Parameter(
            'word',
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=True,
            description="Word to search in paragraphs"
        )
    ],
    responses={
        200: openapi.Response(
            description="List of paragraphs containing the searched word",
            examples={
                "application/json": {
                    "paragraphs": ["Para 1...", "Para 2..."]
                }
            }
        ),
        400: "Missing required 'word' query parameter"
    },
    security=[{'Token': []}]
)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search_word(request):
    query = request.query_params.get('word', '').lower()
    if not query:
        return Response({'error': 'word is required'}, status=400)
    
    # Get all paragraphs that contain the word
    paragraphs = Paragraph.objects.filter(words__word=query).distinct()[:10]
    return Response({'paragraphs': [p.text for p in paragraphs]})




