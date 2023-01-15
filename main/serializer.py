from rest_framework.serializers import ModelSerializer
from .models import *


class SliderSerializer(ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'



class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        


class DirectionSerializer(ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'
        


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ResultItemSerializer(ModelSerializer):
    class Meta:
        model = ResultItem
        fields = '__all__'



class ResultSerializer(ModelSerializer):
    class Meta:
        depth = 1
        model = Result
        fields = '__all__'
                


