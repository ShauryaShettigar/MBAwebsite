from django.contrib import admin
from .models import StudentLead, IndustryLead, NewsletterSubscriber, ContactInquiry


@admin.register(StudentLead)
class StudentLeadAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'current_qualification', 'created_at']
    search_fields = ['full_name', 'email']
    list_filter = ['created_at']


@admin.register(IndustryLead)
class IndustryLeadAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'organization', 'designation', 'engagement_type', 'created_at']
    search_fields = ['full_name', 'email', 'organization']
    list_filter = ['engagement_type', 'created_at']


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
    search_fields = ['email']


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'inquiry_type', 'subject', 'created_at']
    search_fields = ['full_name', 'email', 'subject']
    list_filter = ['inquiry_type', 'created_at']
