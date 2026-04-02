import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Donor, NGOCampaign, Volunteer


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['donor_count'] = Donor.objects.count()
    ctx['donor_individual'] = Donor.objects.filter(donor_type='individual').count()
    ctx['donor_corporate'] = Donor.objects.filter(donor_type='corporate').count()
    ctx['donor_foundation'] = Donor.objects.filter(donor_type='foundation').count()
    ctx['donor_total_total_donated'] = Donor.objects.aggregate(t=Sum('total_donated'))['t'] or 0
    ctx['ngocampaign_count'] = NGOCampaign.objects.count()
    ctx['ngocampaign_active'] = NGOCampaign.objects.filter(status='active').count()
    ctx['ngocampaign_completed'] = NGOCampaign.objects.filter(status='completed').count()
    ctx['ngocampaign_paused'] = NGOCampaign.objects.filter(status='paused').count()
    ctx['ngocampaign_total_goal_amount'] = NGOCampaign.objects.aggregate(t=Sum('goal_amount'))['t'] or 0
    ctx['volunteer_count'] = Volunteer.objects.count()
    ctx['volunteer_active'] = Volunteer.objects.filter(status='active').count()
    ctx['volunteer_inactive'] = Volunteer.objects.filter(status='inactive').count()
    ctx['volunteer_pending'] = Volunteer.objects.filter(status='pending').count()
    ctx['recent'] = Donor.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def donor_list(request):
    qs = Donor.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(donor_type=status_filter)
    return render(request, 'donor_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def donor_create(request):
    if request.method == 'POST':
        obj = Donor()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.total_donated = request.POST.get('total_donated') or 0
        obj.donations_count = request.POST.get('donations_count') or 0
        obj.donor_type = request.POST.get('donor_type', '')
        obj.status = request.POST.get('status', '')
        obj.last_donation = request.POST.get('last_donation') or None
        obj.save()
        return redirect('/donors/')
    return render(request, 'donor_form.html', {'editing': False})


@login_required
def donor_edit(request, pk):
    obj = get_object_or_404(Donor, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.total_donated = request.POST.get('total_donated') or 0
        obj.donations_count = request.POST.get('donations_count') or 0
        obj.donor_type = request.POST.get('donor_type', '')
        obj.status = request.POST.get('status', '')
        obj.last_donation = request.POST.get('last_donation') or None
        obj.save()
        return redirect('/donors/')
    return render(request, 'donor_form.html', {'record': obj, 'editing': True})


@login_required
def donor_delete(request, pk):
    obj = get_object_or_404(Donor, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/donors/')


@login_required
def ngocampaign_list(request):
    qs = NGOCampaign.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'ngocampaign_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def ngocampaign_create(request):
    if request.method == 'POST':
        obj = NGOCampaign()
        obj.title = request.POST.get('title', '')
        obj.goal_amount = request.POST.get('goal_amount') or 0
        obj.raised_amount = request.POST.get('raised_amount') or 0
        obj.donors_count = request.POST.get('donors_count') or 0
        obj.status = request.POST.get('status', '')
        obj.start_date = request.POST.get('start_date') or None
        obj.end_date = request.POST.get('end_date') or None
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/ngocampaigns/')
    return render(request, 'ngocampaign_form.html', {'editing': False})


@login_required
def ngocampaign_edit(request, pk):
    obj = get_object_or_404(NGOCampaign, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.goal_amount = request.POST.get('goal_amount') or 0
        obj.raised_amount = request.POST.get('raised_amount') or 0
        obj.donors_count = request.POST.get('donors_count') or 0
        obj.status = request.POST.get('status', '')
        obj.start_date = request.POST.get('start_date') or None
        obj.end_date = request.POST.get('end_date') or None
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/ngocampaigns/')
    return render(request, 'ngocampaign_form.html', {'record': obj, 'editing': True})


@login_required
def ngocampaign_delete(request, pk):
    obj = get_object_or_404(NGOCampaign, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/ngocampaigns/')


@login_required
def volunteer_list(request):
    qs = Volunteer.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'volunteer_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def volunteer_create(request):
    if request.method == 'POST':
        obj = Volunteer()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.skills = request.POST.get('skills', '')
        obj.hours_contributed = request.POST.get('hours_contributed') or 0
        obj.status = request.POST.get('status', '')
        obj.availability = request.POST.get('availability', '')
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/volunteers/')
    return render(request, 'volunteer_form.html', {'editing': False})


@login_required
def volunteer_edit(request, pk):
    obj = get_object_or_404(Volunteer, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.skills = request.POST.get('skills', '')
        obj.hours_contributed = request.POST.get('hours_contributed') or 0
        obj.status = request.POST.get('status', '')
        obj.availability = request.POST.get('availability', '')
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/volunteers/')
    return render(request, 'volunteer_form.html', {'record': obj, 'editing': True})


@login_required
def volunteer_delete(request, pk):
    obj = get_object_or_404(Volunteer, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/volunteers/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['donor_count'] = Donor.objects.count()
    data['ngocampaign_count'] = NGOCampaign.objects.count()
    data['volunteer_count'] = Volunteer.objects.count()
    return JsonResponse(data)
