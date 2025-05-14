from django.contrib import admin
from .models import ServiceRequest, RequestAttachment, CustomerProfile, RequestNote

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'request_type', 'status', 'priority', 'created_at', 'updated_at', 'assigned_to')
    list_filter = ('status', 'request_type', 'priority', 'created_at')
    search_fields = ('customer__username', 'customer__email', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(RequestAttachment)
class RequestAttachmentAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'file', 'uploaded_at', 'description')
    list_filter = ('uploaded_at',)
    search_fields = ('service_request__customer__username', 'description')
    date_hierarchy = 'uploaded_at'

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'account_number', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone_number', 'account_number')
    date_hierarchy = 'created_at'

@admin.register(RequestNote)
class RequestNoteAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('service_request__customer__username', 'content', 'author__username')
    date_hierarchy = 'created_at'
