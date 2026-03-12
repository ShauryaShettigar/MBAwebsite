from django.db import models


class StudentLead(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    current_qualification = models.CharField(max_length=200, blank=True)
    years_of_experience = models.CharField(max_length=50, blank=True)
    area_of_interest = models.CharField(max_length=300, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.email}"


class IndustryLead(models.Model):
    ENGAGEMENT_CHOICES = [
        ('faculty', 'Guest Faculty'),
        ('mentor', 'Mentor'),
        ('advisor', 'Advisory Board'),
        ('hiring', 'Hiring Partner'),
        ('speaker', 'Guest Speaker'),
        ('other', 'Other'),
    ]
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    designation = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    engagement_type = models.CharField(max_length=50, choices=ENGAGEMENT_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.organization}"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactInquiry(models.Model):
    INQUIRY_CHOICES = [
        ('student', 'Prospective Student'),
        ('industry', 'Industry Professional'),
        ('media', 'Media / Press'),
        ('general', 'General Inquiry'),
    ]
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    inquiry_type = models.CharField(max_length=50, choices=INQUIRY_CHOICES)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Contact inquiries'

    def __str__(self):
        return f"{self.full_name} - {self.subject}"
