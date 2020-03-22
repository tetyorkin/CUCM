from os.path import abspath
from urllib.parse import urljoin
from urllib.request import pathname2url
import ssl
from suds.client import Client
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


WSDL = urljoin('file:', pathname2url(abspath('schema/AXLAPI.wsdl')))
URL = 'https://cucm_ip:8443/axl'
USERNAME = 'admin'
PASSWORD = ''

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

CLIENT = Client(WSDL, location=URL, username=USERNAME, password=PASSWORD)


# pattern - number, shareLineAppearanceCssName - using CSS
response = CLIENT.service.listLine(
                {
                    'pattern': '%'}, returnedTags={
                    'pattern': '', 'description': '', 'usage': '', 'shareLineAppearanceCssName': '%'
                })
# print(response)


with open('cucm_dn.txt', 'w', encoding='utf-8') as file:
    file.write(str(response))
print('Done')