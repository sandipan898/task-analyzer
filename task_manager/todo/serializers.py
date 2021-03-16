from rest_framework import serializers
from .models import List


class ListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=False, 
        max_length=500, 
    )
    weight = forms.IntegerField(
        required=False, 
    )

    class Meta:
        model = List
        fields = ["name", "weight", ]
        