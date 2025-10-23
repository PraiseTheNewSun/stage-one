from django.shortcuts import render
from rest_framework import viewsets, status #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.decorators import api_view #type: ignore
from rest_framework.generics import ListAPIView #type: ignore
from .serializers import StringSerializer
from .models import StringModel
from .filters import StringFilter

import hashlib

# Create your views here.
@api_view(['POST'])
def StringAnalyzer(request):
    def is_palindrome(string):
        n_string = ''
        for i in string:
            if i.isalnum():
             n_string += i

        r_string = ''.join(reversed(n_string))
        return r_string == n_string
    
    def hasher(x):
        x_string = str(x)
        hash = hashlib.sha256()
        hash.update(x_string.encode('utf-8'))
        return hash.hexdigest()
    
    def unique_chars(string):
        u_string = set(string)
        return len(list(u_string))
    
    def word_count(string):
        return len(string.split(' '))
    
    def char_freq_map(string):
        dict = {}
        for i in sorted(set(string)):
            dict[f'{i}'] = string.count(i)
        return dict


    if request.method == 'POST':
        #queryset = StringAnalyzer.objects.all()
        serializer = StringSerializer(data=request.data)
        if serializer.is_valid():
            if StringModel.objects.filter(value=serializer.validated_data['value']).exists():
                return Response({'details': 'String already exists'}, status=status.HTTP_409_CONFLICT)
            else:
                serializer.save()
                return Response({
                    'id': hasher(serializer.data['id']),
                    'value': serializer.data['value'],
                    'properties': {
                        'length': len(serializer.data['value']),
                        'is_palindrome': is_palindrome(serializer.data['value']),
                        'unique_characters': unique_chars(serializer.data['value']),
                        'word_count': word_count(serializer.data['value']),
                        'sha256_hash': hasher(serializer.data['value']),
                        'character_frequency_map': char_freq_map(serializer.data['value'])
                    },
                    'created_at': serializer.data['created_at']
                    })
        else:
            return Response({'details': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def StringDetail(request, pk):
    def is_palindrome(string):
        n_string = ''
        for i in string:
            if i.isalnum():
             n_string += i

        r_string = ''.join(reversed(n_string))
        return r_string == n_string
    
    def hasher(x):
        x_string = str(x)
        hash = hashlib.sha256()
        hash.update(x_string.encode('utf-8'))
        return hash.hexdigest()
    
    def unique_chars(string):
        u_string = set(string)
        return len(list(u_string))
    
    def word_count(string):
        return len(string.split(' '))
    
    def char_freq_map(string):
        dict = {}
        for i in sorted(set(string)):
            dict[f'{i}'] = string.count(i)
        return dict
    
    if request.method == 'GET':
        #print(request.data)
        if StringModel.objects.filter(pk=pk).exists():
            d = StringModel.objects.get(pk=pk)
            return Response({
                'id': hasher(d.id),
                'value': d.value,
                'properties': {
                    'length': len(d.value),
                    'is_palindrome': is_palindrome(d.value),
                    'unique_characters': unique_chars(d.value),
                    'word_count': word_count(d.value),
                    'sha256_hash': hasher(d.value),
                    'character_frequency_map': char_freq_map(d.value)
                },
                'created_at': d.created_at
                })
        else:
            return Response({'details': 'String does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
class FilteredStringList(ListAPIView):
    queryset = StringModel.objects.all()
    serializer_class = StringSerializer
    filterset_class = StringFilter 
    
    # Optional: Add ordering support
    ordering_fields = ['is_palindrome', 'min_length', 'max_length', 'word_count', 'contains_character']