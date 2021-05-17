from rest_framework import serializers
from index.models import Index

class IndexsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = ("id","name")
