from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest.utils import get_course_policy, get_course_structure, get_scores
from rest.serializers import ScoreSerializer
from rest.graders.graders import get_grader


class ScoreView(APIView):
    """
    A view that can accept POST requests with JSON content to save to DB Score model
    and parse on GET course data from openedx.
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
        grading_type = request.query_params.get('grading_type', None)

        if not all([course_id, user_id]):
            return Response({'error': 'course_id or user_id is None.'}, status=400)

        course_structure = get_course_structure(course_id)
        course_policy = get_course_policy(course_id)
        scores = get_scores(course_id, user_id)

        try:
            grader = get_grader(grading_type)
        except KeyError:
            return Response({'error': 'Incorrect grading type.'}, status=400)

        result = grader.grade(course_structure, course_policy, scores)
        return Response(result, status=200)
