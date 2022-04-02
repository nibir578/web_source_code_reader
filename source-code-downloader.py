import urllib.request as U
import pyfiglet
from termcolor import *
banar=colored(pyfiglet.figlet_format("Web_Source_Code_Reader"),'green')
print(banar)
print(colored("                                                                                    Created_by_King37         ",'red'))
website_url=input("Enter Your Website Name : ")
source =U.urlopen(website_url)
source_read=source.read()
print(source_read)