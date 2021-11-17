"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerply/', views.registerPagePly, name="registerp"),
    path('registerDM/', views.registerPageDm, name="registerdm"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('welcome/', views.welcomeview, name='welcome'),
    path('DMpage/',views.DMview, name='DMview'),
    path('Playerpage/',views.Pview, name='Pview'),
    path('Create_Monster', views.createmonsterview, name='CreateMonster'),
    path('Create_Character', views.createcharacterview, name='CreateCharacter'),
    path('Create_Campaign', views.createcampaignview, name='CreateCampaign'),
    path('Update_Monster/<str:pk>/', views.updateMonster, name='UpdateMonster'),
    path('Update_Character/<str:pk>/', views.updateCharacter, name='UpdateCharacter'),
    path('Update_Campaign/<str:pk>/', views.updateCampaign, name='UpdateCampaign'),
    path('Delete_Monster/<str:pk>/', views.deleteMonster, name='DeleteMonster'),
    path('Delete_Character/<str:pk>/', views.deleteCharacter, name='DeleteCharacter'),
    path('Delete_Campaign/<str:pk>/', views.deleteCampaign, name='DeleteCampaign'),
    path("search_monster/", views.search_monster, name="search-m"),
    path("search_character/", views.search_character, name="search-c"),
    path("search_campaign/", views.search_campaign, name="search-ca"),
    path("add_stats_m/<str:pk>/", views.add_mstats_view, name="m_stats"),
    path("add_stats_c/<str:pk>/", views.add_cstats_view, name="c_stats"),
    path("add_notes/<str:pk>/", views.add_notes_view, name="notes"),
    path('view_monster/<str:pk>/', views.view_monster, name='view_monster'),
    path('view_character/<str:pk>/', views.view_character, name='view_character'),
    path('view_campaign/<str:pk>/', views.view_campaign, name='view_campaign'),
    path('random_character/',views.random_characters, name='randomch')
   

]
