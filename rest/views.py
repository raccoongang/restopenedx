from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest.helpers import get_course_policy, get_course_structure, get_scores
from rest.serializers import ScoreSerializer


class ScoreView(APIView):
    """
    A view that can accept POST requests with JSON content to save to DB TrackingLog model
    and parse on GET course data from openedx

    """
    parser_classes = (JSONParser,)

    @staticmethod
    def post(request, format=None):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @staticmethod
    def get(request):
        course_id = request.query_params.get('course_id', None)
        user_id = request.query_params.get('user_id', None)
        if course_id and user_id:
            # TODO: I don't know what to do with jsons: grading_policy, course_structure
            grading_policy = get_course_structure(course_id)
            course_structure = get_course_policy(course_id)
            scores = get_scores(course_id, user_id)
            return Response({'status': 'success'}, status=200)
        return Response({'error': 'course_id or user_id is None'}, status=400)
