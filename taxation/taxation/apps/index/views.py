from rest_framework.generics import ListAPIView
from index.models import Index
from index.serialziers import IndexsCategorySerializer

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