from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
import random
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *

from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPagePly(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')

				group = Group.objects.get(name='Player')
				user.groups.add(group)

				messages.success(request, f" Player: {username} + has created Account")
				return redirect('login')
	context = {'form': form}
	return render(request,'registerp.html',context)
@unauthenticated_user
def registerPageDm(request):
    form = CreateUserForm()
    if request.method == "POST":
	    form = CreateUserForm(request.POST)
	    if form.is_valid():
			    user = form.save()
			    username = form.cleaned_data.get('username')

			    group = Group.objects.get(name='DM')
			    user.groups.add(group)

			    messages.success(request, "DM: " + username + " has created Account")
			    return redirect('login')
    context = {'form': form}
    return render(request,"registerdm.html", context)

def welcomeview(request):
    	return render(request,"welcome.html")

@unauthenticated_user
def loginPage(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
            	login(request, user)
            	return redirect('DMview')   
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def DMview(request):
    context = {}
    return render(request,"DMview.html", context)

def Pview(request):
    context = {}
    return render(request,"Pview.html", context)

@login_required(login_url='login')
def createmonsterview(request):
	form = CreateMonsterForm()
	context = {'form': form}
	if request.method == "POST":
		form = CreateMonsterForm(request.POST)
		if form.is_valid():
			monster = form.save()
			monster.creator = request.user
			monster.save()
			return redirect('DMview')
	return render(request,'create_monster.html',context)

@login_required(login_url='login')
def createcharacterview(request):
		form = CreateCharacterForm()
		context = {'form': form}
		if request.method == "POST":
			form = CreateCharacterForm(request.POST)
			if form.is_valid():
					character = form.save()
					character.creator = request.user
					character.save()
					return redirect('DMview')
		return render(request, 'create_character.html', context)

@login_required(login_url='login')
def updateCharacter(request, pk):

	order = Character.objects.get(id=pk)
	form = CreateCharacterForm(instance=order)

	if request.method == 'POST':
		form = CreateCharacterForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('DMview')

	context = {'form':form}
	return render(request, 'update_character.html', context)

@login_required(login_url='login')
def updateCharacterStats(request, pk):

	order = StatsC.objects.get(id=pk)
	form = CreateStatsCForm(instance=order)

	if request.method == 'POST':
		form = CreateStatsCForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('DMview')

	context = {'form':form}
	return render(request, 'updatec_stats.html', context)

@login_required(login_url='login')
def updateMonsterStats(request, pk):

	order = StatsM.objects.get(id=pk)
	form = CreateStatsMForm(instance=order)

	if request.method == 'POST':
		form = CreateStatsMForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('DMview')

	context = {'form':form}
	return render(request, 'updatem_stats.html', context)

@login_required(login_url='login')
def deleteCharacter(request, pk):
	character = Character.objects.get(id=pk)
	if request.method == "POST":
		character.delete()
		return redirect('DMview')

	context = {'item':character}
	return render(request, 'delete_character.html', context)

@login_required(login_url='login')
def updateMonster(request, pk):

	order = Monster.objects.get(id=pk)
	form = CreateMonsterForm(instance=order)

	if request.method == 'POST':
		form = CreateMonsterForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('DMview')

	context = {'form':form}
	return render(request, 'update_monster.html', context)

@login_required(login_url='login')
def deleteMonster(request, pk):
	monster = Monster.objects.get(id=pk)
	if request.method == "POST":
		monster.delete()
		return redirect('DMview')

	context = {'monster':monster}
	return render(request, 'delete_monster.html', context)


@login_required(login_url='login')
def createcampaignview(request):
		form = CreateCampaignForm()
		context = {'form': form}
		if request.method == "POST":
			form = CreateCampaignForm(request.POST)
			if form.is_valid():
					Campaign = form.save()
					Campaign.creator = request.user
					Campaign.save()
					return redirect('DMview')
		return render(request, 'create_Campaign.html', context)

@login_required(login_url='login')
def updateCampaign(request, pk):

	order = Campaign.objects.get(id=pk)
	form = CreateCampaignForm(instance=order)

	if request.method == 'POST':
		form = CreateCampaignForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('DMview')

	context = {'form':form}
	return render(request, 'update_campaign.html', context)

@login_required(login_url='login')
def deleteCampaign(request, pk):
	campaign = Campaign.objects.get(id=pk)
	if request.method == "POST":
		campaign.delete()
		return redirect('DMview')

	context = {'item':campaign}
	return render(request, 'delete_campaign.html', context)

@login_required(login_url='login')
def search_monster(request):
    if request.GET:
        search = request.GET["search"]
        monsters = Monster.objects.filter(name=search)
        return render(request, "search_monster.html", {"monsters":monsters})	
    return render(request, "search_monster.html")

@login_required(login_url='login')
def search_character(request):
    if request.GET:
        search = request.GET["search"]
        characters = Character.objects.filter(name=search)
        return render(request, "search_character.html", {"characters": characters})	
    return render(request, "search_character.html")

@login_required(login_url='login')
def search_campaign(request):
    if request.GET:
        search = request.GET["search"]
        campaigns = Campaign.objects.filter(name=search)
        return render(request, "search_campaign.html", {"campaigns":campaigns})	
    return render(request, "search_campaign.html")

@login_required(login_url='login')
def add_mstats_view(request,pk):
    monster = Monster.objects.get(id=pk)
    form = CreateStatsMForm()
    if request.method == 'POST':
        form = CreateStatsMForm(request.POST)
        if form.is_valid():
            monster.stats = form.save()
            monster.save()
            return redirect('DMview')

    context = {'form':form}
    return render(request, 'addm_stats.html', context)

@login_required(login_url='login')
def add_cstats_view(request,pk):
    character = Character.objects.get(id=pk)
    form = CreateStatsCForm()
    if request.method == 'POST':
        form = CreateStatsCForm(request.POST)
        if form.is_valid():
            character.stats = form.save()
            character.save()
            return redirect('DMview')

    context = {'form':form}
    return render(request, 'addc_stats.html', context)

@login_required(login_url='login')
def add_notes_view(request,pk):
    campaign = Campaign.objects.get(id=pk)
    form = CreateNoteForm()
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            note.campaign = campaign
            note.save()
            return redirect('DMview')

    context = {'form':form}
    return render(request, 'add_notes.html', context)

@login_required(login_url='login')
def view_monster(request, pk):
    monster = Monster.objects.get(id=pk)
    mc = Comment.objects.filter(monster=monster)
    
    form = CreateCommentForm()

    if request.method == "POST":
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.content = form.cleaned_data["content"]
            comment.monster = monster
            comment.user = request.user
            comment.save()
            monster.save()
            return redirect(f"/view_monster/{monster.id}")
    context = {
		"monster":monster,
		"form":form,
		'mc': mc
	}
    return render(request, 'monster_view.html', context)

@login_required(login_url='login')
def view_character(request, pk):
    character = Character.objects.get(id=pk)
    comments = Comment.objects.filter(character=character)
    form = CreateCommentForm()

    if request.method == "POST":
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.content = form.cleaned_data["content"]
            comment.character = character
            comment.user = request.user
            comment.save()
            character.save()
            return redirect(f"/view_character/{character.id}")

    context = {
		"character":character,
		"form":form,
		"comments":comments
	}

    return render(request, 'character_view.html', context)

@login_required(login_url='login')
def view_campaign(request, pk):
    campaign = Campaign.objects.get(id=pk)
    notes = Notes.objects.filter(campaign=campaign)
    context = {"campaign":campaign,"notes":notes}
    return render(request, 'campaign_view.html', context)


@login_required(login_url='login') 	
def random_characters(request):
    if request.method == 'POST':
        gender = ['male','female'] 
        name = random.choice(['Nalla','Skarde','Ødger','Torsten','Sten','Arne','Paikt','Ux',
		'Ziah','Ameria','Serena','Sariah','Chara','Annalisa','Kelsey','Octavia','Petyr','Sansa',
		'Yennefer','Albus','Emmett','Tyrion','Freya','Korra','Madeleine','Morgana','Ravenna',
		'Ambrose','Kirk','Aqua','Talus','Valatos','Dimitri','Zorn',])
        haircolor = ['Red','Blonde','Brown','Black','Blue','Green','Purple','White']
        hairlength = ['Short','Medium','Long']
        eyes = ['Red','Yellow','Hazel','Black','Blue','Green','Purple','White']
        feet = ['3','4','5','6','7','8']
        inches = ['0','1','2','3','4','5','6','7','8','9','10','11',]
        classes = random.choice(["Barbarian","Bard",  "Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer", "Warlock","Wizard"])
        races = random.choice(['Human','Elf','Dark Elf','Dwarf','Halfling','Teifling','Aarakocra','Dragonborn',
		'Genasi','Gnome','Goliath','Half-Elf','Half-Orc','Aasimar'])
        region = ['Esnuesia','Hasmeassau','Ofrurg','Sepreau','Strucor','Crubar','Oglon','Usmium','Skuiz Shium','Claum Snor',
		'Lestaoque','Yustiowana','Iesnad','Hosnus','Shiavania','Gluasal','Eflar','Adrya','Smaey Skein','Snov Spos']
        weight = random.randint(70,300)
        descript = f"{random.choice(gender)}, Has {random.choice(hairlength)} {random.choice(haircolor)} hair with {random.choice(eyes)} eyes,standing at {random.choice(feet)},{random.choice(inches)}ft weighing in at {weight} pounds, from the region of {random.choice(region)}"
        date_created = datetime.now()
        character = Character(name=name,descript=descript,race=races,classes=classes,date_created=date_created,creator=request.user,stats=None)
        character.save()
        return redirect('DMview')
    return render(request, 'random_character.html')


@login_required(login_url='login') 	
def random_monsters(request):
    if request.method == 'POST':
        name = random.choice(['Blightlich','Doomstep','Duskmonster','Razorcreep','Lean Guardian', 'Putrid Hybrid','Muted Woman', 'Spite Fiend','Razorback Cat', 'Mountain Rhino','Viletalon','Cryptfoot',"Cursehand",'Soilsoul','World Frog','Webbug', 'Nighthag','Cavecreep','Dustcrackle'])
        eyes = ['Red','Yellow','Hazel','Black','Blue','Green','Purple','White','Translucent', 'None']
        texture = ['Slimy','Smooth','Rough','Fluffy','Hairy','Bumpy']
        skincolor = ['Black','Red','Yellow','Green','Brown','White','Purple','Orange','Rainbow'] 
        height = random.randint(1,50) 
        weight = random.randint(10,5000)
        descript = f'Skin: {random.choice(skincolor)},{random.choice(texture)} Eyes: {random.choice(eyes)}  Height: {height}ft  Weight: {weight}'
        date_created = datetime.now()  
        monster = Monster(name=name,descript=descript,date_created=date_created,creator=request.user,stats=None)
        monster.save()
        return redirect('DMview')
    return render(request, 'random_monster.html')


	
