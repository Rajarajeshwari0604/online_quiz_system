from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/<int:quiz_id>/', views.quiz_page, name='quiz_page'),
    path('result/<int:quiz_id>/', views.result_page, name='result_page'),
]
