from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Curation
# from django.contrib.auth import get_user_model
from .serializers import CurationSerializer


@api_view(['GET'])
def curation_list(request):
    curations = get_list_or_404(Curation)
    serializer = CurationSerializer(curations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def curation_detail(request, curation_pk):
    curation = get_object_or_404(Curation, pk=curation_pk)
    serializer = CurationSerializer(curation)
    return Response(serializer.data)
