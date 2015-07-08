from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest.serializers import TrackingLogSerializer


class TrackingLogView(APIView):
    """
    A view that can accept POST requests with JSON content. And try to save to DB TrackingLog model.
    """
    parser_classes = (JSONParser,)

    @staticmethod
    def post(request, format=None):
        serializer = TrackingLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
