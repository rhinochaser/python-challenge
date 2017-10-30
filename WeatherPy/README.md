

```python
# Trend 1: The temperature tends to be higher for cities closer to the equator. Elevation of these cities needs to be considered.
# Trend 2: The avg wind speeds increase as cities are located further from the equator
# Trend 3: Average cloud coverage increases as cities  get further away from the equator
```


```python
#Dependencies
import csv
import matplotlib.pyplot as plt
import requests as req
import pandas as pd
import json
import random
from citipy import citipy
import os

```


```python
# configurations
api_key = "b8cdca3c02508276a3ae854132f5d6e1"
url = "http://api.openweathermap.org/data/2.5/weather?"
url
```




    'http://api.openweathermap.org/data/2.5/weather?'




```python
# partial query url:
query_url = url + "appid=" + api_key + "&units=imperial" + "&id="
```


```python
# Import citites list JSON from Open weather map
cities_file = open('city.list.json')
cities_json = json.load(cities_file)

```


```python
# cities variable to be used for manuipulations
cities = cities_json
```


```python
#test random search of small sample of cities
cities_random = random.sample(cities, 500)
#cities_random
```


```python
weather_data = []

for city in cities_random:
    # city id
    city_id = city.get("id")
    city_id = str(city_id)
    
    #city name
    city_name = city.get('name')
    
     
    # append weather_data list
    response = req.get(query_url + city_id).json()
    weather_data.append(response)
    
    requested_url = query_url + city_id
    
    #print log
    print('City Name: ' + city_name)
    print('City ID: ' + city_id)
    print('requested_url: ' + requested_url)
    print()
    
  
```

    City Name: Heintrop
    City ID: 3207366
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3207366
    
    City Name: Aspen Valley
    City ID: 5325059
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5325059
    
    City Name: Deliblato
    City ID: 836988
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=836988
    
    City Name: Dodworth
    City ID: 2651172
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2651172
    
    City Name: Scherpenheuvel-Zichem
    City ID: 2787061
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2787061
    
    City Name: Cullar-Vega
    City ID: 2518950
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2518950
    
    City Name: Viro Viro
    City ID: 3901409
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3901409
    
    City Name: Dale
    City ID: 5186244
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5186244
    
    City Name: Herleshausen
    City ID: 2906050
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2906050
    
    City Name: Huata
    City ID: 6621257
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6621257
    
    City Name: Tormestorp
    City ID: 2668180
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2668180
    
    City Name: Oberlin
    City ID: 5165445
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5165445
    
    City Name: Riedholz
    City ID: 7286906
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7286906
    
    City Name: Gornje Mostre
    City ID: 3200108
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3200108
    
    City Name: Borredon
    City ID: 3031507
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3031507
    
    City Name: Kowalewo
    City ID: 3094960
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3094960
    
    City Name: Rio Claro
    City ID: 3451232
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3451232
    
    City Name: Bang Pahan
    City ID: 1619371
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1619371
    
    City Name: Memerambi
    City ID: 2158135
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2158135
    
    City Name: Thurins
    City ID: 2972644
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2972644
    
    City Name: Mons
    City ID: 2993228
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2993228
    
    City Name: Virginia Valley
    City ID: 4568707
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4568707
    
    City Name: Santa Margarida
    City ID: 3450116
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3450116
    
    City Name: Sergey-Pole
    City ID: 805597
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=805597
    
    City Name: Hellstein
    City ID: 2906761
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2906761
    
    City Name: Caseres
    City ID: 3126024
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3126024
    
    City Name: Villebois-les-Pins
    City ID: 6612414
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6612414
    
    City Name: Werda
    City ID: 2810970
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2810970
    
    City Name: Namoluk
    City ID: 7627586
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7627586
    
    City Name: High Point
    City ID: 4158591
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4158591
    
    City Name: Wißmannsdorf
    City ID: 6554616
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6554616
    
    City Name: Paoli
    City ID: 5205037
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5205037
    
    City Name: Glantane
    City ID: 3292102
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3292102
    
    City Name: Couiza
    City ID: 3023294
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3023294
    
    City Name: Safonovskaya
    City ID: 499421
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=499421
    
    City Name: Ognes
    City ID: 6615673
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6615673
    
    City Name: Berridale
    City ID: 2176067
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2176067
    
    City Name: Karttula
    City ID: 653841
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=653841
    
    City Name: Khayredin
    City ID: 730425
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=730425
    
    City Name: La Plaine-des-Palmistes
    City ID: 935694
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=935694
    
    City Name: Lulindi
    City ID: 878184
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=878184
    
    City Name: Brüchermühle
    City ID: 2943623
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2943623
    
    City Name: Avoca
    City ID: 2962139
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2962139
    
    City Name: Jiefang
    City ID: 7735319
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7735319
    
    City Name: Cambridgeshire
    City ID: 2653940
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2653940
    
    City Name: Longjing
    City ID: 1914468
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1914468
    
    City Name: Alcantarilha
    City ID: 8012024
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=8012024
    
    City Name: Tarcento
    City ID: 6536694
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6536694
    
    City Name: La Loma
    City ID: 3707311
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3707311
    
    City Name: Longjie
    City ID: 1802578
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1802578
    
    City Name: Baden
    City ID: 5178806
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5178806
    
    City Name: Plaudren
    City ID: 6437330
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6437330
    
    City Name: Santa Cecília de Voltregà
    City ID: 6356264
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6356264
    
    City Name: Montehermoso
    City ID: 3116351
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3116351
    
    City Name: Brcko District of Bosnia and Herzegovina
    City ID: 3294903
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3294903
    
    City Name: Hardwick
    City ID: 2647492
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2647492
    
    City Name: Zaratamo
    City ID: 6362435
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6362435
    
    City Name: Medway
    City ID: 4971734
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4971734
    
    City Name: Fleac
    City ID: 3018354
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3018354
    
    City Name: Ellerbe
    City ID: 4465198
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4465198
    
    City Name: Celanova
    City ID: 6359842
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6359842
    
    City Name: Nine Mile
    City ID: 4924187
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4924187
    
    City Name: Landkreis Mecklenburg-Strelitz
    City ID: 3302144
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3302144
    
    City Name: Zavoronezhskoye
    City ID: 464094
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=464094
    
    City Name: Schochwitz
    City ID: 2837225
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2837225
    
    City Name: Binmaley
    City ID: 1724956
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1724956
    
    City Name: Air Force Academy
    City ID: 7260752
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7260752
    
    City Name: Landkreis Erding
    City ID: 2929716
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2929716
    
    City Name: Wulften
    City ID: 2805870
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2805870
    
    City Name: Talavera La Real
    City ID: 2510692
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2510692
    
    City Name: Sheridan
    City ID: 4911289
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4911289
    
    City Name: Savigny
    City ID: 2975553
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2975553
    
    City Name: Wyong Creek
    City ID: 2142741
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2142741
    
    City Name: Gau-Bischofsheim
    City ID: 6555271
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6555271
    
    City Name: Bei
    City ID: 7574369
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7574369
    
    City Name: Bregano
    City ID: 6535092
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6535092
    
    City Name: Rellingen
    City ID: 2848340
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2848340
    
    City Name: Tuckerton
    City ID: 4504525
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4504525
    
    City Name: Bertheauville
    City ID: 3033202
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3033202
    
    City Name: Kozova
    City ID: 704525
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=704525
    
    City Name: Brighouse
    City ID: 2654715
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2654715
    
    City Name: Pazuengos
    City ID: 3114158
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3114158
    
    City Name: Lollschied
    City ID: 2876018
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2876018
    
    City Name: Mekarsari
    City ID: 7579591
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7579591
    
    City Name: Sassari
    City ID: 6540111
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6540111
    
    City Name: Borovoy
    City ID: 572091
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=572091
    
    City Name: Barra do Trombudo
    City ID: 3470670
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3470670
    
    City Name: Lengthal
    City ID: 2878813
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2878813
    
    City Name: Possendorf
    City ID: 2852525
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2852525
    
    City Name: Encarnacion de Diaz
    City ID: 4006783
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4006783
    
    City Name: Loket
    City ID: 3071627
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3071627
    
    City Name: Hosakote
    City ID: 1269947
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1269947
    
    City Name: Molzino
    City ID: 525456
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=525456
    
    City Name: Castries
    City ID: 3576812
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3576812
    
    City Name: Garden Acres
    City ID: 5351496
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5351496
    
    City Name: Beverino
    City ID: 6534385
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6534385
    
    City Name: Saint-Aubin-de-Branne
    City ID: 6432370
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6432370
    
    City Name: Greece
    City ID: 5119251
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5119251
    
    City Name: Bletterans
    City ID: 3032251
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3032251
    
    City Name: Korgan
    City ID: 742658
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=742658
    
    City Name: Figueroles
    City ID: 3122445
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3122445
    
    City Name: Gelgaudiskis
    City ID: 599420
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=599420
    
    City Name: Anglesola
    City ID: 3130031
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3130031
    
    City Name: Province de Namur
    City ID: 2790469
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2790469
    
    City Name: Grube
    City ID: 2914642
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2914642
    
    City Name: Chhatapur
    City ID: 1274342
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1274342
    
    City Name: Chunskiy
    City ID: 1507636
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1507636
    
    City Name: Marlow
    City ID: 2873250
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2873250
    
    City Name: Sloboda
    City ID: 492015
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=492015
    
    City Name: Buchelay
    City ID: 3029684
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3029684
    
    City Name: Maennedorf / Ausserfeld
    City ID: 6293364
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6293364
    
    City Name: New Well
    City ID: 2064751
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2064751
    
    City Name: Gabrene
    City ID: 731564
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=731564
    
    City Name: Kauman
    City ID: 8185104
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=8185104
    
    City Name: Distrito do Porto
    City ID: 2735941
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2735941
    
    City Name: Reichersbeuern
    City ID: 6556129
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6556129
    
    City Name: Waller
    City ID: 5814941
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5814941
    
    City Name: Nomós Thessaloníkis
    City ID: 734075
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=734075
    
    City Name: Dataganj
    City ID: 1273409
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1273409
    
    City Name: Segura de Toro
    City ID: 3109239
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3109239
    
    City Name: Livingston
    City ID: 5367427
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5367427
    
    City Name: Punta Silum
    City ID: 1692400
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1692400
    
    City Name: Point Pleasant
    City ID: 5102796
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5102796
    
    City Name: Nidfurn
    City ID: 2659472
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2659472
    
    City Name: Zawiercie
    City ID: 7531906
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7531906
    
    City Name: Constantine
    City ID: 4989486
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4989486
    
    City Name: Kuryatnikovo
    City ID: 6654187
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6654187
    
    City Name: Rauchenwarth
    City ID: 2767878
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2767878
    
    City Name: Mühlbach am Hochkönig
    City ID: 7872227
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7872227
    
    City Name: Woolsthorpe
    City ID: 2142959
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2142959
    
    City Name: Trémery
    City ID: 6437897
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6437897
    
    City Name: Borough of Knowsley
    City ID: 3333162
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3333162
    
    City Name: Belle Vernon
    City ID: 5179794
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5179794
    
    City Name: Bogève
    City ID: 3032130
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3032130
    
    City Name: Emmaville
    City ID: 2167404
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2167404
    
    City Name: Aurières
    City ID: 3036019
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3036019
    
    City Name: Moià
    City ID: 6356167
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6356167
    
    City Name: eMbalenhle
    City ID: 1005646
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1005646
    
    City Name: Kham Khuean Kaeo
    City ID: 1610086
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1610086
    
    City Name: Ratoath
    City ID: 2961872
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2961872
    
    City Name: Ceara Mirim
    City ID: 3402360
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3402360
    
    City Name: Schöneweide
    City ID: 2836678
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2836678
    
    City Name: Lehesten
    City ID: 6550376
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6550376
    
    City Name: Nadigaon
    City ID: 1262291
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1262291
    
    City Name: Cintheaux
    City ID: 3024931
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3024931
    
    City Name: Carreira
    City ID: 2741399
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2741399
    
    City Name: Sant Iscle de Vallalta
    City ID: 3110925
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3110925
    
    City Name: Fennville
    City ID: 4992609
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4992609
    
    City Name: Karatu
    City ID: 158324
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=158324
    
    City Name: Hewlett
    City ID: 5120598
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5120598
    
    City Name: Grand Junction
    City ID: 5423573
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5423573
    
    City Name: Padada
    City ID: 1696780
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1696780
    
    City Name: Newburn
    City ID: 2641690
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2641690
    
    City Name: Armstrong Station
    City ID: 5887116
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5887116
    
    City Name: Moruga
    City ID: 3574087
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3574087
    
    City Name: Bang Na
    City ID: 1620755
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1620755
    
    City Name: Novyye Berëzki
    City ID: 517183
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=517183
    
    City Name: Lusk
    City ID: 2962769
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2962769
    
    City Name: Quanan
    City ID: 1917443
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1917443
    
    City Name: Novyy Karanlug
    City ID: 146969
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=146969
    
    City Name: Coincy
    City ID: 3024396
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3024396
    
    City Name: Salerno
    City ID: 6542117
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6542117
    
    City Name: Urana
    City ID: 7839777
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7839777
    
    City Name: Bugewitz
    City ID: 2942024
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2942024
    
    City Name: Sparta
    City ID: 4409615
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4409615
    
    City Name: Tuyen Quang
    City ID: 1563287
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1563287
    
    City Name: Eisenstadt
    City ID: 2780190
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2780190
    
    City Name: Saint-Angel
    City ID: 6617330
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6617330
    
    City Name: Yokohama
    City ID: 2127436
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2127436
    
    City Name: Cascada
    City ID: 3862372
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3862372
    
    City Name: Yahilnytsya
    City ID: 688602
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=688602
    
    City Name: Achmer
    City ID: 2959676
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2959676
    
    City Name: Siorac-en-Périgord
    City ID: 6429650
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6429650
    
    City Name: Kolbingen
    City ID: 6555847
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6555847
    
    City Name: Kafr Ayn
    City ID: 283379
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=283379
    
    City Name: Roa
    City ID: 3141671
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3141671
    
    City Name: Auleben
    City ID: 2954069
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2954069
    
    City Name: Chaumont-sur-Loire
    City ID: 3025876
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3025876
    
    City Name: Kotojedy
    City ID: 3073105
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3073105
    
    City Name: Welsford
    City ID: 6177995
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6177995
    
    City Name: Eibar
    City ID: 3123709
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3123709
    
    City Name: Foumbot
    City ID: 2231504
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2231504
    
    City Name: Langnau im Emmental
    City ID: 7286261
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7286261
    
    City Name: Cliffside Park
    City ID: 5096686
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5096686
    
    City Name: Bear River
    City ID: 5896216
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5896216
    
    City Name: Santutxu
    City ID: 6618856
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6618856
    
    City Name: T’aep’ong-dong
    City ID: 1930831
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1930831
    
    City Name: Zeneta
    City ID: 2509316
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2509316
    
    City Name: Weiswampach
    City ID: 6693302
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6693302
    
    City Name: Setubal
    City ID: 2262963
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2262963
    
    City Name: Partido de Navarro
    City ID: 3430454
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3430454
    
    City Name: Racines - Ratschings
    City ID: 6534784
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6534784
    
    City Name: Digor
    City ID: 748148
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=748148
    
    City Name: Altenberga
    City ID: 2957830
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2957830
    
    City Name: Valles de Palenzuela
    City ID: 3106535
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3106535
    
    City Name: Badi
    City ID: 6643968
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6643968
    
    City Name: Lauben
    City ID: 2880282
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2880282
    
    City Name: Villeneuve
    City ID: 2968605
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2968605
    
    City Name: Llinars del Valles
    City ID: 3118240
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3118240
    
    City Name: Brăneşti
    City ID: 618522
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=618522
    
    City Name: Mirow
    City ID: 764664
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=764664
    
    City Name: Minatomachi
    City ID: 1857089
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1857089
    
    City Name: Zhelezinka
    City ID: 1516634
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1516634
    
    City Name: Botro
    City ID: 2290985
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2290985
    
    City Name: Landivisiau
    City ID: 3007842
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3007842
    
    City Name: Baoluo
    City ID: 1894072
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1894072
    
    City Name: Cervo
    City ID: 3125287
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3125287
    
    City Name: Torrijos
    City ID: 6361833
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6361833
    
    City Name: Khutor Rodniki
    City ID: 549022
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=549022
    
    City Name: Quend
    City ID: 2984828
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2984828
    
    City Name: Ballou
    City ID: 5325943
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5325943
    
    City Name: Schwabsroth
    City ID: 2835469
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2835469
    
    City Name: Bilqas Qism Awwal
    City ID: 358821
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=358821
    
    City Name: Falkland Islands (Islas Malvinas)
    City ID: 3474414
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3474414
    
    City Name: Meinheim
    City ID: 2872231
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2872231
    
    City Name: Spindale
    City ID: 4492909
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4492909
    
    City Name: Dundalk
    City ID: 5943968
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5943968
    
    City Name: Witzeeze
    City ID: 6551516
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6551516
    
    City Name: Springerville
    City ID: 5315525
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5315525
    
    City Name: Faimes
    City ID: 2798512
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2798512
    
    City Name: Rock Falls
    City ID: 4907898
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4907898
    
    City Name: Wimmenau
    City ID: 2967349
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2967349
    
    City Name: Nagygajla
    City ID: 717357
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=717357
    
    City Name: Tottenham
    City ID: 2146193
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2146193
    
    City Name: Pioner
    City ID: 1494955
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1494955
    
    City Name: Rechkunovskiy
    City ID: 1493707
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1493707
    
    City Name: Itzlishofen
    City ID: 2895553
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2895553
    
    City Name: Friendship
    City ID: 4964943
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4964943
    
    City Name: Bustelo do Caima
    City ID: 2741916
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2741916
    
    City Name: Rogue River
    City ID: 5749213
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5749213
    
    City Name: Brenzone
    City ID: 6534598
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6534598
    
    City Name: Connells Point
    City ID: 2206004
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2206004
    
    City Name: Mshinskaya
    City ID: 525988
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=525988
    
    City Name: Dietersheim
    City ID: 2937124
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2937124
    
    City Name: Windesheim
    City ID: 2808219
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2808219
    
    City Name: Shchekutina
    City ID: 818493
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=818493
    
    City Name: Renfrew
    City ID: 6119448
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6119448
    
    City Name: Waldbrol
    City ID: 2815137
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2815137
    
    City Name: Gechuan
    City ID: 1921627
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1921627
    
    City Name: Welch
    City ID: 4826660
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4826660
    
    City Name: Black River
    City ID: 5246099
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5246099
    
    City Name: Mielec
    City ID: 7531899
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7531899
    
    City Name: Trujillo
    City ID: 2510145
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2510145
    
    City Name: Fulpmes
    City ID: 2779143
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2779143
    
    City Name: Leith-Hatfield
    City ID: 7258855
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7258855
    
    City Name: Chortov Most
    City ID: 805438
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=805438
    
    City Name: Barroca
    City ID: 8011687
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=8011687
    
    City Name: Harptree
    City ID: 5971207
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5971207
    
    City Name: Ordona
    City ID: 3171973
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3171973
    
    City Name: Pisang
    City ID: 7802063
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7802063
    
    City Name: Torre Annunziata
    City ID: 3165475
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3165475
    
    City Name: Paola
    City ID: 2562617
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2562617
    
    City Name: La Corey
    City ID: 6035779
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6035779
    
    City Name: Teosinte
    City ID: 3582981
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3582981
    
    City Name: Cavasso Nuovo
    City ID: 3179293
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3179293
    
    City Name: Gamlitz
    City ID: 7872400
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7872400
    
    City Name: East Harling
    City ID: 2650424
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2650424
    
    City Name: Saint Joseph
    City ID: 5008327
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5008327
    
    City Name: Przyborow
    City ID: 3087895
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3087895
    
    City Name: Gårde
    City ID: 2621605
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2621605
    
    City Name: Philippsburg
    City ID: 2853907
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2853907
    
    City Name: Canton de Luxembourg
    City ID: 2960315
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2960315
    
    City Name: West Little River
    City ID: 4177865
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4177865
    
    City Name: La Punt-Chamues-ch
    City ID: 7286266
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7286266
    
    City Name: Compiano
    City ID: 3178225
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3178225
    
    City Name: La Neuveville
    City ID: 7286256
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7286256
    
    City Name: Grand Falls-Windsor
    City ID: 5964378
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5964378
    
    City Name: Neuhaus
    City ID: 7871676
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7871676
    
    City Name: Cabrera de Mar
    City ID: 3127161
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3127161
    
    City Name: Erie County
    City ID: 5153362
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5153362
    
    City Name: Skwierzyna
    City ID: 3085656
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3085656
    
    City Name: Deutsch Jahrndorf
    City ID: 2781026
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2781026
    
    City Name: Villa Constitucion
    City ID: 3832778
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3832778
    
    City Name: Sebastianópolis do Sul
    City ID: 3447924
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3447924
    
    City Name: Pichoapan
    City ID: 3521576
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3521576
    
    City Name: Aves
    City ID: 2742577
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2742577
    
    City Name: Ganja City
    City ID: 828298
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=828298
    
    City Name: Kizema
    City ID: 547871
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=547871
    
    City Name: Laguna Salada
    City ID: 3502373
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3502373
    
    City Name: Corumbaíba
    City ID: 3465338
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3465338
    
    City Name: Manvi
    City ID: 1263594
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1263594
    
    City Name: Onzonilla
    City ID: 6358647
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6358647
    
    City Name: Lamothe-Montravel
    City ID: 6612361
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6612361
    
    City Name: Saint-Cannat
    City ID: 2981259
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2981259
    
    City Name: Kyotera
    City ID: 230256
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=230256
    
    City Name: Kars
    City ID: 743942
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=743942
    
    City Name: Benevides
    City ID: 3405792
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3405792
    
    City Name: Starachowice
    City ID: 7532300
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7532300
    
    City Name: Ampopohona
    City ID: 1077503
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1077503
    
    City Name: El Carrizo
    City ID: 4010589
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4010589
    
    City Name: Baláczaidűlő
    City ID: 3055603
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3055603
    
    City Name: Forni Avoltri
    City ID: 3176700
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3176700
    
    City Name: Tavernola Bergamasca
    City ID: 3165874
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3165874
    
    City Name: Zwethau
    City ID: 2803562
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2803562
    
    City Name: Mount Holly Springs
    City ID: 5202164
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5202164
    
    City Name: Nohn
    City ID: 2862292
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2862292
    
    City Name: Moisakula
    City ID: 590186
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=590186
    
    City Name: Beilstein
    City ID: 6553659
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6553659
    
    City Name: Dascalu
    City ID: 679708
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=679708
    
    City Name: Podstepki
    City ID: 507977
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=507977
    
    City Name: Evinayong
    City ID: 2308994
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2308994
    
    City Name: East Brookfield
    City ID: 4935347
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4935347
    
    City Name: Chynov
    City ID: 3077457
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3077457
    
    City Name: Motzorongo
    City ID: 3522923
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3522923
    
    City Name: Diffa
    City ID: 2445702
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2445702
    
    City Name: La Rosita
    City ID: 3636395
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3636395
    
    City Name: Yangzi
    City ID: 1787208
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1787208
    
    City Name: Llanwenog
    City ID: 2643917
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2643917
    
    City Name: Oristano
    City ID: 6540123
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6540123
    
    City Name: Lovely Banks
    City ID: 2159497
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2159497
    
    City Name: Cristobal Obregon
    City ID: 3530097
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3530097
    
    City Name: Perre
    City ID: 8013396
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=8013396
    
    City Name: Santiago do Cacem
    City ID: 2263458
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2263458
    
    City Name: Peypin
    City ID: 6454960
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6454960
    
    City Name: Schutzbach
    City ID: 2835583
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2835583
    
    City Name: Annur
    City ID: 1278539
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1278539
    
    City Name: Krasnyy Profintern
    City ID: 541446
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=541446
    
    City Name: Aguada
    City ID: 4562503
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4562503
    
    City Name: San Luis Obispo
    City ID: 5392323
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5392323
    
    City Name: Abu Zabad
    City ID: 380348
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=380348
    
    City Name: Washington
    City ID: 5218069
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5218069
    
    City Name: Galesti
    City ID: 677655
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=677655
    
    City Name: Glenns
    City ID: 4761123
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4761123
    
    City Name: Vitomiresti
    City ID: 662658
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=662658
    
    City Name: Cootamundra
    City ID: 7839718
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7839718
    
    City Name: Radchenko
    City ID: 503281
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=503281
    
    City Name: El Cuervo
    City ID: 2518510
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2518510
    
    City Name: Möhlin
    City ID: 7286514
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7286514
    
    City Name: Krina
    City ID: 2883895
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2883895
    
    City Name: Plan-de-Cuques
    City ID: 6447154
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6447154
    
    City Name: Copóns
    City ID: 3124643
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3124643
    
    City Name: Saint-Avit-Sénieur
    City ID: 2981493
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2981493
    
    City Name: Saint-Sylvestre-Pragoulin
    City ID: 2976821
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2976821
    
    City Name: Vilar de Besteiros
    City ID: 8014353
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=8014353
    
    City Name: Tuffé
    City ID: 6442764
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6442764
    
    City Name: Chernukha
    City ID: 568615
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=568615
    
    City Name: Shikotan
    City ID: 6930874
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6930874
    
    City Name: Weißbach
    City ID: 6555543
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6555543
    
    City Name: Yeola
    City ID: 1252738
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1252738
    
    City Name: San Francisco Zapotitlan
    City ID: 3590197
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3590197
    
    City Name: El Tablon
    City ID: 3682981
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3682981
    
    City Name: Bayt Marran
    City ID: 404915
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=404915
    
    City Name: Saint Helens
    City ID: 2638785
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2638785
    
    City Name: Bonansa
    City ID: 3127851
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3127851
    
    City Name: Stiftsgrün
    City ID: 2827040
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2827040
    
    City Name: Patsyeyki
    City ID: 623155
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=623155
    
    City Name: Shaami-Yurt
    City ID: 496204
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=496204
    
    City Name: Cercal
    City ID: 2269413
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2269413
    
    City Name: Kolobovka
    City ID: 546380
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=546380
    
    City Name: Zunzgen
    City ID: 2657899
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2657899
    
    City Name: Taranaki
    City ID: 2181872
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2181872
    
    City Name: Radhan
    City ID: 1167501
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1167501
    
    City Name: Scheyern
    City ID: 6556354
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6556354
    
    City Name: King Island
    City ID: 7839675
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7839675
    
    City Name: Jiyang
    City ID: 1805022
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1805022
    
    City Name: Ilvesheim
    City ID: 6555665
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6555665
    
    City Name: French Harbor
    City ID: 3609667
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3609667
    
    City Name: Namir
    City ID: 1515506
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1515506
    
    City Name: Barili
    City ID: 1726670
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1726670
    
    City Name: Lamberville
    City ID: 3008210
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3008210
    
    City Name: Prádena del Rincón
    City ID: 6359338
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6359338
    
    City Name: Garwolin
    City ID: 772339
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=772339
    
    City Name: Xiatangyunxiang
    City ID: 1930346
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1930346
    
    City Name: Voroshnevo
    City ID: 471820
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=471820
    
    City Name: Schwanden
    City ID: 2835304
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2835304
    
    City Name: Czarnkow
    City ID: 3101145
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3101145
    
    City Name: Vascoveiro
    City ID: 8012211
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=8012211
    
    City Name: Meyendorf
    City ID: 2871417
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2871417
    
    City Name: Troutdale
    City ID: 5757477
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5757477
    
    City Name: Anthering
    City ID: 2782475
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2782475
    
    City Name: Pecky
    City ID: 3068476
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3068476
    
    City Name: Menands
    City ID: 5126588
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5126588
    
    City Name: Jupiá
    City ID: 3459447
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3459447
    
    City Name: Lalapanzi
    City ID: 888667
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=888667
    
    City Name: Novi Seher
    City ID: 3194358
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3194358
    
    City Name: Lete
    City ID: 7614694
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7614694
    
    City Name: Villanueva del Trabuco
    City ID: 6359501
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6359501
    
    City Name: Likhoy
    City ID: 535253
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=535253
    
    City Name: Sankt Johann in der Haide
    City ID: 2766638
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2766638
    
    City Name: Nieder Neundorf
    City ID: 2863056
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2863056
    
    City Name: Göhren
    City ID: 6550537
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6550537
    
    City Name: Tuchlovice
    City ID: 3063896
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3063896
    
    City Name: Bruchsal
    City ID: 2943560
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2943560
    
    City Name: Jefferson
    City ID: 4766586
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4766586
    
    City Name: Ponnur
    City ID: 7302844
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7302844
    
    City Name: Rio Bueno
    City ID: 3873145
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3873145
    
    City Name: Erath
    City ID: 4323842
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4323842
    
    City Name: Männedorf
    City ID: 7286430
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7286430
    
    City Name: l'Alfàs del Pi
    City ID: 6355387
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6355387
    
    City Name: Altenhagen
    City ID: 6547809
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6547809
    
    City Name: Heralec
    City ID: 3075877
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3075877
    
    City Name: Maua
    City ID: 187231
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=187231
    
    City Name: Freshwater
    City ID: 2649069
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2649069
    
    City Name: Krouson
    City ID: 258744
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=258744
    
    City Name: Crigglestone
    City ID: 2651980
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2651980
    
    City Name: Yamachiche
    City ID: 6185138
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6185138
    
    City Name: Kostice
    City ID: 3073130
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3073130
    
    City Name: Pavlovskaya Sloboda
    City ID: 512039
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=512039
    
    City Name: Sielbeck
    City ID: 2832396
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2832396
    
    City Name: Lewisham
    City ID: 3333166
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3333166
    
    City Name: Shantou
    City ID: 1795940
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1795940
    
    City Name: Hochspeyer
    City ID: 2903026
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2903026
    
    City Name: Frederiksberg Kommune
    City ID: 2621941
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2621941
    
    City Name: Mysen
    City ID: 3145094
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3145094
    
    City Name: Banana
    City ID: 2177010
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2177010
    
    City Name: Lib
    City ID: 7306524
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7306524
    
    City Name: Norheim
    City ID: 2861830
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2861830
    
    City Name: Grantsdale
    City ID: 5655069
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5655069
    
    City Name: Xexéu
    City ID: 3384930
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3384930
    
    City Name: Tacligan
    City ID: 1684717
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1684717
    
    City Name: Senhora das Preces
    City ID: 2734130
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2734130
    
    City Name: Buttisholz
    City ID: 2661300
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2661300
    
    City Name: Pujiang
    City ID: 7843644
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7843644
    
    City Name: Vesper
    City ID: 2145253
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2145253
    
    City Name: Balakliya
    City ID: 712926
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=712926
    
    City Name: Budrio
    City ID: 6539713
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6539713
    
    City Name: Pfeffelbach
    City ID: 6555138
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6555138
    
    City Name: Merl
    City ID: 2871778
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2871778
    
    City Name: Bykhaw
    City ID: 629447
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=629447
    
    City Name: Montz
    City ID: 4333725
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4333725
    
    City Name: Elmali
    City ID: 315697
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=315697
    
    City Name: Kharmanli
    City ID: 730442
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=730442
    
    City Name: Kostromskaya Oblast’
    City ID: 543871
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=543871
    
    City Name: South Kensington
    City ID: 4369976
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4369976
    
    City Name: Richmond
    City ID: 5091729
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5091729
    
    City Name: Qualiano
    City ID: 3169724
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3169724
    
    City Name: Röllbach
    City ID: 6547457
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6547457
    
    City Name: Kotlyakovo
    City ID: 543672
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=543672
    
    City Name: Walda
    City ID: 2815191
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2815191
    
    City Name: Innertkirchen
    City ID: 2660255
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2660255
    
    City Name: Bessemer
    City ID: 5180106
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5180106
    
    City Name: Moulay Abdallah
    City ID: 2541906
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2541906
    
    City Name: Holma
    City ID: 2339468
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2339468
    
    City Name: Ouistreham
    City ID: 2989013
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2989013
    
    City Name: Cinyasag
    City ID: 8052270
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=8052270
    
    City Name: Mutschellen
    City ID: 7669789
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7669789
    
    City Name: Gemeente Barneveld
    City ID: 2759406
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2759406
    
    City Name: Darfield
    City ID: 2191913
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2191913
    
    City Name: Bierbeek
    City ID: 2801999
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2801999
    
    City Name: Rabenau
    City ID: 3208101
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3208101
    
    City Name: Sammatz
    City ID: 2842071
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2842071
    
    City Name: Globasnitz
    City ID: 2778467
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2778467
    
    City Name: Metcalfe
    City ID: 4435803
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4435803
    
    City Name: Dahlem
    City ID: 6554413
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6554413
    
    City Name: Paula Cândido
    City ID: 3454703
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3454703
    
    City Name: Mongolia
    City ID: 2029969
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2029969
    
    City Name: Bismarck
    City ID: 5688025
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5688025
    
    City Name: Flat River
    City ID: 5954426
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5954426
    
    City Name: Abramow
    City ID: 776808
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=776808
    
    City Name: El Limon
    City ID: 3642833
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3642833
    
    City Name: Sohāwal
    City ID: 1255873
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1255873
    
    City Name: Wanggang
    City ID: 7652271
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7652271
    
    City Name: Bianzano
    City ID: 6534956
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6534956
    
    City Name: Belegis
    City ID: 792764
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=792764
    
    City Name: Freamunde
    City ID: 8012790
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=8012790
    
    City Name: Eschi
    City ID: 7669564
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7669564
    
    City Name: Rock Fork
    City ID: 7248920
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7248920
    
    City Name: Tenancingo de Degollado
    City ID: 3516006
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3516006
    
    City Name: Hamminkeln
    City ID: 2911051
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2911051
    
    City Name: El Espino
    City ID: 3123496
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3123496
    
    City Name: Vysokovo
    City ID: 470148
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=470148
    
    City Name: Tionesta
    City ID: 5215696
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5215696
    
    City Name: Standenbühl
    City ID: 6554988
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6554988
    
    City Name: Manahawkin
    City ID: 4502866
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4502866
    
    City Name: Auray
    City ID: 3036059
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3036059
    
    City Name: Cadaques
    City ID: 3127117
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3127117
    
    City Name: Llantwit Fardre
    City ID: 2643934
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2643934
    
    City Name: Darby
    City ID: 4557485
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4557485
    
    City Name: Schweindorf
    City ID: 6553014
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6553014
    
    City Name: Plöwen
    City ID: 6548473
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6548473
    
    City Name: Ig
    City ID: 3199162
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3199162
    
    City Name: Zorita del Maestrazgo
    City ID: 3104261
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3104261
    
    City Name: Puebla de Almenara
    City ID: 2512268
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2512268
    
    City Name: Landrecht
    City ID: 6552212
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6552212
    
    City Name: Visby
    City ID: 2610150
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2610150
    
    City Name: Kallmerode
    City ID: 6549789
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6549789
    
    City Name: Salins
    City ID: 6443848
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6443848
    
    City Name: Schottwien
    City ID: 7873000
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7873000
    
    City Name: Ullerslev
    City ID: 2610942
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2610942
    
    City Name: Lichtenau
    City ID: 2878140
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2878140
    
    City Name: Ruelisheim
    City ID: 2982234
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2982234
    
    City Name: Arrondissement de Versailles
    City ID: 2969678
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2969678
    
    City Name: Guntramsdorf
    City ID: 7872978
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=7872978
    
    City Name: Khlong Yai
    City ID: 1609863
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1609863
    
    City Name: Kenley
    City ID: 2645820
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2645820
    
    City Name: Franklin Square
    City ID: 5117891
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=5117891
    
    City Name: Saint-Agnant
    City ID: 6428049
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6428049
    
    City Name: Ames
    City ID: 4670666
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4670666
    
    City Name: Japitan
    City ID: 1710269
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=1710269
    
    City Name: Hythe
    City ID: 2646317
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2646317
    
    City Name: Castro de Filabres
    City ID: 2519698
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2519698
    
    City Name: Carnlough
    City ID: 2653712
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2653712
    
    City Name: Golconda
    City ID: 4239519
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4239519
    
    City Name: San Paolo di Iesi
    City ID: 3167887
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3167887
    
    City Name: Caduaño
    City ID: 4016309
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=4016309
    
    City Name: Tongala
    City ID: 2146390
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=2146390
    
    City Name: Burolo
    City ID: 3181389
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3181389
    
    City Name: Obshtina Vetrino
    City ID: 725923
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=725923
    
    City Name: Colli del Tronto
    City ID: 3178314
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=3178314
    
    City Name: Cellarengo
    City ID: 6534317
    requested_url: http://api.openweathermap.org/data/2.5/weather?appid=b8cdca3c02508276a3ae854132f5d6e1&units=imperial&id=6534317
    



```python
#Extract data of interest
city_name = [data.get("name") for data in weather_data]
city_name_id = [data.get("id") for data in weather_data]
lat_data = [data.get("coord").get("lat") for data in weather_data]
lon_data = [data.get("coord").get("lon") for data in weather_data]
temp_data = [data.get("main").get("temp") for data in weather_data]
humid_data = [data.get("main").get("humidity") for data in weather_data]
cloud_data = [data.get("clouds").get("all") for data in weather_data]
wind_data = [data.get("wind").get("speed") for data in weather_data]

```


```python
#build weather data DataFrame:
weather_data = {"city name": city_name, "lat": lat_data, "temp": temp_data, "humidity": humid_data, "cloudiness": cloud_data, "wind speed": wind_data}
weather_data_df = pd.DataFrame(weather_data)
weather_data_df.to_csv('weatherpy_tel.csv')
weather_data_df.head(15)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city name</th>
      <th>cloudiness</th>
      <th>humidity</th>
      <th>lat</th>
      <th>temp</th>
      <th>wind speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Heintrop</td>
      <td>75</td>
      <td>76</td>
      <td>51.65</td>
      <td>51.24</td>
      <td>16.11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aspen Valley</td>
      <td>1</td>
      <td>76</td>
      <td>37.83</td>
      <td>53.60</td>
      <td>4.83</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Deliblato</td>
      <td>20</td>
      <td>71</td>
      <td>44.83</td>
      <td>51.80</td>
      <td>4.70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Dodworth</td>
      <td>40</td>
      <td>77</td>
      <td>53.54</td>
      <td>57.29</td>
      <td>21.92</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Scherpenheuvel-Zichem</td>
      <td>75</td>
      <td>76</td>
      <td>51.01</td>
      <td>52.34</td>
      <td>14.99</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Cullar-Vega</td>
      <td>0</td>
      <td>23</td>
      <td>37.15</td>
      <td>82.40</td>
      <td>6.93</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Viro Viro</td>
      <td>75</td>
      <td>74</td>
      <td>-17.65</td>
      <td>79.74</td>
      <td>9.17</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dale</td>
      <td>90</td>
      <td>62</td>
      <td>40.31</td>
      <td>58.12</td>
      <td>11.41</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Herleshausen</td>
      <td>75</td>
      <td>70</td>
      <td>51.02</td>
      <td>50.11</td>
      <td>25.28</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Huata</td>
      <td>0</td>
      <td>46</td>
      <td>-18.95</td>
      <td>63.77</td>
      <td>3.15</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Tormestorp</td>
      <td>0</td>
      <td>100</td>
      <td>56.12</td>
      <td>51.80</td>
      <td>10.29</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Oberlin</td>
      <td>90</td>
      <td>80</td>
      <td>41.29</td>
      <td>37.69</td>
      <td>9.17</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Riedholz</td>
      <td>75</td>
      <td>54</td>
      <td>47.23</td>
      <td>53.38</td>
      <td>10.29</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Gornje Mostre</td>
      <td>75</td>
      <td>75</td>
      <td>44.02</td>
      <td>48.38</td>
      <td>5.82</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Borredon</td>
      <td>0</td>
      <td>51</td>
      <td>44.88</td>
      <td>58.87</td>
      <td>6.93</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Build a scatter plot for temp vs lat data
temp_scat = plt.scatter(weather_data["lat"], weather_data["temp"], marker="o")

# Incorporate the other graph properties
plt.title("Temperature in World Cities")
plt.ylabel("Temperature (Farenheight)")
plt.xlabel("Latitude")
plt.grid(True)
```


```python
# Save the figure
plt.savefig("TemperatureInWorldCities.png")

# Show plot
plt.show()
```


![png](output_11_0.png)



```python
# Build a scatter plot for humidity vs data:
humid_scat = plt.scatter(weather_data["lat"], weather_data["humidity"], marker="o")

# Incorporate the other graph properties
plt.title("Stickiness (Humidity) in World Cities")
plt.ylabel("Stickiness (% Humidity) ")
plt.xlabel("Latitude")
plt.grid(True)
```


```python
# Save the figure
plt.savefig("HumidutyInWorldCities.png")

# Show plot
plt.show()
```


![png](output_13_0.png)



```python
# Build a scatter plot for cloudiness vs data:
cloud_scat = plt.scatter(weather_data["lat"], weather_data["cloudiness"], marker="o")

# Incorporate the other graph properties
plt.title("Cloudiness in World Cities")
plt.ylabel("Cloud coverage (%) ")
plt.xlabel("Latitude")
plt.grid(True)
```


```python
# Save the figure
plt.savefig("CloudinessInWorldCities.png")

# Show plot
plt.show()
```


![png](output_15_0.png)



```python
# Build a scatter plot for wind speed vs data:
wind_scat = plt.scatter(weather_data["lat"], weather_data["wind speed"], marker="o")

# Incorporate the other graph properties
plt.title("Wind Speed (mph) in World Cities")
plt.ylabel("wind Speed (MPH) ")
plt.xlabel("Latitude")
plt.grid(True)
```


```python
# Save the figure
plt.savefig("Wind SpeedInWorldCities.png")

# Show plot
plt.show()
```


![png](output_17_0.png)



```python

    
        
   
```


```python

```


```python

```
