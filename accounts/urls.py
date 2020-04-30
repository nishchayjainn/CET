from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
	path('',include('djoser.urls')),
	path('',include('djoser.urls.authtoken')),
	path('signup/',views.RegistrationView.as_view()),
	path('login/',views.ProfileView.as_view())
]