

```python
'''
Anlaysis:
Trend 1: As the number of rides per driver increase from Rural > Suburban > Urban.

Trend 2: The number of drivers per city increases as from Rural > Suburban > Urban.

Trend 3: Tha average fare price decreases from Rural > Suburban > Urban.

'''
```




    '\nAnlaysis:\nTrend 1: As the number of rides per driver increase from Rural > Suburban > Urban.\n\nTrend 2: The number of drivers per city increases as from Rural > Suburban > Urban.\n\nTrend 3: Tha average fare price decreases from Rural > Suburban > Urban.\n\n'




```python
# Dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

```


```python
city_data = pd.read_csv('raw_data/city_data.csv')
city_data.head()
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
city_data_df = pd.DataFrame(city_data)
city_data_df.head()
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
ride_data = pd.read_csv('raw_data/ride_data.csv')
ride_data.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
    </tr>
  </tbody>
</table>
</div>




```python
city_info_df= pd.merge(city_data, ride_data, on='city')
city_info_df.head()
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-19 04:27:52</td>
      <td>5.51</td>
      <td>6246006544795</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-04-17 06:59:50</td>
      <td>5.54</td>
      <td>7466473222333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-05-04 15:06:07</td>
      <td>30.54</td>
      <td>2140501382736</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-01-25 20:44:56</td>
      <td>12.08</td>
      <td>1896987891309</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-09 18:19:47</td>
      <td>17.91</td>
      <td>8784212854829</td>
    </tr>
  </tbody>
</table>
</div>




```python
city_info_df = pd.DataFrame(city_info_df)
city_info_df.head()
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-19 04:27:52</td>
      <td>5.51</td>
      <td>6246006544795</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-04-17 06:59:50</td>
      <td>5.54</td>
      <td>7466473222333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-05-04 15:06:07</td>
      <td>30.54</td>
      <td>2140501382736</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-01-25 20:44:56</td>
      <td>12.08</td>
      <td>1896987891309</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-09 18:19:47</td>
      <td>17.91</td>
      <td>8784212854829</td>
    </tr>
  </tbody>
</table>
</div>




```python
total_fares = city_info_df['fare'].sum()
total_fares
```




    64669.11999999995




```python
total_rides = city_info_df['ride_id'].count()
total_rides
```




    2407




```python
total_drivers = city_data_df['driver_count'].sum()
total_drivers
```




    3349




```python
'''Your objective is to build a Bubble Plot that showcases the relationship between four key variables:
Average Fare ($) Per City
Total Number of Rides Per City
Total Number of Drivers Per City
City Type (Urban, Suburban, Rural)'''
```




    'Your objective is to build a Bubble Plot that showcases the relationship between four key variables:\nAverage Fare ($) Per City\nTotal Number of Rides Per City\nTotal Number of Drivers Per City\nCity Type (Urban, Suburban, Rural)'




```python
city_groups = city_info_df.groupby('city')
```


```python
# isolated via Urban type city 
urban_fpc = city_info_df.loc[city_info_df['type']=='Urban']
urban_fpc_df = pd.DataFrame(urban_fpc)
urban_city_groups = urban_fpc_df.groupby('city')
```


```python
# Urban city total
urban_ucc = len(urban_city_groups["city"].unique())
urban_ct = urban_ucc
urban_ct
```




    66




```python
# Urban city fare totals
ucg_total = urban_city_groups['fare'].sum()
ucg_total_df = pd.DataFrame(ucg_total)
ucg_total_df.head()
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
      <th>fare</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alvarezhaven</th>
      <td>741.79</td>
    </tr>
    <tr>
      <th>Alyssaberg</th>
      <td>535.85</td>
    </tr>
    <tr>
      <th>Antoniomouth</th>
      <td>519.75</td>
    </tr>
    <tr>
      <th>Aprilchester</th>
      <td>417.65</td>
    </tr>
    <tr>
      <th>Arnoldview</th>
      <td>778.30</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reformatting the Urban city fare totals
ucg_total_df = ucg_total_df.rename(columns={"fare": "Urban Total Fare"})
ucg_total_df = ucg_total_df.reset_index()
ucg_total_df.head()
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
      <th>city</th>
      <th>Urban Total Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>741.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alyssaberg</td>
      <td>535.85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Antoniomouth</td>
      <td>519.75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Aprilchester</td>
      <td>417.65</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arnoldview</td>
      <td>778.30</td>
    </tr>
  </tbody>
</table>
</div>




```python
# avg fare per urban city
urban_acf = ucg_total / urban_ct
urban_acf_df = pd.DataFrame(urban_acf)
urban_acf_df.head()
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
      <th>fare</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alvarezhaven</th>
      <td>11.239242</td>
    </tr>
    <tr>
      <th>Alyssaberg</th>
      <td>8.118939</td>
    </tr>
    <tr>
      <th>Antoniomouth</th>
      <td>7.875000</td>
    </tr>
    <tr>
      <th>Aprilchester</th>
      <td>6.328030</td>
    </tr>
    <tr>
      <th>Arnoldview</th>
      <td>11.792424</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reformatting the avg fare per Urban city
urban_acf_df = urban_acf_df.rename(columns={"fare": "Average Urban Fare"})
urban_acf_df = urban_acf_df.reset_index()
urban_acf_df.head()
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
      <th>city</th>
      <th>Average Urban Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>11.239242</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alyssaberg</td>
      <td>8.118939</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Antoniomouth</td>
      <td>7.875000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Aprilchester</td>
      <td>6.328030</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arnoldview</td>
      <td>11.792424</td>
    </tr>
  </tbody>
</table>
</div>




```python
# total number of rides per Urban city
urban_trc = urban_city_groups['ride_id'].count()
urban_trc_df = pd.DataFrame(urban_trc)
urban_trc.dtype
```




    dtype('int64')




```python
# Reformatting the total number of rides per Urban city
urban_trc_df = urban_trc_df.rename(columns={"ride_id": "Urban Ride Total"})
urban_trc_df = urban_trc_df.reset_index()
urban_trc_df.head()
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
      <th>city</th>
      <th>Urban Ride Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>31</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alyssaberg</td>
      <td>26</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Antoniomouth</td>
      <td>22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Aprilchester</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arnoldview</td>
      <td>31</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Urban city Driver total
udt = urban_city_groups['driver_count'].unique()
udt = udt.astype(int)
udt.head()
```




    city
    Alvarezhaven    21
    Alyssaberg      67
    Antoniomouth    21
    Aprilchester    49
    Arnoldview      41
    Name: driver_count, dtype: int64




```python
# Merged Urban DataFrames
urban_merge = ucg_total_df.merge(urban_acf_df, on='city')
urban_summary = urban_merge.merge(urban_trc_df, on='city')
urban_summary.head()
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
      <th>city</th>
      <th>Urban Total Fare</th>
      <th>Average Urban Fare</th>
      <th>Urban Ride Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>741.79</td>
      <td>11.239242</td>
      <td>31</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alyssaberg</td>
      <td>535.85</td>
      <td>8.118939</td>
      <td>26</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Antoniomouth</td>
      <td>519.75</td>
      <td>7.875000</td>
      <td>22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Aprilchester</td>
      <td>417.65</td>
      <td>6.328030</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arnoldview</td>
      <td>778.30</td>
      <td>11.792424</td>
      <td>31</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Isolated info for Suburban type city
suburban_fpc = city_info_df.loc[city_info_df['type']=='Suburban']
suburban_fpc_df = pd.DataFrame(suburban_fpc)
suburban_city_groups = suburban_fpc_df.groupby('city')
```


```python
# Suburban city total
suburban_ucc = len(suburban_city_groups["city"].unique())
suburban_ct = suburban_ucc
suburban_ct
```




    41




```python
# Suburban Total Fares
sucg_total = suburban_city_groups['fare'].sum()
sucg_total_df = pd.DataFrame(sucg_total)
sucg_total_df.head()
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
      <th>fare</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Anitamouth</th>
      <td>335.84</td>
    </tr>
    <tr>
      <th>Campbellport</th>
      <td>505.67</td>
    </tr>
    <tr>
      <th>Carrollbury</th>
      <td>366.06</td>
    </tr>
    <tr>
      <th>Clarkstad</th>
      <td>372.62</td>
    </tr>
    <tr>
      <th>Conwaymouth</th>
      <td>380.51</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reformatting the Suburban Total Fares
sucg_total_df = sucg_total_df.rename(columns={"fare": "Suburban Total Fare"})
sucg_total_df = sucg_total_df.reset_index()
sucg_total_df.head()
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
      <th>city</th>
      <th>Suburban Total Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Anitamouth</td>
      <td>335.84</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Campbellport</td>
      <td>505.67</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Carrollbury</td>
      <td>366.06</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Clarkstad</td>
      <td>372.62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Conwaymouth</td>
      <td>380.51</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Suburban avg city fare
suburban_acf = sucg_total / suburban_ct
suburban_acf_df = pd.DataFrame(suburban_acf)
suburban_acf_df.head()
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
      <th>fare</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Anitamouth</th>
      <td>8.191220</td>
    </tr>
    <tr>
      <th>Campbellport</th>
      <td>12.333415</td>
    </tr>
    <tr>
      <th>Carrollbury</th>
      <td>8.928293</td>
    </tr>
    <tr>
      <th>Clarkstad</th>
      <td>9.088293</td>
    </tr>
    <tr>
      <th>Conwaymouth</th>
      <td>9.280732</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reformatting Suburban avg city fare
suburban_acf_df = suburban_acf_df.rename(columns={"fare": "Average Suburban Fare"})
suburban_acf_df = suburban_acf_df.reset_index()
suburban_acf_df.head()
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
      <th>city</th>
      <th>Average Suburban Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Anitamouth</td>
      <td>8.191220</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Campbellport</td>
      <td>12.333415</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Carrollbury</td>
      <td>8.928293</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Clarkstad</td>
      <td>9.088293</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Conwaymouth</td>
      <td>9.280732</td>
    </tr>
  </tbody>
</table>
</div>




```python
# total number of rides per Suburban city
suburban_trc = suburban_city_groups['ride_id'].count()
suburban_trc_df = pd.DataFrame(suburban_trc)
suburban_trc.head()
```




    city
    Anitamouth       9
    Campbellport    15
    Carrollbury     10
    Clarkstad       12
    Conwaymouth     11
    Name: ride_id, dtype: int64




```python
# Reformatting the total number of rides per Suburban city
suburban_trc_df = suburban_trc_df.rename(columns={"ride_id": "Suburban Ride Total"})
suburban_trc_df = suburban_trc_df.reset_index()
suburban_trc_df.head()
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
      <th>city</th>
      <th>Suburban Ride Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Anitamouth</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Campbellport</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Carrollbury</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Clarkstad</td>
      <td>12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Conwaymouth</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
suburban_merge = sucg_total_df.merge(suburban_acf_df, on='city')
suburban_merge2 = suburban_merge.merge(suburban_trc_df, on='city')
suburban_summary = suburban_merge2.merge(city_data_df, on='city')
suburban_summary.head()
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
      <th>city</th>
      <th>Suburban Total Fare</th>
      <th>Average Suburban Fare</th>
      <th>Suburban Ride Total</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Anitamouth</td>
      <td>335.84</td>
      <td>8.191220</td>
      <td>9</td>
      <td>16</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Campbellport</td>
      <td>505.67</td>
      <td>12.333415</td>
      <td>15</td>
      <td>26</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Carrollbury</td>
      <td>366.06</td>
      <td>8.928293</td>
      <td>10</td>
      <td>4</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Clarkstad</td>
      <td>372.62</td>
      <td>9.088293</td>
      <td>12</td>
      <td>21</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Conwaymouth</td>
      <td>380.51</td>
      <td>9.280732</td>
      <td>11</td>
      <td>18</td>
      <td>Suburban</td>
    </tr>
  </tbody>
</table>
</div>




```python
su_dc = suburban_summary['driver_count'].unique()
su_dc = su_dc.astype(int)
su_dc
```




    array([16, 26,  4, 21, 18,  9, 22,  7, 25,  8, 13, 12, 24,  5, 20, 14, 27,
           15,  3, 11, 10, 19,  6,  1, 17])




```python
# Isolated info by Rural type city
rural_fpc = city_info_df.loc[city_info_df['type']=='Rural']
rural_fpc_df = pd.DataFrame(rural_fpc)
rural_city_groups = rural_fpc_df.groupby('city')
```


```python
# Rural city total
rural_ucc = len(rural_city_groups["city"].unique())
rural_ct = rural_ucc
rural_ct
```




    18




```python
# Rural Total Fares
rural_total = rural_city_groups['fare'].sum()
rural_total_df = pd.DataFrame(rural_total)
rural_total_df.head()
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
      <th>fare</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>East Leslie</th>
      <td>370.27</td>
    </tr>
    <tr>
      <th>East Stephen</th>
      <td>390.53</td>
    </tr>
    <tr>
      <th>East Troybury</th>
      <td>232.71</td>
    </tr>
    <tr>
      <th>Erikport</th>
      <td>240.35</td>
    </tr>
    <tr>
      <th>Hernandezshire</th>
      <td>288.02</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reforamtted Rural Total Fares
rural_total_df = rural_total_df.rename(columns={"fare": "Rural Total Fare"})
rural_total_df = rural_total_df.reset_index()
rural_total_df.head()
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
      <th>city</th>
      <th>Rural Total Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>East Leslie</td>
      <td>370.27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>East Stephen</td>
      <td>390.53</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Troybury</td>
      <td>232.71</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Erikport</td>
      <td>240.35</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Hernandezshire</td>
      <td>288.02</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Suburban avg city fare
rural_acf = rural_total / rural_ct
rural_acf_df = pd.DataFrame(rural_acf)
rural_acf_df.head()
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
      <th>fare</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>East Leslie</th>
      <td>20.570556</td>
    </tr>
    <tr>
      <th>East Stephen</th>
      <td>21.696111</td>
    </tr>
    <tr>
      <th>East Troybury</th>
      <td>12.928333</td>
    </tr>
    <tr>
      <th>Erikport</th>
      <td>13.352778</td>
    </tr>
    <tr>
      <th>Hernandezshire</th>
      <td>16.001111</td>
    </tr>
  </tbody>
</table>
</div>




```python
rural_acf_df = rural_acf_df.rename(columns={"fare": "Average Rural Fare"})
rural_acf_df = rural_acf_df.reset_index()
rural_acf_df.head()
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
      <th>city</th>
      <th>Average Rural Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>East Leslie</td>
      <td>20.570556</td>
    </tr>
    <tr>
      <th>1</th>
      <td>East Stephen</td>
      <td>21.696111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Troybury</td>
      <td>12.928333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Erikport</td>
      <td>13.352778</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Hernandezshire</td>
      <td>16.001111</td>
    </tr>
  </tbody>
</table>
</div>




```python
# total number of rides per Rural city
rural_trc = rural_city_groups['ride_id'].count()
rural_trc_df = pd.DataFrame(rural_trc)
rural_trc_df.head()
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
      <th>ride_id</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>East Leslie</th>
      <td>11</td>
    </tr>
    <tr>
      <th>East Stephen</th>
      <td>10</td>
    </tr>
    <tr>
      <th>East Troybury</th>
      <td>7</td>
    </tr>
    <tr>
      <th>Erikport</th>
      <td>8</td>
    </tr>
    <tr>
      <th>Hernandezshire</th>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reformatted total number of rides per Rural city
rural_trc_df = rural_trc_df.rename(columns={"ride_id": "Suburban Ride Total"})
rural_trc_df = rural_trc_df.reset_index()
rural_trc_df.head()
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
      <th>city</th>
      <th>Suburban Ride Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>East Leslie</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>East Stephen</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Troybury</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Erikport</td>
      <td>8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Hernandezshire</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Rural Driver Total
rdt = rural_city_groups['driver_count'].unique()
rdt = rdt.astype(int)
rdt.head()
```




    city
    East Leslie        9
    East Stephen       6
    East Troybury      3
    Erikport           3
    Hernandezshire    10
    Name: driver_count, dtype: int64




```python
rural_merge = rural_total_df.merge(rural_acf_df, on='city')
rural_summary = rural_merge.merge(rural_trc_df, on='city')
rural_summary.head()
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
      <th>city</th>
      <th>Rural Total Fare</th>
      <th>Average Rural Fare</th>
      <th>Suburban Ride Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>East Leslie</td>
      <td>370.27</td>
      <td>20.570556</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>East Stephen</td>
      <td>390.53</td>
      <td>21.696111</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Troybury</td>
      <td>232.71</td>
      <td>12.928333</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Erikport</td>
      <td>240.35</td>
      <td>13.352778</td>
      <td>8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Hernandezshire</td>
      <td>288.02</td>
      <td>16.001111</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python

urban = plt.scatter(urban_trc, urban_acf, marker="o", facecolor="lightcoral", edgecolors="black", label = "Urban", s = udt, alpha = 0.75)


```


```python
suburban = plt.scatter(suburban_trc, suburban_acf, marker="o", facecolor="skyblue", edgecolors="black", label = "Suburban", s=su_dc, alpha=0.75)


```


```python
rural = plt.scatter(rural_trc, rural_acf, marker="o", facecolor="gold", edgecolors="black", label = "Rural", s=rdt, alpha=0.75)

```


```python
plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare ($)")

```




    <matplotlib.text.Text at 0x10f8abfd0>




```python
plt.ylim(0, 30)
```




    (0, 30)




```python
plt.xlim(0, 35)
```




    (0, 35)




```python
#legend
plt.legend(handles = [urban, suburban, rural], loc = 'best')
```




    <matplotlib.legend.Legend at 0x10f97c240>




```python
plt.grid()
```


```python
plt.savefig("pyber_ride_sharing_data.png")
plt.show()
```


![png](output_50_0.png)



```python
# % of Total Fares by Urban City Type
urb_tot_fare = ucg_total.sum()
urban_percent_tot_fare = (urb_tot_fare / total_fares) * 100
urban_percent_tot_fare
```




    61.97446323685868




```python
# % of Total Fares by Suburban City Type
sub_tot_fare = sucg_total.sum()
sub_percent_tot_fare = (sub_tot_fare / total_fares) * 100
sub_percent_tot_fare
```




    31.445750305555443




```python
# % of Total Fares by Rural City Type
rur_tot_fare = rural_total.sum()
rur_percent_tot_fare = (rur_tot_fare / total_fares) * 100
rur_percent_tot_fare
```




    6.579786457585944




```python
# Labels for the sections of our pie chart, 
labels = ["Total Urban Fares", "Total Suburban Fares", "Total Rural Fares"]

# The values of each section of the pie chart
sizes = [urban_percent_tot_fare, sub_percent_tot_fare, rur_percent_tot_fare]

# The colors of each section of the pie chart
colors = ["lightcoral","lightskyblue","gold"]

# Tells matplotlib to seperate section from the others
explode = (0.1, 0, 0.0)
```


```python
# Creates the pie chart based upon the values above
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=90)
```




    ([<matplotlib.patches.Wedge at 0x10fadb748>,
      <matplotlib.patches.Wedge at 0x112e9d048>,
      <matplotlib.patches.Wedge at 0x112ea6908>],
     [<matplotlib.text.Text at 0x10fae4550>,
      <matplotlib.text.Text at 0x112e9de10>,
      <matplotlib.text.Text at 0x112eae710>],
     [<matplotlib.text.Text at 0x10fae4ac8>,
      <matplotlib.text.Text at 0x112ea63c8>,
      <matplotlib.text.Text at 0x112eaec88>])




```python
# Tells matplotlib that we want a pie chart with equal axes
plt.axis("equal")
```




    (-1.2108148442451359,
     1.1195081872813206,
     -1.1505576098209547,
     1.1024075187583688)




```python
# Prints our pie chart to the screen
plt.savefig("total_fares_by_city_type_data.png")
plt.show()
```


![png](output_57_0.png)



```python
# % of Total Rides by Urban City Type
urb_tot_rides = urban_trc.sum()
urban_percent_tot_rides = (urb_tot_rides / total_rides)*100
urban_percent_tot_rides

```




    67.511425010386375




```python
# % of Total Rides by Suburban City Type
sub_tot_rides = suburban_trc.sum()
sub_percent_tot_rides = (sub_tot_rides / total_rides)*100
sub_percent_tot_rides
```




    27.295388450353137




```python
# % of Total Rides by Rural City Type
rur_tot_rides = rural_trc.sum()
rur_percent_tot_rides = (rur_tot_rides / total_rides)*100
rur_percent_tot_rides
```




    5.1931865392604903




```python
# Labels for the sections of our pie chart, 
labels = ["Urban Total Rides", "Suburban Total Rides", "Rural Total Rides"]

# The values of each section of the pie chart
sizes = [urban_percent_tot_rides, sub_percent_tot_rides, rur_percent_tot_rides ]

# The colors of each section of the pie chart
colors = ["lightcoral","lightskyblue","gold"]

# Tells matplotlib to seperate section from the others
explode = (0.1, 0, 0.0)
```


```python
# Creates the pie chart based upon the values above
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=90)
```




    ([<matplotlib.patches.Wedge at 0x112f8ee80>,
      <matplotlib.patches.Wedge at 0x112f9e780>,
      <matplotlib.patches.Wedge at 0x112fae080>],
     [<matplotlib.text.Text at 0x112f96c88>,
      <matplotlib.text.Text at 0x112fa7588>,
      <matplotlib.text.Text at 0x112faee48>],
     [<matplotlib.text.Text at 0x112f9e240>,
      <matplotlib.text.Text at 0x112fa7b00>,
      <matplotlib.text.Text at 0x112fb6400>])




```python
# Tells matplotlib that we want a pie chart with equal axes
plt.axis("equal")
```




    (-1.1932705425802141,
     1.1098032420872641,
     -1.1614913716774034,
     1.1029281765673717)




```python
# Prints our pie chart to the screen
plt.savefig("total_rides_per_city_type.png")
plt.show()
```


![png](output_64_0.png)



```python
# % of Total Drivers by Urban City Type
urb_tot_drivers = udt.sum()
urb_percent_tot_drivers = (urb_tot_drivers / total_drivers)*100
urb_percent_tot_drivers
```




    77.84413257688863




```python
# % of Total Drivers by Suburban City Type
srb_tot_drivers = su_dc.sum()
srb_percent_tot_drivers = (srb_tot_drivers / total_drivers)*100
srb_percent_tot_drivers

```




    10.540459838757839




```python
# % of Total Drivers by Rural City Type
rur_tot_drivers = rdt.sum()
rur_percent_tot_drivers = (rur_tot_drivers / total_drivers)*100
rur_percent_tot_drivers
```




    3.1054045983875787




```python
# Labels for the sections of our pie chart, 
labels = ["Urban Drivers", "Suburban Drivers", "Rural Drivers"]

# The values of each section of the pie chart
sizes = [urb_percent_tot_drivers, srb_percent_tot_drivers, rur_percent_tot_drivers]

# The colors of each section of the pie chart
colors = ["lightcoral","lightskyblue","gold"]

# Tells matplotlib to seperate section from the others
explode = (0.1, 0, 0.0)

```


```python
# Creates the pie chart based upon the values above
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=90)
```




    ([<matplotlib.patches.Wedge at 0x113087c18>,
      <matplotlib.patches.Wedge at 0x113098518>,
      <matplotlib.patches.Wedge at 0x1130a2dd8>],
     [<matplotlib.text.Text at 0x113090a20>,
      <matplotlib.text.Text at 0x1130a2320>,
      <matplotlib.text.Text at 0x1130a9be0>],
     [<matplotlib.text.Text at 0x113090f98>,
      <matplotlib.text.Text at 0x1130a2898>,
      <matplotlib.text.Text at 0x1130b0198>])




```python
# Tells matplotlib that we want a pie chart with equal axes
plt.axis("equal")
```




    (-1.1517790925545255,
     1.058572794442451,
     -1.1999187466243408,
     1.1047580355535356)




```python
# Prints our pie chart to the screen
plt.savefig("total_num_of_drivers_per_city_type.png")
plt.show()
```


![png](output_71_0.png)



```python

```
