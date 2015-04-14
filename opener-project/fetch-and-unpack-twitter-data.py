import requests
import shutil
import os.path
from glob import glob
from tempfile import NamedTemporaryFile

DATA_URL = 'http://stash.compjour.org/data/sunlight-twitter-opener.zip'
DATA_DIR = 'data-hold'

print("Downloading", DATA_URL)
r = requests.get(DATA_URL)

tzip = NamedTemporaryFile(delete = False)
tzip.write(r.content)
tzip.close()
print("Unzipping to", DATA_DIR)
shutil.unpack_archive(tzip.name, DATA_DIR, format = 'zip')
os.remove(tzip.name) # again, thanks a lot Windows
csvname = os.path.join(DATA_DIR, 'sunlight_legislators.csv')
print(csvname, 'has', os.path.getsize(csvname), 'bytes')
print("Tweet files:", len(glob('data-hold/tweets/*.json')))
print("Profile files:", len(glob('data-hold/profiles/*.json')))