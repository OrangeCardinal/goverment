from    government.base.api             import API
from    government.usa.census.constants import *
from    lxml                            import html as lxml_html
import  html
import  re


class Geocoder(API):
    """
    Encapsulates the US Census Bureau Department'S Geo Encoding Service


    Responsibilities
    Converts addresses into longitude and latitude values
    Converts longitude and latitude values into addresses

    Relevant Links
    https://www.census.gov/data/developers/data-sets/Geocoding-services.html
    """

    BASE_URL = "https://geocoding.geo.census.gov/geocoder/locations"

    def get_locations_by_one_line_address(self,address):
        search_type =SearchType.ONE_LINE_ADDRESS.value
        url = "https://geocoding.geo.census.gov/geocoder/locations/{0}?{1}".format(search_type, address)
        response = self.get_response(url)
        print(response.data)


    def get_locations_by_address(self, street, city, state, zip, benchmark=Benchmark.CURRENT.value):
        """
        Given a physical address, gets the coordinates, any matched address, and address components accordingly

        :param street: Number and street name
        :param city: City name
        :param state: State
        :param zip: Zip code
        :param benchmark: Benchmark to use. Valid values found in the Benchmark enum.
        :returns: coordinates, matched_address, address_components
        """
        # Make the html request and get the response
        #TODO: Fix the html escape stuff here, looks incorrect
        search_type = SearchType.ADDRESS.value
        url         = "{0}/{1}".format(self.BASE_URL, search_type)
        url        += "?street={0}&city={1}&state={2}&zip={3}&benchmark={4}".format(html.escape(street),
                                                                                    html.escape(city),
                                                                                    html.escape(state),
                                                                                    html.escape(str(zip)),
                                                                                    benchmark)
        response = self.get_response(url)

        # Assign default return values in the case no valid data is found
        matched_address     = None
        coordinates         = None
        address_components  = {}

        # Scrape the html results for data
        tree = lxml_html.fromstring(response.data)
        xpath = '//*[@id="pl_gov_census_geo_geocoder_domain_AddressResult"]/text()'
        results = tree.xpath(xpath)
        for data in results:
            if re.match('Matched Address', data):
                section         = 'matched_address'
                matched_address = data.split(':')[1]
            elif re.match('Coordinates:', data):
                parts       = data.split(':')
                longitude   = float(re.sub("[^0-9\.\-]", "", parts[2]))
                latitude    = float(parts[3])
                coordinates = (longitude, latitude)
            elif re.match('Address Components', data):
                section         = 'address_components'
            elif section == 'address_components':
                key, value              = data.split(':')
                key                     = re.sub(" ","_",key).lower()
                value                   = re.sub(" ","",value)
                address_components[key] = value

        return coordinates, matched_address, address_components