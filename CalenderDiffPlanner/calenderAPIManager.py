
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
import urllib2


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = '../res/client_secret.json'
APPLICATION_NAME = 'DiffPlanner'

CALENDAR_NAME = 'Diff Planner'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def buildCalendarRequest():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    return discovery.build('calendar', 'v3', http=http)

def checkForCalendar(service, calendarName):
    """ Checks to see if a calender by a certain name exists.
    
        Returns:    The ID of the queried calender.
    """
    while True:

      calendar_list = service.calendarList().list(pageToken=None).execute()

      for calendar_list_entry in calendar_list['items']:
        if calendar_list_entry['summary'] == calendarName:
            print('Adding events to ' + calendarName)
            return calendar_list_entry['id']
      page_token = calendar_list.get('nextPageToken')
      if not page_token: # Run untill the last calender
        break
    return 
    

def createCalendar(service):
    """ Creates a google calender, if the calender doesn't exist.

        Returns:    The ID of the created calender.
    """

    calendar = {
    'summary': CALENDAR_NAME,
    'timeZone': 'America/Los_Angeles'
    }
    created_calendar = service.calendars().insert(body=calendar).execute()
    print('Created new ' + created_calendar['summary'] + ' calender')
    return created_calendar['id']


def getCalender(service):
    """ Returns the calenter ID of interested based on the CALENDAR_NAME glob val.
    """
    calID = checkForCalendar(service, CALENDAR_NAME)
    if not calID:
        calID = createCalendar(service)
    return calID


def addEvent(service, summary, description, start, end, calID):
    """ Adds an event. 
    """

    event = {
        'summary': summary,
        'description': description,
        'start': {'dateTime': start},
        'end': {'dateTime': end},
        'reminders':{
            'useDefault': True
        }
    }

    event = service.events().insert(calendarId=calID, body=event).execute()
    return



def main():
    """Shows basic usage of the Google Calendar API.

    """
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        flags, extras = parser.parse_known_args(None)
    except ImportError:
        flags = None


    if not checkConnection():
        raise Exception("Not connected to the internet dummy!")

    service = buildCalendarRequest()
    calID = getCalender(service)

    addEvent(service, 
        'Test Event',
        '2016-10-11T14:00:00-07:00',
        '2016-10-11T15:00:00-07:00',
        calID)




if __name__ == '__main__':

    main()
