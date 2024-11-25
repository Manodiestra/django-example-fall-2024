import random
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserInfoForm
from .models import UserInfo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserInfoSerializer

class HelloWorldView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, World!"})

def generate_unique_user_id():
    while True:
        user_id = random.randint(100000, 999999)
        if not UserInfo.objects.filter(UserID=user_id).exists():
            return user_id

def registration_api(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.UserID = generate_unique_user_id()
            user_info.save()
            return JsonResponse({"message": "User info added successfully!"}, status=201)
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = UserInfoForm()
    return render(request, 'registration/registrationForm.html', {'form': form})


@api_view(['GET'])
def user_list_api(request):
    users = UserInfo.objects.all()
    serializer = UserInfoSerializer(users, many=True)
    return Response(serializer.data)


class AddUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get all users
        users = UserInfo.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        data['UserID'] = generate_unique_user_id()
        serializer = UserInfoSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
