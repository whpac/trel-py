from datetime import datetime
from io import BytesIO
import re
import urllib.request

index_url = 'https://www.ztm.poznan.pl/pl/dla-deweloperow/gtfsFiles'
url = 'https://www.ztm.poznan.pl/pl/dla-deweloperow/getGTFSFile?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ0ZXN0Mi56dG0ucG96bmFuLnBsIiwiY29kZSI6MSwibG9naW4iOiJtaFRvcm8iLCJ0aW1lc3RhbXAiOjE1MTM5NDQ4MTJ9.ND6_VN06FZxRfgVylJghAoKp4zZv6_yZVBu_1-yahlo&file='

# feed_date: string (YYYY-MM-DD)
# returns: io.BytesIO
def downloadGtfsFeed(feed_date):
    feed_date = datetime.strptime(feed_date, '%Y-%m-%d')
    gtfs_file = ''
    with urllib.request.urlopen(index_url) as r:
        data = r.read().decode('utf-8')
        matches = re.findall(r'<td>((\d{8})_\d{8}\.zip)</td>', data)
        for match in matches:
            row_date = datetime.strptime(match[1], '%Y%m%d')
            if feed_date >= row_date:
                gtfs_file = match[0]
                break
    
    with urllib.request.urlopen(url + gtfs_file) as f:
        data = f.read()
        return BytesIO(data)