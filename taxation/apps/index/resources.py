from import_export import resources
from .models import Index,City,Data

class IndexResource(resources.ModelResource):
    class Meta:
        model = Index

class CityResource(resources.ModelResource):
    class Meta:
        model = City

class DataResource(resources.ModelResource):
    class Meta:
        model = Data