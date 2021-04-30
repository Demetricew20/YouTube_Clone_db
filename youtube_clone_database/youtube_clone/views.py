from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from .serializers import VideoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class VideoList(APIView):

    def get(self, request):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDetail(APIView):

    def get_by_pk(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST

    def get(self, request, pk):
        video = self.get_by_pk(pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)


    def put(self, request, pk):
        video = self.get_by_pk(pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        video = self.get_by_pk(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        video = self.get_by_pk(pk)
        serializer = VideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            video.likes += 1
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED),
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def dislike_video(self, request, pk):
        video = self.get_by_pk(pk)
        serializer = VideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            video.likes -= 1
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)