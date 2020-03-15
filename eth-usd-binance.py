#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/bin/python
#
# <bitbar.title>ETH-USD Tracker</bitbar.title>
# <bitbar.version>v2.0</bitbar.version>
# <bitbar.desc>It tracks ETH-USD prices</bitbar.desc>
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

url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
r = requests.get(url)
j = r.json()

url24 = 'https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT'
r24 = requests.get(url24)
j24 = r24.json()

price = float(j["price"])

price = "%.2f" % price

ud = ""

udp = float(j24["priceChangePercent"])

if udp > 0:
  ud = u"\u001b[32m" + u"\u2191" + str(round(udp, 1)) + "%"
elif udp < 0:
  ud = u"\u001b[31m" + u"\u2193" + str(round(udp, 1) * -1) + "%"
else:
  ud =  + u"0%"

print(str(price) + "  " + ud + u"\u001b[0m" + u"  \uFF5C" + " | image=iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAMAAADzapwJAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABX1BMVEUAAABifupif+xjf+xjfutjf+pifulif+tifupifupifupifupifupifupifupifupifupifupifupifupifupifuphfupjf+pqhOtgfOqFmu+uvfRog+vN1vjZ3/qKn+9hfeqdr/L7/P+zwfVyi+x2ju3k6fv////X3vrBzPecrvJkgOq6xvbY3/rAy/e9yfZ/lu6LoO/19/78/P/P2Pm/yvfDzvesu/RqhetshuvV3fn8/f/o7PzS2vmgsfKYq/Gxv/WRpfCer/Lj6PvO1vnCzfeYqvGEm+6VqPGis/Nxi+yEmu+uvPSAl+6BmO54ke2Bl+6OovC1wvWZq/F5ku1xiux+le5wiezG0Pe4xfaIne+crfKPo/Bwiux7k+2isvODme7u8f3m6vyktPN8lO6WqfG7x/amtvP9/f90jOxmgevCzPe9yPaFm+91jezf5fva4Pq2w/Vrhutkf+prheuAuKdCAAAAFXRSTlMAAAAAAAAAACx9xOz8GILf/jLCM9S1uHP/AAAAAWJLR0QnLQ+oIwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAAd0SU1FB+QDDRENFqhVU2IAAAE+SURBVBjTbZFXV8JAEIV3RTA9gbBBNGCsEZGIBQVREDVYUYO9997L/z8mswRfzMNm5zv3zOzcixDCGLcwLMcLAs+xTMAtEQIqSrJCCNEIUWRJBO4e4Qjxvlg7/CKqxzFWo1DGOzp1uERVD4tUq+mJZJdB9SJGAYlQcXdPsrePcqkVMTLcjP4BczA1lIZCZhCr0HnDppmxRrIgV1jE0RajY+b4RG5yKg+cQzy0KEwXZ2ZL5blcBVQ8EgDPLyzaVjW7tLyy6skFisnaumWnyrWN7GaeAIYmZMup1O3t2s7uXoE2gZHG/sHh0fHJ6dm5E6Mj6QPjF5dX1ze3d/e6Rh/or1N6KCZS9UejsY6//NOzmXl5bSwfbFplvL1/VNNNq1y7G8Y6n18gjobBbz+G7x8/hhD+L7SQH2bbX8RBiPIXUeA15DleXGgAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjAtMDMtMTNUMTc6MTI6NDgrMDA6MDCTBjekAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIwLTAzLTEzVDE3OjEyOjQ4KzAwOjAw4luPGAAAAABJRU5ErkJggg==")
