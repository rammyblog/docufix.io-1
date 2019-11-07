from rest_framework import serializers
from .models import File, FileDelimeter, URLfield, duplicateURL

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("file1","file2")

class FileDelimeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileDelimeter
        fields = ("file1",)



class URLUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = URLfield
        fields = ("url1", "url2")

class DuplicateURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = duplicateURL
        fields = ("url1")