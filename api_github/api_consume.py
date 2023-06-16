from requests import get as get_url
from typing import Dict

def api_github_get(url:str,params:Dict={}, headers:Dict={}):
    return get_url(url=url, params=params, headers=headers)