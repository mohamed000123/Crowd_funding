from rest_framework import serializers
from projects import models


class ProjectsSer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = '__all__'


class ImageSer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectImages
        fields = '__all__'


class TagsSer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectTags
        fields = '__all__'


class RatingSer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectRating
        fields = '__all__'
