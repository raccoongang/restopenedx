import json
import requests
import urlparse
from django.conf import settings
from requests.exceptions import RequestException
from rest.models import Score


def get_course_api(url, course_id):
    """
    :param course_id: sting
    :param url: string (Course structure API endpoint)
    :return: Api request to url with param course_id
    """
    url = urlparse.urljoin(url, course_id)
    try:
        response = requests.get(url=url)
    except RequestException:
        raise RequestException
    return json.loads(response.text)


def get_course_structure(course_id):
    url = urlparse.urljoin(settings.COURSE_STRUCTURE_API, '/course_structures/')
    get_course_api(url, course_id)


def get_course_policy(course_id):
    url = urlparse.urljoin(settings.COURSE_STRUCTURE_API, '/grading_policies/')
    get_course_api(url, course_id)


def get_scores(course_id, user_id):
    return Score.objects.filter(course_id=course_id, user_id=user_id)
