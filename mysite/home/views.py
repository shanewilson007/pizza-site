from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from .models import Customer, BdayClub, Reservations
from django import forms
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)

class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)

class CareerView(TemplateView):
    template_name = 'home/careers.html'
    
    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)

class CateringView(TemplateView):
    template_name = 'home/catering.html'
    
    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)

class ClubView(TemplateView):
    template_name = 'home/club.html'

    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)

class EstimateView(TemplateView):
    template_name = 'home/estimate.html'

    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)

class MenuView(TemplateView):
    template_name = 'home/menu.html'
    
    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)

class ReservationView(TemplateView):
    template_name = 'home/reservations.html'
    
    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)
