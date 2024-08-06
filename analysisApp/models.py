from django.db import models

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


class Contact(models.Model):
    name = models.CharField(null=False, blank=False, max_length=122)
    email = models.CharField(null=False, blank=False, max_length=122)
    phone = models.CharField(null=False, blank=False, max_length=12)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
