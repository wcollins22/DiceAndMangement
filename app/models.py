from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.deletion import CASCADE, PROTECT
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Character(models.Model):
    RACES = (
       ("Human", "Human"),
       ("Elf", "Elf"),
       ("Dark Elf", "Dark Elf"),
       ("Dwarf", "Dwarf"),
       ("Halfling", "Halfling"),
       ("Teifling", "Teifling"),
       ("Aarakocra", "Aarakocra"),
       ("Dragonborn", "Dragonborn"),
       ("Genasi", "Genasi"),
       ("Gnome", "Gnome"),
       ("Goliath", "Goliath"),
       ("Half-Elf", "Half-Elf"),
       ("Half-Orc", "Half-Orc"),
       ("Aasimar", "Aasimar")
    )
    CLASS = (
       ("Barbarian", "Barbarian"),
       ("Bard", "Bard"),
       ("Cleric", "Cleric"),
       ("Druid", "Druid"),
       ("Fighter", "Fighter"),
       ("Monk", "Monk"),
       ("Paladin", "Paladin"),
       ("Ranger", "Ranger"),
       ("Rogue", "Rogue"),
       ("Sorcerer", "Sorcerer"),
       ("Warlock", "Warlock"),
       ("Wizard", "Wizard")
    )
    name = models.CharField(max_length=200, null=True)
    descript = models.CharField(max_length=10000)
    race = models.CharField(max_length=200, null=True,choices=RACES)
    classes = models.CharField(max_length=200, null=True,choices=CLASS)
    date_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, null=True, default=User)
    


    def __str__(self) -> str:
           return self.name


class StatsC(models.Model):
    Hp = models.PositiveIntegerField(null=True)
    Str = models.PositiveIntegerField(null=True)
    Dex = models.PositiveIntegerField(null=True)
    Con = models.PositiveIntegerField(null=True)
    Int = models.PositiveIntegerField(null=True)
    Wis = models.PositiveIntegerField(null=True)
    Cha = models.PositiveIntegerField(null=True)
    Walk = models.PositiveIntegerField(null=True, validators=[MinValueValidator(10),MaxValueValidator(60)])
    character = models.OneToOneField(Character,on_delete=models.PROTECT, null=True)



class Monster(models.Model):
   name = models.CharField(max_length=200, null=True)
   descript = models.CharField(max_length=10000, null=True)
   date_created = models.DateTimeField(auto_now_add=True)
   creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, null=True, default=User)
   

   def __str__(self) -> str:
       return self.name

class StatsM(models.Model):
    hp = models.PositiveIntegerField(null=True)
    Str = models.PositiveIntegerField(null=True)
    Dex = models.PositiveIntegerField(null=True)
    Con = models.PositiveIntegerField(null=True)
    Int = models.PositiveIntegerField(null=True)
    Wis = models.PositiveIntegerField(null=True)
    Cha = models.PositiveIntegerField(null=True)
    Walk = models.PositiveIntegerField(null=True)
    monster = models.ForeignKey(Monster, on_delete=models.PROTECT,null=True)
    

class Campaign(models.Model):
    name = models.CharField(max_length=200)
    descript = models.CharField(max_length=3000)
    date_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User,on_delete=models.PROTECT, null=True)


class Notes(models.Model):
    descript = models.CharField(max_length=3000)
    campaign = models.ForeignKey(Campaign,on_delete=models.PROTECT, null=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT, null=True)
    monster = models.ForeignKey(Monster,on_delete=models.PROTECT, null=True)
    content = models.CharField(max_length=10000, null=True)

    def __str__(self) -> str:
        return self.content
