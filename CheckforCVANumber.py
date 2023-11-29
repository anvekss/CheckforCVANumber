import os ,sys
import shutil
import configparser
import time
from zipfile import ZipFile
import subprocess
import re
import urllib3
import requests 
from bs4 import BeautifulSoup

ArtifactoryLocation = os.getenv("ArtifactoryLocation")
buildinstalllocation = os.getenv("AdapterLocation")

def getCVAdapterVersion(buildinstalllocation):
    FilePath = os.path.join(buildinstalllocation ,'bin','olstat.exe')
    Cmd = FilePath + ' -I'
    proc = subprocess.Popen(Cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    buildetailedinfo = proc.stderr.read().decode("utf-8")
    buildinfo =re.findall("Build.*x86e_win64", buildetailedinfo)
    print(buildinfo)
    buildinfo = buildinfo[0].replace('Build' , "")
    buildinfo = buildinfo.replace('x86e_win64' , "")
    Build = re.findall("[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]", buildinfo )
    Build = Build[0].strip()
    print("CVA build is " , Build )
    return (Build)

def getzipurllocation(zipurl):
    http = urllib3.PoolManager()
    response = http.request('GET', zipurl)
    soup = BeautifulSoup(response.data,'html.parser')
    listzips = soup.find_all('a')
    tolalzipfiles = len(listzips)
    lastbuild = tolalzipfiles-1
    latestbuild = (listzips[lastbuild].string)
    finalurl = zipurl + '/' + latestbuild
    print("URL==" , finalurl)
    Build = re.findall("[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9].zip", finalurl )
    Build = Build[0].replace('.zip' , "")
    Build = Build.strip()
    print("Artifactory build is " , Build )
    return (Build)

InstalledBuild = getCVAdapterVersion(buildinstalllocation)
AtifactoryBuild = getzipurllocation(ArtifactoryLocation)

if (InstalledBuild == AtifactoryBuild ):
    print("Both the Build matches")
    exit(200)
else:
    print("Builds are different")
    exit(400)
   

