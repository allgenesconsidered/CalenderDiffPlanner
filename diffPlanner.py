from __future__ import print_function
import httplib2
import os
from datetime import date, datetime, time
import argparse

import generateSchedule



def getArgs():
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

def convertToDateTime(date, time):
	return datetime(int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2]),
		int(time.split(':')[0]), int(time.split(':')[1]))

if __name__ == '__main__':

	args = getArgs()
	t = convertToDateTime(args.date, args.time)
	generateSchedule.runScheduler(args.name, args.protocol, t)