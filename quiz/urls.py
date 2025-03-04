from django.urls import path
from quiz import views

urlpatterns = [
    path('', views.quiz, name='quiz'),  # Quiz page
    path('submit/', views.submit_quiz, name='submit_quiz'),  # Handle form submission
]

