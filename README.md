# CalenderDiffPlanner

## Dependancies ##
  > Python 2.7._
  
  > Google Client Library
  
  > A Google gmail account
  
## Setup ##
Alot of the setup has bee adapted from the Google Quickstart Guide.

1. Verify installing python by opening up terminal and typing the following. Make sure the version is 2.7._:
```bash
$ python
Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
``` 
2. [Go to this website](https://labs.gladstone.org/conklin/pages/genomic-sequence-data-and-rna-sequence-ips-cells) to install your API client.
  1. On the website, click Continue, then Go to credentials.
  2. On the **Add credentials to your project** page, click the **Cancel** button.
  3. At the top of the page, select the **OAuth consent screen** tab. Select an *Email address*, enter a **Product name** if not already set, and click the **Save** button.
  4. Select the **Credentials** tab, click the **Create credentials** button and select **OAuth client ID**.
  5. Select the application type **Other**, enter the name "Google Calendar API Quickstart", and click the **Create** button.
  6. Click **OK** to dismiss the resulting dialog.
  7. Click the down arrow to download the JSON file of the client ID.
  8. Move this file to your working directory (the files you downloaded from here) and rename it *client_secret.json*. 
  
3. Run the following command to install the Google Client library using pip:
```bash
$ pip install --upgrade google-api-python-client
``` 

## Running the script

To run the script you need to specify:

 * The name of the Diff. Surround in qoutes. 
 
 * The version of the protocol you're using.
 
  - 1.0
  - 1.2
  - 1.4
  
  
You can also add the time and date of the diff. If left blank, the time and date are set to now:

  * -d for adding the date in YYYY-MM-DD format.
  
  * -t for adding the time in HH:MM format for 24-hour or HH:MM:_M for 12-hour format
 

Here's an example of running the script for a diff called "BAG3 Het KO", with protocol 1.0, at 9:35 AM starting today:
 ```bash
$ python diffPlanner.py "BAG3 Het KO" 1.0 -t 9:35 
Initiating API request
Adding events to Diff Planner
Making the magic happen
Diff schedule generated sucessfully!
``` 
Check your google calender to make sure everything worked well.
