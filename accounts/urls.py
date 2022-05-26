from django.urls import path

from accounts.views import SignUpAPIView, SignInView

urlpatterns = [
    path('signup/', SignUpAPIView.as_view()),
    path('signin/', SignInView.as_view()),
]