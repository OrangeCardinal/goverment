from government.base import API
from government.international.imf.imf_data_structure import IMF_DataStructure
from government.international.imf.imf_data_set import IMF_DataSet
import json

class IMF(API):
    """
    API for the International Monetary Fund
    """
    API_VERSION = 1

    def data_flow(self):
        url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/Dataflow/"
        response = super().get_response(url)
        print(response.data)

    def data_structure(self, database_id):
        url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/DataStructure/{0}".format(database_id)
        response = super().get_response(url)
        json_response = json.loads(response.data)
        data_structure = IMF_DataStructure(database_id, json_response)
        return data_structure


    def compact_data(self, database_id, start_period, end_period):
        """

        Related Information:

        :param database_id:
        :param start_period:
        :param end_period:
        :return: Time Series, or Error
        """
        # Generate the correct url to retrieve data from
        url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/{0}/".format(database_id)
        url += "M.GB.PMP_IX"        #TODO: Make this dynamic
        url += "?startPeriod={0}&endPeriod={1}".format(start_period, end_period)

        # Get the JSON response, parse it, and return the formatted object back
        response        = super().get_response(url)
        json_response   = json.loads(response.data)
        data_set        = IMF_DataSet(database_id, json_response)

        return data_set

    def metadata_structure(self, database_id):
        url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/MetadataStructure/{0}".format(database_id)
        response = super().get_response(url)
        json_response = json.loads(response.data)
        return json_response

    def generic_metadata(self, database_id):
        url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/GenericMetadata/{0}/".format(database_id)
        response = super().get_response(url)
        print(response.data)

    def code_list(self, database_id, code):
        url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CodeList/{0}_{1}".format(code, database_id)
        response = super().get_response(url)
        print(response.data)

