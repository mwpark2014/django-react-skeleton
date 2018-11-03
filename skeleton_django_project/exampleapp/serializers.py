from rest_framework import serializers
from leads.models import Lead
class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('id', 'name', 'email', 'message')