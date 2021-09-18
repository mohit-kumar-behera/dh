from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model, authenticate
from accounts.api.utils import create_response_obj
import json

User = get_user_model()

@csrf_exempt
def login_api_handler(request):
    if request.method == 'POST':
        req_data = json.loads(request.body.decode('utf-8'))
        email = req_data.get('email')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            print("email or pwd incoreect")
            status = 404
            response_obj = create_response_obj(status, False, 'email address or password is incorrect')
        else:
            password = req_data.get('password')
            user_isAuthenticated = authenticate(request, email=email, password=password)
            if user_isAuthenticated:
                status = 200
                response_obj = create_response_obj(status, True, f'You can log in the user - {email}')
            else:
                status = 404
                response_obj = create_response_obj(status, False, 'email address or password is incorrect')

    return HttpResponse(json.dumps(response_obj), status=status)


@csrf_exempt
def register_api_handler(request):
    if request.method == 'POST':
        req_data = json.loads(request.body.decode('utf-8'))
        email = req_data.get('email')
        password = req_data.get('password')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            # Continue with user creation
            user = User.objects.create_user(email=email, password=password)
            user.save()
            status = 201
            response_obj = create_response_obj(status, True, 'User created successfully')
        else:
            # User with this email already exists
            status = 400
            response_obj = create_response_obj(status, False, 'User with this email address already exists')

    return HttpResponse(json.dumps(response_obj), status=status)