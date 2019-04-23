import certifi
import urllib3

class API(object):

    def get_response(self, url):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        response = http.request('GET', url)
        return response



    def get_file(self, url, path):

        http = urllib3.PoolManager()
        r = http.request('GET', url, preload_content=False)

        with open(path, 'wb') as out:
            while True:
                data = r.read(1024)
                if not data:
                    break
                out.write(data)

        r.release_conn()