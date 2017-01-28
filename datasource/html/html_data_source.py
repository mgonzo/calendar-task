# list of urls
# need a class for each different calendar transformation
# run the fetch in a cron job once a day to start
# store in elasticsearch

from urllib.request import urlopen
from urllib import error
import http
from bs4 import BeautifulSoup
import re
from urllib import parse

class HtmlDataSource:
    def fetch():
        return data_as_rows
        end

    def fetch_html(url):
        print('Fetching '+ url)
        try:
            response = urlopen(url)

        except error.HTTPError as e:
            print('HTTPError = ' + str(e.code))
            return None

        except error.URLError as e:
            print('URLError = ' + str(e.reason))
            return None

        except http.client.HTTPException as e:
            print('HTTPException')
            return None

        except Exception as e:
            import traceback
            print('generic exception: ' + traceback.format_exc())
            return None

        return response.read()

    def getDataFromHtml(parser, html):
        end

    def parseData():
        end
