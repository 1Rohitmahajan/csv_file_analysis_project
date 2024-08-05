from django.db import models
from django.core.validators import MinLengthValidator

class New_User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_newuser_by_email(email):
        try:
            return New_User.objects.get(email=email)
        except New_User.DoesNotExist:
            return None

    def isExists(self):
        return New_User.objects.filter(email=self.email).exists()
