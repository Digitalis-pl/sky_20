from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='zhora.karsakov@mail.ru',
            first_name='Admin',
            last_name='Me',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('stripedHat80')
        user.save()
