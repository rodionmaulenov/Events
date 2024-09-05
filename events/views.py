from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .filters import EventFilter
from .models import Event, EventRegistration
from .serializers import EventSerializer, UserRegistrationSerializer, EventRegistrationSerializer
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer

    def perform_create(self, serializer):
        # add user who make request
        registration = serializer.save(user=self.request.user)

        # Send email notification
        self.send_registration_email(registration)

    def send_registration_email(self, registration):
        subject = f"Registration Confirmation for {registration.event.title}"
        message = (f"Hello {registration.user.username},\n\nYou have successfully registered for the event "
                   f"'{registration.event.title}' happening on {registration.event.date} "
                   f"at {registration.event.location}.\n\nThank you for registering!\n\nBest regards,\nEvent "
                   f"Management Team")
        recipient_list = [registration.user.email]
        from_email = settings.EMAIL_HOST_USER

        send_mail(subject, message, from_email, recipient_list)
