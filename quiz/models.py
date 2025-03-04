# quiz/models.py
from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)  # Store the correct answer

    def __str__(self):
        return self.text

