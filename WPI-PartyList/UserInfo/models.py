from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

# def filepath(self, filename):
# 	"""
# 		Defines where files uploaded by the user should be stored
# 	"""
# 	return "users/" + self.user.username + "/" + filename

class Fraternity(models.Model):
    name = models.CharField(max_length=100)
    manager = models.OneToOneField(User)

    @staticmethod
    def managers():
        return [f.manager for f in Fraternity.objects.all()]

    def brothers(self):
        users = UserInfo.objects.filter(fraternity=self)
        print users
        print UserInfo.objects.all()
        return users

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Fraternities"
        verbose_name = "Fraternity"

class UserInfo(models.Model):
    """
        Model for site-specific user info.
        Complements the built in User models
    """
    user = models.OneToOneField(User)
    fraternity = models.ForeignKey(Fraternity)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "User Info"
        verbose_name = "User Info"
        permissions = (
            ("manage_users", "Can manage users."),
            )


class EditUserInfoForm(ModelForm):
    """
        Form for editing a user
    """
    fraternity = forms.CharField(required=True)

    class Meta:
        model = UserInfo
        exclude = ['user']
