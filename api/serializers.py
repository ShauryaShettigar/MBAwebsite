from rest_framework import serializers
from .models import StudentLead, IndustryLead, NewsletterSubscriber, ContactInquiry


class StudentLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLead
        fields = '__all__'
        read_only_fields = ['created_at']


class IndustryLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryLead
        fields = '__all__'
        read_only_fields = ['created_at']


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = '__all__'
        read_only_fields = ['created_at']


class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = '__all__'
        read_only_fields = ['created_at']
