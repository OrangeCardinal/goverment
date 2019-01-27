from base.api import API
import json

class BureauOfLaborStatistics(API):
    API_VERSION = 2

    def all_surveys(self):
        url = "https://api.bls.gov/publicAPI/v2/surveys"
        response = super().get_response(url)
        print(response.data)

    def popular_time_series(self):
        url = "https://api.bls.gov/publicAPI/v2/timeseries/popular"
        response = super().get_response(url)
        json_response = json.loads(response.data)
        return json_response



    def time_series(self, time_series, latest=None):
        """

        :param time_series:
        :param latest:
        :return:
        """
        url = "https://api.bls.gov/publicAPI/v2/timeseries/data/{0}?".format(time_series)
        if latest:
            url += "latest={0}".format(latest)
        response = super().get_response(url)