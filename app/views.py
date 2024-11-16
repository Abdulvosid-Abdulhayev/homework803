from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Travel, Klass, Mehmonxona
from .serializers import TravelSerializer, KlassSerializer, MehmonxonaSerializer

class KlassView(APIView):
    def get(self, request):
        klasslar = Klass.objects.all()
        serializer = KlassSerializer(klasslar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KlassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            klass = Klass.objects.get(pk=pk)
        except Klass.DoesNotExist:
            return Response({'error': 'Klass not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = KlassSerializer(klass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            klass = Klass.objects.get(pk=pk)
        except Klass.DoesNotExist:
            return Response({'error': 'Klass not found'}, status=status.HTTP_404_NOT_FOUND)
        klass.delete()
        return Response({'message': 'Klass deleted'}, status=status.HTTP_204_NO_CONTENT)


class MehmonxonaView(APIView):
    def get(self, request):
        mehmonxonalar = Mehmonxona.objects.all()
        serializer = MehmonxonaSerializer(mehmonxonalar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MehmonxonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            mehmonxona = Mehmonxona.objects.get(pk=pk)
        except Mehmonxona.DoesNotExist:
            return Response({'error': 'Mehmonxona not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MehmonxonaSerializer(mehmonxona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            mehmonxona = Mehmonxona.objects.get(pk=pk)
        except Mehmonxona.DoesNotExist:
            return Response({'error': 'Mehmonxona not found'}, status=status.HTTP_404_NOT_FOUND)
        mehmonxona.delete()
        return Response({'message': 'Mehmonxona deleted'}, status=status.HTTP_204_NO_CONTENT)


class TravelView(APIView):
    def get(self, request):
        travels = Travel.objects.all()
        serializer = TravelSerializer(travels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            travel = Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            return Response({'error': 'Travel not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TravelSerializer(travel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            travel = Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            return Response({'error': 'Travel not found'}, status=status.HTTP_404_NOT_FOUND)
        travel.delete()
        return Response({'message': 'Travel deleted'}, status=status.HTTP_204_NO_CONTENT)
