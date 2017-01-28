#!/usr/bin/python3

#
# The command line entry point
#

import sys
import argparse
from datetime import datetime

from sql import venue

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="optional fetch query string", action='store_true')
args = parser.parse_args()

def load_venues():
    if (not args.quiet):
        print('executing load_venues ...')
    venues = venue.fetch()
#   get venues list from mariaDB
#   log success/failure
#   sys.exit(1) exit failure if no venues
    return venues

#   get venue.datasource.type
#   can be html or api
def get_datasource(venue):
    if (not args.quiet):
        print('executing get_datasource ...')
#   return new HtmlAdapter(venue.datasource)
#   return new ApiAdapter(venue.datasource)

def fetch_data(adapter):
    if (not args.quiet):
        print('executing fetch_data ...')
#   adapter.configure()
#   data = adapter.fetch()
#   log success/failure
#   return data

def transform_data(data):
    if (not args.quiet):
        print('executing transform_data ...')
#   transform data from parsed data into elasticsearch json
#   return transformed_data

def store_data(transformedData):
    if (not args.quiet):
        print('executing store_data ...')
#   store (bulk store in es)
#   log success/failure
#   sys.exit(1) exit failure if store fails

def run_command():
    venues = load_venues()
    for venue in venues:
        print(venue['parser'])
    # foreach venue
    #   get_datasource
    #   fetch_data(dataAdapter))
    #   transform_data(data)
    #   store_data(transformedData)
    sys.exit(0)

# kick it off ...
run_command()
