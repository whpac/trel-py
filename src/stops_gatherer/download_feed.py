import urllib.request

url = 'https://www.ztm.poznan.pl/pl/dla-deweloperow/getGtfsRtFile?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ0ZXN0Mi56dG0ucG96bmFuLnBsIiwiY29kZSI6MSwibG9naW4iOiJtaFRvcm8iLCJ0aW1lc3RhbXAiOjE1MTM5NDQ4MTJ9.ND6_VN06FZxRfgVylJghAoKp4zZv6_yZVBu_1-yahlo&file=vehicle_positions.pb'

def downloadGtfsRtFeed():
    with urllib.request.urlopen(url) as f:
        data = f.read()
        return data