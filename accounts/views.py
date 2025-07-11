from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
import json
import random
from accounts.serializers import CustomerSignupSerializer
from accounts.models import CustomUser
from otp_app.models import OTP



class CustomerSignupView(APIView):
    def post(self, request):
        serializer = CustomerSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

   
            OTP.objects.filter(user=user).delete()

        
            otp_code = str(random.randint(10000, 99999))
            OTP.objects.create(user=user, code=otp_code)

         
            try:
                send_mail(
                    subject='Signup OTP',
                    message=f'Hi {user.first_name}, your OTP is: {otp_code}',
                    from_email='sreelekshmisgit@gmail.com',
                    recipient_list=[user.email],
                    fail_silently=False,
                )
                print(" OTP sent to:", user.email)
            except Exception as e:
                print("Email sending failed:", str(e))
                return Response({"message": "Signup successful, but email failed to send."}, status=500)

            return Response({"message": "Customer registered successfully. OTP sent to email."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifySignupOTPView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")

        try:
            user = CustomUser.objects.get(email=email)
            latest_otp = OTP.objects.filter(user=user).order_by("-created_at").first()

            if latest_otp:
                
                if timezone.now() > latest_otp.created_at + timezone.timedelta(minutes=1):
                    return Response({"status": "fail", "message": "OTP expired"}, status=400)

                if latest_otp.code == otp:
                    user.is_verified = True
                    user.save()
                    return Response({"status": "success", "message": "Signup OTP verified"}, status=200)

            return Response({"status": "fail", "message": "Invalid OTP"}, status=400)
        except CustomUser.DoesNotExist:
            return Response({"status": "fail", "message": "User not found"}, status=404)


@csrf_exempt
def customer_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return JsonResponse({"status": "fail", "message": "Email and password are required"}, status=400)

        user = authenticate(request, username=email, password=password)

        if user is not None and not user.is_staff:
          
            OTP.objects.filter(user=user).delete()

            
            otp_code = str(random.randint(10000, 99999))
            OTP.objects.create(user=user, code=otp_code)

            send_mail(
                subject='Login OTP',
                message=f'Hi {user.first_name}, your OTP is: {otp_code}',
                from_email='sreelekshmisgit@gmail.com',
                recipient_list=[user.email],
                fail_silently=False,
            )

            return JsonResponse({
                "status": "success",
                "message": "OTP sent to email. Please verify.",
                "email": email
            }, status=200)
        else:
            return JsonResponse({"status": "fail", "message": "Invalid credentials or not a customer"}, status=401)

    return JsonResponse({"status": "error", "message": "Only POST method allowed"}, status=405)


class VerifyLoginOTPView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")

        try:
            user = CustomUser.objects.get(email=email)
            latest_otp = OTP.objects.filter(user=user).order_by("-created_at").first()

            if latest_otp:
              
                if timezone.now() > latest_otp.created_at + timezone.timedelta(minutes=1):
                    return Response({"status": "fail", "message": "OTP expired"}, status=400)

                if latest_otp.code == otp:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        "status": "success",
                        "message": "Login successful",
                        "access": str(refresh.access_token),
                        "refresh": str(refresh),
                        "username": user.username
                    }, status=200)

            return Response({"status": "fail", "message": "Invalid OTP"}, status=400)
        except CustomUser.DoesNotExist:
            return Response({"status": "fail", "message": "User not found"}, status=404)
