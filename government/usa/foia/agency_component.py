class AgencyComponent(object):
    def __init__(self, data):
        self.data = data
        self.id = self.data['id']
        for name, val in self.data['attributes'].items():
            setattr(self, name, val)



    def __str__(self):
        readable_desc = "<AgencyComponent>\n"
        readable_desc += "{0}\n{1}\n".format(self.title,self.id)
        readable_desc += "Email: {0}\n".format(self.email)
        readable_desc += "Telephone: {0}\n".format(self.telephone)

        readable_desc += "Update Schedule\n"
        readable_desc += "Scheduled Transition Date: {0}\n".format(self.scheduled_transition_date)
        readable_desc += "Scheduled Publication: {0}\n".format(self.scheduled_publication)
        readable_desc += "Scheduled Moderation State: {0}\n".format(self.scheduled_moderation_state)

        readable_desc += "Reading Rooms\n"
        for room in self.reading_rooms:
            readable_desc += "{0}\n".format(room['uri'])

        return readable_desc