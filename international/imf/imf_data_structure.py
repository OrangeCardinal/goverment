class IMF_DataStructure(object):
    def __init__(self, database_id, json_data):
        self.database_id        = database_id
        self.structure          = json_data['Structure']

        # Parse out data from the Header section
        self.header             = self.structure['Header']
        self.contact_info       = {
            'telephone_number'  : self.header['Sender']['Contact']['Telephone']   ,
            'uri'               : self.header['Sender']['Contact']['URI']
        }
        self.available_frequencies  = {}
        self.geographical_areas     = {}
        self.indicators             = {}
        self.time_values            = {}

        #############################################################
        # Parse out data from the CodeLists section of the document #
        #############################################################
        raw_code_list           = self.structure['CodeLists']['CodeList'][0]['Code']
        self.codes              = {}
        for code in raw_code_list:
            key = code['@value']
            val = code['Description']['#text']
            self.codes[key] = val


        # Get Frequency Data
        for code in self.structure['CodeLists']['CodeList'][1]['Code']:
            key     = code['@value']
            value   = code['Description']['#text']
            self.available_frequencies[key] = value


        # Get Geographical Areas
        for code in self.structure['CodeLists']['CodeList'][2]['Code']:
            key     = code['@value']
            value   = code['Description']['#text']
            self.geographical_areas[key] = value


        # Get Indicators
        for code in self.structure['CodeLists']['CodeList'][3]['Code']:
            key     = code['@value']
            value   = code['Description']['#text']
            self.indicators[key] = value

        # Get Time Values
        for code in self.structure['CodeLists']['CodeList'][4]['Code']:
            key     = code['@value']
            value   = code['Description']['#text']
            self.time_values[key] = value

        #######################################################
        # Parse out any needed data from the Concepts section #
        #######################################################
        self.concept = self.structure['Concepts']['ConceptScheme']['Name']['#text']


        # Parse out any needed data from the KeyFamilies section
        #print(self.structure['KeyFamilies']['KeyFamily']['Components'])
        #print(self.structure['KeyFamilies']['KeyFamily']['Annotations'])
        raw_annotations = self.structure['KeyFamilies']['KeyFamily']['Annotations']['Annotation']
        self.annotations = {}
        for annotation in raw_annotations:
            key = annotation['AnnotationTitle']
            value = annotation['AnnotationText']['#text']
            self.annotations[key] = value
        #print(self.structure['KeyFamilies']['KeyFamily'].keys())

    def __str__(self):
        """
        Human readable representation of the data
        :return: Well Formatted Text Representation of this object
        """
        #print(self.structure.keys())
        #print(self.header.keys())
        desc  = "\n{0}\n".format(self.concept)
        desc += "{0:-<{width}}\n".format('-',width=len(self.concept))
        desc += "Database ID: {0}\n".format(self.database_id)
        desc += "Contact URI: {0}\n".format(self.contact_info['uri'])
        desc += "Contact Telephone: {0}\n".format(self.contact_info['telephone_number'])

        section_title = "Frequencies"
        desc += "\n{0}\n".format(section_title)
        for code, description in self.available_frequencies.items():
            desc += "{0}: {1}\n".format(code, description)

        section_title = "Annotations"
        desc += "\n{0}\n".format(section_title)
        for annotation, annotation_text in self.annotations.items():
            desc += "{0}: {1}\n".format(annotation, annotation_text)
        return desc