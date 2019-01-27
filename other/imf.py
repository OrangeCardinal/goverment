from base.api import API
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
        print(response.data)

    def compact_data(self, database_id):
        url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/{0}/".format(database_id)
        response = super().get_response(url)
        print(response.data)

    def metadata_structure(self, database_id):
        url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/MetadataStructure/{0}".format(database_id)
        response = super().get_response(url)
        print(response.data)

    def generic_metadata(self, database_id):
        url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/GenericMetadata/{0}/".format(database_id)
        response = super().get_response(url)
        print(response.data)

    def code_list(self, database_id, code):
        url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CodeList/{0}_{1}".format(code, database_id)
        response = super().get_response(url)
        print(response.data)

