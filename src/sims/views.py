from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import SimulationSerializer
from .models import Agent, Simulation

# Create your views here.
def tester(request):
    sim = Simulation.objects.get(pk=1)

    print('Track Id', sim.track_id)
    print('Date', sim.carrieout_date)
    print('Agent Count', sim.agent_count)
    print('Agent Finish', sim.finished_agents)
    print('Agent Time', sim.average_agent_time)
    print('Total Colisions', sim.total_colisions)

    return HttpResponse('hi')

@api_view(['GET', 'POST'])
def sim_list(request):
    if request.method == 'GET':
        sims = Simulation.objects.all()
        serializer = SimulationSerializer(sims, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SimulationSerializer(data=data, many=True)
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sim_detail(request, pk):
    try:
        sim = Simulation.objects.get(pk=pk)
    except Simulation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SimulationSerializer(sim)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SimulationSerializer(sim, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sim.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




