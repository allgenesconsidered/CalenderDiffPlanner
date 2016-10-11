from __future__ import print_function
from datetime import datetime, timedelta

import calenderAPIManager as API



PROTOCOL_v1_0 = {
	0 : "12 uM CHIR in RPMI (-)Insulin",
	1 : "RPMI (-)Insulin Only",
	3 : "5 uM IWP2 in RPMI(-)",
	5 : "RPMI (-)Insulin Only",
	7 : "RPMI (+)Insulin",
	14: "Check for beating cells",
	15: "Replate cells",
	16: "RPMI (+)Insulin",
	20: "Lactate Treatment #1",
	22: "Lactate Treatment #2",
	24: "RPMI (+)Insulin"

}

PROTOCOL_v1_2 = {
	0 : "12 uM CHIR in RPMI (-)Insulin",
	1 : "RPMI (-)Insulin Only",
	3 : "5 uM IWP2 in RPMI(-)",
	5 : "RPMI (-)Insulin Only. Split cells.",
	10 : "RPMI (+)Insulin",
	14: "Check for beating cells",
	15: "Replate cells",
	16: "RPMI (+)Insulin",
	20: "Lactate Treatment #1",
	22: "Lactate Treatment #2",
	24: "RPMI (+)Insulin"

}

PROTOCOL_v1_4 = {
	0 : "6 uM CHIR in RPMI (-)Insulin",
	2 : "RPMI (-)Insulin Only",
	4 : "5 uM IWP2 in RPMI(-)",
	6 : "RPMI (-)Insulin Only",
	8 : "RPMI (+)Insulin",
	14: "Check for beating cells",
	15: "Replate cells",
	16: "RPMI (+)Insulin",
	20: "Lactate Treatment #1",
	22: "Lactate Treatment #2",
	24: "RPMI (+)Insulin"

}

MAP_PROTOCOL = {
	'1.0' : PROTOCOL_v1_0,
	'1.2' : PROTOCOL_v1_2,
	'1.4' : PROTOCOL_v1_4
}

def getProtocolSchedule(protocol):
	try:
		return MAP_PROTOCOL[protocol]
	except KeyError:
		print(protocol)
		raise Exception('Incorrect protocol.\
			The protocol should be either \'1.0\', \'1.2\', or \'1.4\'')
	return None


def runScheduler(title, protocol, dateTime):

	print("Initiating API request")

	service = API.buildCalendarRequest()
	calID = API.getCalender(service)
	protocolSchedule = getProtocolSchedule(protocol)

	print('Making the magic happen')

	for key in protocolSchedule.keys():

		eventStart = dateTime + timedelta(days=key)
		eventEnd = eventStart + timedelta(hours=1)

		name = title + ' : Day ' + str(key)

		description = protocolSchedule[key]

		API.addEvent(service, 
        name,
        description,
        str(eventStart.isoformat()) + '-07:00',
        str(eventEnd.isoformat()) + '-07:00',
        calID)

	print('Diff schedule generated sucessfully!')

	return

