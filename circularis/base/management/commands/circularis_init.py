from django.core.management.base import BaseCommand

from circularis.base.common import populate_database


class Command(BaseCommand):
    help = 'Populates auxiliary tables'

    def add_arguments(self, parser):
        parser.add_argument('--force-recreate', action='store_true', dest='force_recreate')

    def handle(self, *args, **options):
        recreate = options.get('force_recreate')
        populate_database(recreate)
        print("table(s) populated")
