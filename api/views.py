from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import StudentLead, IndustryLead, NewsletterSubscriber, ContactInquiry
from .serializers import (
    StudentLeadSerializer, IndustryLeadSerializer,
    NewsletterSubscriberSerializer, ContactInquirySerializer,
)


class StudentLeadCreateView(generics.CreateAPIView):
    queryset = StudentLead.objects.all()
    serializer_class = StudentLeadSerializer


class IndustryLeadCreateView(generics.CreateAPIView):
    queryset = IndustryLead.objects.all()
    serializer_class = IndustryLeadSerializer


class NewsletterSubscribeView(generics.CreateAPIView):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Successfully subscribed to newsletter.'},
                status=status.HTTP_201_CREATED,
            )
        if 'email' in serializer.errors and any(
            'unique' in str(e) for e in serializer.errors['email']
        ):
            return Response(
                {'message': 'This email is already subscribed.'},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactInquiryCreateView(generics.CreateAPIView):
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer


@api_view(['GET'])
def health_check(request):
    return Response({'status': 'ok'})
