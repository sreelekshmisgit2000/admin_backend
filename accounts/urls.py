from django.urls import path
from accounts.views import (
    CustomerSignupView,
    customer_login,
    VerifySignupOTPView,
    VerifyLoginOTPView,
)

urlpatterns = [
    path('signup/', CustomerSignupView.as_view(), name='customer-signup'),
    path('verify-signup-otp/', VerifySignupOTPView.as_view(), name='verify-signup-otp'),
    path('login/', customer_login, name='customer-login'),
    path('verify-login-otp/', VerifyLoginOTPView.as_view(), name='verify-login-otp'),
]
