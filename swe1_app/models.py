from statistics import mode
from tkinter.messagebox import QUESTION
from django.db import models
from pandas import option_context

# Create your models here.


class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question}: {self.option_one}, {self.option_two} or {self.option_three}?"
