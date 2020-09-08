from django.conf import settings
from django.apps import apps

from mapbox import Geocoder


def get_models(app_name):
    my_app = apps.get_app_config(app_name)
    return my_app.models.values()


def populate_database(recreate=False):
    project_apps = [app.split('.')[-1] for app in settings.INSTALLED_APPS if settings.SYSTEM_NAME.lower() in app]
    for app in project_apps:
        tables = get_models(app)
        for table in tables:
            try:
                table.objects.populate(recreate=recreate)
            except AttributeError:
                pass


def get_latitude_longitude(address_instance=None):
    if address_instance is None:
        return None, None
    address = address_instance.to_str()
    geocode = Geocoder(access_token=settings.MAPBOX_ACCESS_KEY)
    response = geocode.forward(address=address)
    json_data = response.json()
    # get latitude and longitude from json_data
    features = json_data.get('features')
    best_result = features[0]
    center = best_result.get('center', [None, None])
    return center
