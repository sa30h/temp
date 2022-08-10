from rest_framework import serializers
from .models import *






class TempSerializer(serializers.ModelSerializer):
    class  Meta:
          model        =           Temp
          fields       =           '__all__'
