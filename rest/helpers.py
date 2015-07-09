import json
from django.conf import settings
from requests.exceptions import RequestException
import requests
import urlparse


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
    get_course_api(settings.COURSE_STRUCTURES_URL, course_id)


def get_course_policy(course_id):
    get_course_api(settings.COURSE_GRADING_POLICY_URL, course_id)
