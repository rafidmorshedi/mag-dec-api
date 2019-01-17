import requests
import time
from bs4 import BeautifulSoup
import re

def decdeg2dms(dd):
    negative = dd < 0
    dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60)
    degrees,minutes = divmod(minutes,60)
    if negative:
        if degrees > 0:
            degrees = -degrees
        elif minutes > 0:
            minutes = -minutes
        else:
            seconds = -seconds
    return (degrees,minutes,seconds)

def get_mag_var(lat, lon, year, month, day, elev=0):
    """Returns the magnetic variation at a particulat point on earth.

    Keyword Arguments
    lat -- latitude (e.g. -180.6 deg)
    lon -- longitude (e.g. -34.6 deg)
    elev -- elevation in km (default 0.0)
    year -- year (e.g. 2015)
    month -- month (e.g. 11)
    day -- day (e.g. 30)

    Returns
    float -- magnetic variation
    """
    (latd, latm, lats) = decdeg2dms(lat)
    (lond, lonm, lons) = decdeg2dms(lon)

    payload = {'latd': latd,'latm':latm,'lats':lats,'lond':lond,'lonm':lonm,
    'lons':lons,'elev':elev,'year':year,'month':month,'day':day,'Ein':'D'}
    url = 'http://www.ga.gov.au/oracle/cgi/geoAGRF.sh'

    # Sleep to avoid spamming server
    time.sleep(1)

    r = requests.get(url, params=payload)
    if r.status_code == 200:
        c = r.content
        soup = BeautifulSoup(c,'html.parser')
        deg_text = soup.find_all('b')[-1].text.strip()
        # strip out the junk so we have a number
        deg = re.search(r'D  =    (.*?) deg', deg_text).group(1)
        deg = float(deg)
        return deg
    else:
        return 'something went wrong'