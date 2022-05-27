from django.urls import path

urlpatterns = [
    path('categories/', ProductAPIView.as_view(), name='categories'),
]