from django.http import JsonResponse
from .models import Message
from .serializer import MessageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(["GET", "POST"])
def message_list(request):
    if request.method == "GET":
        message = Message.objects.all().order_by("-date")
        serializer = MessageSerializer(message, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(["GET", "PUT", "DELETE"])
def message_detail(request, pk):
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = MessageSerializer(message)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)