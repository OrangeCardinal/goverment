import json
import os
from government.base.api import API
from government.usa.foia.agency_component import AgencyComponent

class FreedomOfInformationAct(API):
    """
    Wrapper for the API Endpoints

    References
    https://www.foia.gov/developer/agency-api/
    """

    def agency_components(self):
        """
        Gets a list of Agency Components
        :return:
        """

        api_key = os.environ['API_DATA_GOV_KEY']


        # Make the API Call parse the json data received
        url = "https://api.foia.gov/api/agency_components?api_key={0}".format(api_key)
        response = self.get_response(url)
        json_response = json.loads(response.data)

        # Format the data as warranted
        processed_data = []
        for agency_component in json_response['data']:
            processed_data.append(AgencyComponent(agency_component))

        return processed_data

    def download_data_set(self, year):
        """
        Downloads a compressed archive of xml data into the requested for a given year if available

        :param year: Year to get data set for
        :return: Path to Zip File | None
        """
        zipname  = "{0}-FOIASetFull.zip".format(year)
        filename = "{0}\{1}".format(os.environ['GOVERNMENT_DATA_DOWNLOAD_DIRECTORY'],zipname)
        url = "https://www.foia.gov/{0}".format(zipname)
        self.get_file(url, filename)
        print(filename)
        return filename



    def request_form(self, agency_id):
        api_key = os.environ['API_DATA_GOV_KEY']
        url = "https://api.foia.gov/api/agency_components/{0}/request_form?api_key={1}".format(agency_id, api_key)
        print(url)
        response = self.get_response(url)
        json_response = json.loads(response.data)
        print(json_response)



