import os
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp


class Command(BaseCommand):
    help = 'Create or update the Google social app using environment variables.'

    def handle(self, *args, **kwargs):
        client_id = settings.GOOGLE_CLIENT_ID
        secret = settings.GOOGLE_CLIENT_SECRET

        if not client_id or not secret:
            self.stdout.write(self.style.ERROR('GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET must be set in the environment or .env file.'))
            return

        site, _ = Site.objects.get_or_create(
            id=settings.SITE_ID,
            defaults={
                'domain': 'localhost',
                'name': 'localhost',
            },
        )

        app, created = SocialApp.objects.update_or_create(
            provider='google',
            defaults={
                'name': 'Google',
                'client_id': client_id,
                'secret': secret,
            },
        )
        app.sites.set([site])
        app.save()

        if created:
            self.stdout.write(self.style.SUCCESS('Created Google SocialApp.'))
        else:
            self.stdout.write(self.style.SUCCESS('Updated Google SocialApp.'))
        self.stdout.write(self.style.SUCCESS(f'Attached Google SocialApp to site ID {site.id}.'))
