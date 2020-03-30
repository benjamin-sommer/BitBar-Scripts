#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/bin/python
#
# <bitbar.title>Coronavirus Tracker</bitbar.title>
# <bitbar.version>v2.0</bitbar.version>
# <bitbar.desc>It tracks Coronavirus cases</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
#
# by BenSommer

try:
  import requests
except ImportError:
  print("Need to install requests module")
  print("Type the following:")
  print("pip install requests")

import json

url = 'https://coronavirus-19-api.herokuapp.com/countries'
r = requests.get(url)
j = r.json()

uk = {}

for x in j:
  if x["country"] == "UK":
    uk = x

pic = int(round(float(uk["todayCases"]) / (float(uk["cases"]) - float(uk["todayCases"])) * 100))
pid = int(round(float(uk["todayDeaths"]) / (float(uk["deaths"]) - float(uk["todayDeaths"])) * 100))

print("Cases: " + str(uk["cases"]) + " (" + u"\u001b[32m" + u"\u2191" + str(pic) + "%" + u"\u001b[0m" + ")" + "  Deaths: " + str(uk["deaths"]) + " (" + u"\u001b[32m" + u"\u2191" + str(pid) + "%" + u"\u001b[0m" + ")" + " | image=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")
