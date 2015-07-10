import json
import requests
import urlparse
from django.conf import settings
from requests.exceptions import RequestException
from rest.models import Score


def send_request(url, params=None):
    """
    :param url: string
    :return: Response content
    """
    try:
        response = requests.get(url=url, params=params)
    except RequestException:
        raise RequestException
    return response.json()


def get_course_structure(course_id):
    FIELDS = ['has_score', 'weight', 'children', 'graded', 'format', 'always_recalculate_grades', 'max_score']
    url = urlparse.urljoin(settings.COURSE_STRUCTURE_API, '/courses/{course_id}/blocks/'.format(course_id=course_id))
    return send_request(url, params={'fields': ','.join(FIELDS)})


def get_course_policy(course_id):
    url = urlparse.urljoin(settings.COURSE_STRUCTURE_API, '/grading_policies/{course_id}/'.format(course_id=course_id))
    return send_request(url)


def get_scores(course_id, user_id):
    return Score.objects.filter(course_id=course_id, user_id=user_id)
