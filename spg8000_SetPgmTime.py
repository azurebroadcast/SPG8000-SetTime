import requests
from requests.auth import HTTPDigestAuth
from datetime import datetime
import time
import os
from sys import platform

# Sync Gen IP and Credentials
ip = '10.4.50.51'
username = 'admin'
password = 'admin'

# Wait until host and sync gen can talk
while True:
    if platform == 'win32': # Use '-n' flag for windows
        icmp = os.system(f"ping -n 1 {ip}")
    else:
        icmp = os.system(f"ping -c 1 {ip}") # Use '-c' flag for everyone else
    if icmp == 0:
        print(f'\n{ip} Online.')
        break
    else:
        print(f'{ip} Offline. Waiting for device...')
        time.sleep(5)

print('\nWaiting 10 seconds to send time data.')
time.sleep(10)

#Get time from local host
now = datetime.now()
hour = now.strftime('%H')
minute = now.strftime('%M')
second = now.strftime('%S')
print(f'\nSetting Program Time to {hour}:{minute}:{second}')

# Log Into Sync Gen 
try:
    url = f'http://{ip}/admin/'
    auth = requests.get(url, auth=HTTPDigestAuth(username, password))
    print(f'{ip}: Login Successful.')

except:
    print(f'{ip}: Login Failed.')

# Set Program Time
try:
    url = f'http://{ip}/cgi-bin/scpi?1+SOUR%3ATIMES%3APCOU%3ATIME%3AINIT%20{hour}%2C{minute}%2C{second}'
    response = requests.post(url)
    print(response)
except:
    print(f'{ip}: Failed to set program time.')

# Set LTC2 Output to Program Time
try:
    url = f'http://{ip}/cgi-bin/scpi?1+OUTP4%3ALTC2%3ASOUR%20PCOU'
    response = requests.post(url)
    print(response)
except:
    print(f'{ip}: Failed to set LTC Output to Program Time.')

# Set LTC3 Output to Program Time
try:
    url = f'http://{ip}/cgi-bin/scpi?1+OUTP4%3ALTC3%3ASOUR%20PCOU'
    response = requests.post(url)
    print(response)
except:
    print(f'{ip}: Failed to set LTC Output to Program Time.')

# Set LTC4 Output to Program Time
try:
    url = f'http://{ip}/cgi-bin/scpi?1+OUTP4%3ALTC4%3ASOUR%20PCOU'
    response = requests.post(url)
    print(response)
except:
    print(f'{ip}: Failed to set LTC Output to Program Time.')