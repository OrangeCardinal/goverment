class IMF_DataSet(object):
    def __init__(self, database_id, json_data):
        self.database_id = database_id
        self.time_series = {}
        raw_time_series = json_data['CompactData']['DataSet']['Series']['Obs']
        for observation in raw_time_series:
            key = observation['@TIME_PERIOD']
            val = observation['@OBS_VALUE']
            self.time_series[key] = val

    def __str__(self):
        desc =  "\nIMF Data Set\n"
        desc += "-----------\n"
        desc += "Database ID: {0}".format(self.database_id)

        return desc