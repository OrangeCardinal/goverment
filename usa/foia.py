import os
from base.api   import API

class FreedomOfInformationAct(API):
    """
    Wrapper for the API Endpoints
    """


    def agency_components(self):
        print(os.environ)
        return
        #api_key = os.environ['API_DATA_GOV_KEY']


        #url = "https://api.foia.gov/api/agency_components?api_key={0}".format(api_key)
        #response = self.get_response(url)
        #print(response.data)
