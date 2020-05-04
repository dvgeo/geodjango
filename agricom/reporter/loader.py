import os
from django.contrib.gis.utils import LayerMapping
from .models import County

# Auto-generated `LayerMapping` dictionary for County model
county_mapping = {
    'country': 'COUNTRY',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'World_Countries.shp'),)

def run(verbose=True):
    lm = LayerMapping(County, county_shp, county_mapping, transform= False, encoding='UTF-8')
    lm.save(strict=True,verbose=verbose)