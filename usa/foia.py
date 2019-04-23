from base.api import API
class FreedomOfInformationAct(API):
    """
    Wrapper for the API Endpoints
    """


    def agency_components(self):
        url = "https://api.foia.gov/api/agency_components"
        response = self.get_response(url)
        print(response.data)
