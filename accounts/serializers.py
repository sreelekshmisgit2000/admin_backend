from rest_framework import serializers
from accounts.models import CustomUser
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import PasswordResetOTP



class CustomerSignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    is_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'is_verified']

    def validate_email(self, value):
        if " " in value:
            raise serializers.ValidationError("Email should not contain spaces.")
        if '@' not in value:
            raise serializers.ValidationError("Email must contain '@'.")
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError("Password must include at least one uppercase letter.")
        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError("Password must include at least one lowercase letter.")
        if not re.search(r"[0-9]", value):
            raise serializers.ValidationError("Password must include at least one number.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise serializers.ValidationError("Password must include at least one special character.")
        return value

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['email'],  
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_customer=True,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


User = get_user_model()

class SendPasswordResetOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyPasswordResetOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        otp = data.get('otp')

        try:
            otp_obj = PasswordResetOTP.objects.get(email=email, otp=otp)
        except PasswordResetOTP.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP.")

        if otp_obj.is_expired():
            raise serializers.ValidationError("OTP has expired.")

        return data


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(min_length=6)
