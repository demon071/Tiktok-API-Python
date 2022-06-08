import json
from urllib.parse import urlparse, parse_qs, urlencode

def parse_query(url):
    result = urlparse(url)
    query = result.query
    query_dict = parse_qs(query)
    query_dict = {k: v[0] for k, v in query_dict.items()}
    return query_dict

def process_browser_log_entry(entry):
    response = json.loads(entry['message'])['message']
    return response

def set_url(domain, _dict):
    path = urlencode(_dict)
    url = domain + '?%s' % path
    return url

def get_param_url(_dict):
    return urlencode(_dict)
