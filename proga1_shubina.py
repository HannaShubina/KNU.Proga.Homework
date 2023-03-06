from urllib.request import urlopen, Request
from datetime import datetime
import re

url = "https://godinnik.com/time/%D0%BA%D0%B8%D1%97%D0%B2/"
request = Request(url, headers={"user-agent": "True"})
response = urlopen(request)
info = response.info()
html = str(response.read(), encoding=info.get_content_charset())

def find_time(): #function for times comparison
    time_now = datetime.now()
    ct = time_now.strftime("%H:%M:%S") #current time
    site_time = re.findall(r"\d\d\:\d\d\:\d\d", html)
    print("Time from site:", site_time[0])
    print("Yours local time:", ct)
    if site_time[0] == ct:
        print("Time is equal")
    else:
        print("Time is not equal")

find_time()