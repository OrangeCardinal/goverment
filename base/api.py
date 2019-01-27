import certifi
import urllib3

class API(object):

    def get_response(self, url):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        response = http.request('GET', url)
        return response