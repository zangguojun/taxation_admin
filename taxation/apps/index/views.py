from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from index.models import Index
from index.serialziers import IndexsCategorySerializer
from index.resources import IndexResource,CityResource

class IndexsFirstView(ListAPIView):
    pagination_class = None
    serializer_class = IndexsCategorySerializer
    queryset = Index.objects.filter(id__lte=3).all()

class IndexsOthersView(ListAPIView):
    pagination_class = None
    serializer_class = IndexsCategorySerializer
    def get_queryset(self):
        parent_id = self.kwargs.get("parent_id")
        return Index.objects.filter(parent_id=parent_id).all()

def tree(request):
    base_url = 'http://127.0.0.1:8000/indexs/categories/'
    import requests
    context = {}
    r1 = requests.get(base_url)
    for fir in r1.json():
        context[fir['name']] = {}
        r2 = requests.get(base_url+str(fir['id']))
        for sec in r2.json():
            context[fir['name']][sec['name']] = {}
            r3 = requests.get(base_url+str(sec['id']))
            for third in r3.json():
                context[fir['name']][sec['name']][third['name']] = None
    import json
    return render(request,'tree.html',{'tree_data':json.dumps(context)})

from tablib import Dataset
def simple_upload(request):
    if request.method == 'POST':
        index_resource = CityResource()
        dataset = Dataset()
        new_indexs = request.FILES['myfile']
        imported_data = dataset.load(new_indexs.read())
        result = index_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            index_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'import.html')