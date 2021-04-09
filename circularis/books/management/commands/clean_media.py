from django.core.management.base import BaseCommand

from circularis.books.common import clean_images


class Command(BaseCommand):
    help = 'Clean media directory'

    # def add_arguments(self, parser):
    #     parser.add_argument('--force-recreate', action='store_true', dest='force_recreate')

    def handle(self, *args, **options):
        # recreate = options.get('force_recreate')
        print(f"{clean_images()} were removed")
