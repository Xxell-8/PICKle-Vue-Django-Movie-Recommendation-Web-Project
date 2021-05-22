from rest_framework import serializers
from .models import Curation
from movies.serializers import MovieSerializer


class CurationSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Curation
        fields = '__all__'
        