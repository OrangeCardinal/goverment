class IMF_DataStructure(object):
    def __init__(self, database_id, json_data):
        self.database_id        = database_id
        self.structure          = json_data['Structure']
        self.header             = self.structure['Header']
        self.contact_info       = {
            'telephone_number'  : self.header['Sender']['Contact']['Telephone']   ,
            'uri'               : self.header['Sender']['Contact']['URI']
        }

        # Parse out data from the CodeLists section of the document
        raw_code_list           = self.structure['CodeLists']['CodeList'][0]['Code']
        self.codes              = {}
        for code in raw_code_list:
            key = code['@value']
            val = code['Description']['#text']
            self.codes[key] = val



    def __str__(self):
        """
        Human readable representation of the data
        :return: Well Formatted Text Representation of this object
        """
        #print(self.structure.keys())
        #print(self.header.keys())
        desc  = "\nIMF Data Structure\n"
        desc += "------------------\n"
        desc += "Database ID: {0}\n".format(self.database_id)
        desc += "Contact URI: {0}\n".format(self.contact_info['uri'])
        desc += "Contact Telephone: {0}\n".format(self.contact_info['telephone_number'])
        return desc