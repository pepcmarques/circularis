from django.conf import settings
# from circularis import settings

import os
from circularis.books.models import Book


def clean_images():
    media_path = settings.MEDIA_ROOT
    thumbnails_path = os.path.join(media_path, 'thumbnails')

    all_files = [f for f in os.listdir(thumbnails_path)]

    db_files = [f.thumbnail.__str__().replace('thumbnails/', '').replace("b''", '') for f in Book.objects.all()]

    garbage_files = set(all_files) - set(db_files)

    n = 0
    for garbage in garbage_files:
        f = os.path.join(thumbnails_path, garbage)
        os.remove(f)
        print(f"{f} removed")
        n += 1
    return n
