from django.conf import settings
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest.helpers import get_api_course_request
from rest.serializers import TrackingLogSerializer


class ScoreView(APIView):
    """
    A view that can accept POST requests with JSON content to save to DB TrackingLog model
    and parse on GET course data from openedx

    """
    parser_classes = (JSONParser,)

    @staticmethod
    def post(request, format=None):
        serializer = TrackingLogSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @staticmethod
    def get(request):
        course_id = request.query_params.get('course_id', None)
        if course_id:
            # TODO: I don't know what to do with jsons: grading_policy, course_structure
            grading_policy = get_api_course_request(course_id, settings.API_COURSE_STRUCTURE_URL)
            course_structure = get_api_course_request(course_id, settings.API_COURSE_GRADING_POLICY)
            return Response({'status': 'success'}, status=201)
        return Response({'error': 'Course_id is None'}, status=400)
