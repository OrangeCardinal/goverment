from math import floor
import certifi
import json
import urllib3

class EDGAR():
    """
    https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm

    """
    __BASE_URL = "https://www.sec.gov"
    __DAILY_INDEX_URL = "{0}/{1}".format(__BASE_URL, '/Archives/edgar/daily-index/')
    __FULL_INDEX_URL = "{0}/{1}".format(__BASE_URL, '/Archives/edgar/full-index/')


    @staticmethod
    def __get_response(url):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        response = http.request('GET', url)
        return response

    @staticmethod
    def list_by_date(date):
        """
        Gets a list of records for the specified date

        Index files are available in json, xml
        :param date:
        :return: filings:list - List of Filings found on that date
        """
        annual_quarter = "QTR{0}".format(floor(date.month / 3))
        index_file = "index.json"
        url = "{0}/{1}/{2}/{3}".format(EDGAR.__FULL_INDEX_URL,date.year,annual_quarter, index_file)
        response = EDGAR.__get_response(url)
        json_response = json.loads(response.data)
        return json_response

    @staticmethod
    def get_by_accession_number(accession_number):
        """

        :param accesion_number: Accession
        :return: list of all contents in that directory
        """

        accession_directory_url = "{0}/{1}".format(EDGAR.__BASE_URL, accession_number)

        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        response = http.request('GET', accession_directory_url)



        print(response)


