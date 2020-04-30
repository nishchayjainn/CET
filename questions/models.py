from django.db import models

# Create your models here.

question       = models.CharField(max_length = 500,blank=False)
option1        = models.BooleanField(default=False)
option2        = models.BooleanField(default=False)
option3        = models.BooleanField(default=False)
option4        = models.BooleanField(default=False)
correct_answer = models.IntegerField(blank=False,default = 0)

