from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import ServiceRequest, RequestAttachment, CustomerProfile, RequestNote
from .forms import (
    ServiceRequestForm, RequestAttachmentForm, CustomerProfileForm,
    RequestNoteForm, ServiceRequestUpdateForm, UserRegisterForm
)
from django.contrib.auth import login

@login_required
def dashboard(request):
    user_requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')
    paginator = Paginator(user_requests, 10)
    page = request.GET.get('page')
    requests = paginator.get_page(page)
    return render(request, 'customer_services/dashboard.html', {'requests': requests})

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            messages.success(request, 'Service request created successfully!')
            return redirect('customer_services:service_request_detail', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_services/create_request.html', {'form': form})

@login_required
def service_request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.user != service_request.customer and not request.user.is_staff:
        messages.error(request, 'You do not have permission to view this request.')
        return redirect('customer_services:dashboard')
    
    attachments = service_request.attachments.all()
    notes = service_request.notes.all().order_by('-created_at')
    
    if request.method == 'POST':
        if 'add_note' in request.POST:
            note_form = RequestNoteForm(request.POST)
            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.service_request = service_request
                note.author = request.user
                note.save()
                messages.success(request, 'Note added successfully!')
                return redirect('customer_services:service_request_detail', pk=pk)
        elif 'add_attachment' in request.POST:
            attachment_form = RequestAttachmentForm(request.POST, request.FILES)
            if attachment_form.is_valid():
                attachment = attachment_form.save(commit=False)
                attachment.service_request = service_request
                attachment.save()
                messages.success(request, 'Attachment added successfully!')
                return redirect('customer_services:service_request_detail', pk=pk)
    else:
        note_form = RequestNoteForm()
        attachment_form = RequestAttachmentForm()
    
    context = {
        'service_request': service_request,
        'attachments': attachments,
        'notes': notes,
        'note_form': note_form,
        'attachment_form': attachment_form,
    }
    return render(request, 'customer_services/request_detail.html', context)

@login_required
def update_service_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to update this request.')
        return redirect('customer_services:dashboard')
    
    if request.method == 'POST':
        form = ServiceRequestUpdateForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service request updated successfully!')
            return redirect('customer_services:service_request_detail', pk=pk)
    else:
        form = ServiceRequestUpdateForm(instance=service_request)
    
    return render(request, 'customer_services/update_request.html', {'form': form, 'service_request': service_request})

@login_required
def profile(request):
    try:
        profile = request.user.customerprofile
    except CustomerProfile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('customer_services:profile')
    else:
        form = CustomerProfileForm(instance=profile)
    
    return render(request, 'customer_services/profile.html', {'form': form})

@login_required
def staff_dashboard(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('customer_services:dashboard')
    
    all_requests = ServiceRequest.objects.all().order_by('-created_at')
    paginator = Paginator(all_requests, 20)
    page = request.GET.get('page')
    requests = paginator.get_page(page)
    
    return render(request, 'customer_services/staff_dashboard.html', {'requests': requests})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('customer_services:dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
