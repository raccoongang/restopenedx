import json
import requests
import urlparse
from django.conf import settings
from requests.exceptions import RequestException
from rest.models import Score


def send_request(url, params=None):
    """
    :param course_id: sting
    :param url: string (Course structure API endpoint)
    :return: Api request to url with param course_id
    """
    try:
        response = requests.get(url=url, params=params)
    except RequestException:
        raise RequestException
    return response.json()


def get_course_structure(course_id):
    FIELDS = ['has_score', 'weight', 'children', 'graded', 'format', 'always_recalculate_grades', 'max_score']
    url = urlparse.urljoin(settings.COURSE_STRUCTURE_API, '/courses/{course_id}/blocks/'.format(course_id=course_id))
    params = {'fields': ','.join(FIELDS)}
    return send_request(url, params)


def get_course_policy(course_id):
    url = urlparse.urljoin(settings.COURSE_STRUCTURE_API, '/grading_policies/{course_id}/'.format(course_id=course_id))
    return send_request(url)


def get_scores(course_id, user_id):
    return Score.objects.filter(course_id=course_id, user_id=user_id)
