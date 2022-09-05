from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Agent, Simulation
from datetime import date

class SimulationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    track_id = serializers.CharField(max_length=255, validators=[UniqueValidator(Simulation.objects.all(), 'Id already exists')])
    carrieout_date = serializers.DateField(default=date.today) # 'yyyy-mm-dd'
    agent_count = serializers.IntegerField(read_only=True)
    finished_agents = serializers.IntegerField(read_only=True)
    average_agent_time = serializers.IntegerField(read_only=True)
    total_colisions = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Simulation.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.track_id = validated_data.get('track_id', instance.track_id)
        instance.carrieout_date = validated_data.get('carrieout_date', instance.track_id)

        instance.save()

        return instance
