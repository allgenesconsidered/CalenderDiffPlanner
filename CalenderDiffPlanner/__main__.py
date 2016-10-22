#!/usr/bin/env
from __future__ import print_function
import httplib2
import os, argparse, re, urllib2
from datetime import date, datetime, time


import generateSchedule



def getArgs():
	""" Gets the arguments from the command line and returns the parser object 
		for deparsing. Arguments must include:
			* Title of diff. Multi worded titles must be wrapped in quotes.
			* Diff protocol number.
		Can also include:
			* Time of CHIR Addition.
			* Day 0 date.
	"""
	now = datetime.now()

	parser = argparse.ArgumentParser(description='Generates calender events \
		coorisponding with a cardiac diff.')
	parser.add_argument('name', help='Name of diff.')
	parser.add_argument('protocol', help='Protocol version (1.0, 1.2, 1.4).', default=str(1.0))
	parser.add_argument('-d','--date', help='Day 0 of Diff in \'YYYY-MM-DD\' format. \
		Defaults to today.', default=str(now)[:10])
	parser.add_argument('-t','--time', help='Time CHIR was added in \'HH:MH\' format. \
		Defaults to now.', default=str(now)[11:16])
	return parser.parse_args()

def checkConnection():
    """ Pings google to see if you are connected to the internet. 

        Returns True if the google.com server responds.
    """
    try:
        response=urllib2.urlopen('http://216.58.192.142', timeout=3) # google.com, 3 sec
        return True
    except urllib2.URLError as err:
    	raise Exception("Not connected to the internet dummy!")


def identifyTime(time):
	"""	Allows the user to input either a 12-hour or 24-hour formated time.
		Input: The time, either as a 24-hour HH:MM format or as a 
		12-hour HH:MM:_M foramt.
		Output: The time in 24-hour format.
	"""
	try:
		try:
			hour, minute, meridien = time.split(':')
		except:
			hour, minute= time.split(':')
			meridien = None
	except:
		raise IOError('Incorect time format: ' + time)

	if int(minute) > 59:
		raise Exception('Minute out of bounds: ' + time)

	if meridien:
		return twelveHourCheck(hour, minute, meridien)
	else:
		return twentyFourHourCheck(hour, minute)


def twelveHourCheck(hour, minute, meridien):
	"""	Runs checks based on a 12-hour format. 
	"""
	if int(hour) > 12:
		raise IOError('12-hour clock our ot bounds: ' + hour)

	if meridien.upper() == 'AM':
		return ':'.join((hour,minute))
	elif meridien.upper() == 'PM':
		return ':'.join((str(int(hour) + 12),minute))
	else:
		raise IOError('Incorect AM/PM format: ' + meridien)


def twentyFourHourCheck(hour, minute):
	""" Runs checks based on 24-hour time format.
	"""
	if int(hour) > 24:
		raise Exception('Hour out of bounds: ' + hour)
	return ':'.join((hour,minute))



def convertToDateTime(date, time):
	""" Converts all inputs of the -d and -t format to a datetime object.
		Input: Only the date and time.
		Output: A datetime object.
	"""
	time = identifyTime(time)
	year, month, day = date.split('-')
	hour, minute = time.split(':')
	return datetime(int(year), int(month), int(day),
		int(hour), int(minute))


def main():
	if checkConnection():
		args = getArgs()
		t = convertToDateTime(args.date, args.time)
		generateSchedule.runScheduler(args.name, args.protocol, t)




if __name__ == '__main__':
	main()

	