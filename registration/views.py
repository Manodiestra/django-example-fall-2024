import random
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserInfoForm
from .models import UserInfo

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
