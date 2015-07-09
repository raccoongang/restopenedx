import json
from django.conf import settings
from pip._vendor.requests import RequestException
import requests
import urlparse


def get_api_course_request(course_id, url):
    """
    :param course_id: sting
    :param url: string
    :return: Api request to url with param course_id
    """

    url = urlparse.urljoin(url, course_id)
    try:
        response = requests.get(url=url)
    except RequestException:
        raise RequestException
    return json.loads(response.text)
