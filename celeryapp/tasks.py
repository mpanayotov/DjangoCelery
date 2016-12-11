from celery import shared_task
import requests

@shared_task
def retrieve_response(url):
    try:
        r = requests.get(url)
        return r.status_code
    except Exception as e:
        return str(e)

@shared_task
def retrieve_fb_id_by_profile_url(url):
    try:
        lookup_url = "http://findmyfbid.com/"
        data = {"url": url}
        r = requests.post(lookup_url, data)
        fb_id = find_between(r.text, '<code>', '</code>')
        return fb_id
    except Exception as e:
        return str(e)

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""