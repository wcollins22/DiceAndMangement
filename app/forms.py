from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import request
from .models import Character
from django.contrib.auth.models import User
from app.models import  *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateMonsterForm(ModelForm):
    class Meta:
        model = Monster
        fields ='__all__'
        exclude = ['creator', 'stats', 'comments']

class CreateCharacterForm(ModelForm):
    class Meta:
        model = Character
        fields ='__all__'
        exclude = ['creator', 'stats']


class CreateStatsMForm(ModelForm):
    class Meta:
        model = StatsM
        fields = '__all__'
        exclude = ['monster']

class CreateStatsCForm(ModelForm):
    class Meta:
        model = StatsC
        fields = '__all__'
        exclude = ['character']

class CreateCampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'
        exclude = ['creator']

class CreateNoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        exclude = ['campaign']

class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        exclude = ("user",)