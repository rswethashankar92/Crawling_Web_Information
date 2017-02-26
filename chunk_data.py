import os
import sys
import lxml
from bs4 import BeautifulSoup
from six.moves import urllib

# To Change the directory
os.chdir('C:\\Users\\Swetha\\Desktop\\Python_Source_Codes')

# Website to Scrap the data
thisurl = 'http://www.mapsofindia.com/pincode/india/tamil-nadu/chennai/'

def GetURL(url):
    try:
        html_request = urllib.request.urlopen(url).read()
        return html_request
    except HTTPError:
        print("URL Open Error")

def get_parser_data(html_req):
    try:
        fp = BeautifulSoup(html_req,'lxml')
        return fp
    except ValueError:
        print("Parsing Error")

def parse_table_data(table):
    table_data = table.findAll("div",{"class":"table_hide"})
    for tag_data in  table_data:
        return (tag_data.prettify('utf-8'))
        
html =GetURL(thisurl)
data = get_parser_data(html)
html_tag_data = parse_table_data(data)

# Open a file and write the web scraped html tag information
    
filename = None
try:
    filename = open("chunk_file.html",'wb')
except IOError:
    print("File Open Error")
finally:
    filename.write(html_tag_data)
    filename.close()


