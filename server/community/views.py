from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Curation
# from django.contrib.auth import get_user_model
from .serializers import CurationSerializer

# curation 
@api_view(['GET', 'POST'])
def curation_list(request):
    if request.method == 'GET':
        curations = get_list_or_404(Curation)
        serializer = CurationSerializer(curations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CurationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def curation_detail(request, curation_pk):
    curation = get_object_or_404(Curation, pk=curation_pk)
    if request.method == 'GET':
        serializer = CurationSerializer(curation)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        curation.delete()
        data = {
            'delete': f'{curation_pk}번 큐레이션이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CurationSerializer(curation, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

            