from government.usa.foia.foia import FreedomOfInformationAct

foia = FreedomOfInformationAct()

#
dataset = foia.download_data_set(2016)


exit()

# Display All the Federal Agencies that are available via this API currently
for ac in foia.agency_components():
    print(ac)


# This sample shows how to get all the various agency components, and then how to get each agencies
# request form
foia = FreedomOfInformationAct()
for ac in foia.agency_components():
    ac_request_form = foia.request_form(ac.id)



