from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from oauth2_provider.models import Application

class Command(BaseCommand):
    help = "Creates a public OAuth2 application for the Flutter client"

    def handle(self, *args, **options):
        self.stdout.write("Setting up OAuth Application...")
        
        # Get a superuser to own the application
        user = User.objects.filter(is_superuser=True).first()
        if not user:
            # If no superuser exists, check if there's any user
            user = User.objects.first()
            if not user:
                self.stdout.write("Creating temporary user 'oauth_system' to own the application...")
                user = User.objects.create_user(
                    username='oauth_system', 
                    email='oauth@example.com', 
                    password='system_password_123'
                )
        
        app, created = Application.objects.get_or_create(
            client_id="meetflow-mobile-client",
            defaults={
                "name": "MeetFlow Mobile App",
                "client_type": Application.CLIENT_PUBLIC,
                "authorization_grant_type": Application.GRANT_PASSWORD,
                "user": user,
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS("Successfully created OAuth application 'MeetFlow Mobile App'"))
        else:
            # Ensure it is configured correctly if it already exists
            app.client_type = Application.CLIENT_PUBLIC
            app.authorization_grant_type = Application.GRANT_PASSWORD
            app.save()
            self.stdout.write("OAuth application 'MeetFlow Mobile App' configured successfully.")
