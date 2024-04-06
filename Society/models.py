from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.core.validators import MinLengthValidator

class Society(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    secretary_uid = models.UUIDField(default=uuid.uuid4, editable=False)
    resident_uid = models.UUIDField(default=uuid.uuid4, editable=False)


class ResidentProblem(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, related_name='resident_problems')
    problem_description = models.TextField()
    solved = models.BooleanField(default=False) 
    id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10, validators=[MinLengthValidator(1)]) 
    phone_number = models.CharField(max_length=20, validators=[MinLengthValidator(1)])

    def __str__(self):
        return self.problem_description[:50] 

