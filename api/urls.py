from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health-check'),
    path('leads/student/', views.StudentLeadCreateView.as_view(), name='student-lead'),
    path('leads/industry/', views.IndustryLeadCreateView.as_view(), name='industry-lead'),
    path('newsletter/', views.NewsletterSubscribeView.as_view(), name='newsletter'),
    path('contact/', views.ContactInquiryCreateView.as_view(), name='contact'),
]
