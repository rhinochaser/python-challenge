

```python
# import Dependencies
import pandas as pd
import json
import numpy as np
```


```python
# load JSON
new_data_path = 'purchase_data.json'

```


```python
# read with pandas:
new_data_df = pd.read_json(new_data_path)
new_data_df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Total Number of Players:
player_count = len(new_data_df["SN"].unique())
player_count
```




    573




```python
'''**Purchasing Analysis (Total)**

* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue'''

unique_items = len(new_data_df["Item Name"].unique())
total_num_of_purchases = new_data_df["Item Name"].count()
avg_purchase_price = new_data_df["Price"].mean()
total_revenue = new_data_df["Price"].sum()

purch_anl = pd.DataFrame({"Number of Unique Items": [unique_items],"Average Purchase Price": [avg_purchase_price], "Total Number of Purchase": [total_num_of_purchases], "Total Revenue": [total_revenue]})
purch_anl.head()
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
      <th>Average Purchase Price</th>
      <th>Number of Unique Items</th>
      <th>Total Number of Purchase</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.931192</td>
      <td>179</td>
      <td>780</td>
      <td>2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
'''**Gender Demographics**

* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed'''

# Gender Demographics:

#Percentage and Count of Male Players:
male = new_data_df["Gender"].value_counts()['Male']
percent_male = (male/player_count)*100

#Percentage and Count of Female Players:
female = new_data_df["Gender"].value_counts()['Female']
percent_female = (female/player_count)*100

#Percentage and Count of Other / Non-Disclosed Players:
other_ND = player_count - male - female
percent_OND = (other_ND/player_count)*100

gen_demo_df = pd.DataFrame.from_items([('Male', [male, percent_male]), ('Female', [female, percent_female]), ('OND', [other_ND, percent_OND])], orient='index', columns=['Count', 'Percentage'])

gen_demo_df.head()
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
      <th>Count</th>
      <th>Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>110.471204</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>23.734729</td>
    </tr>
    <tr>
      <th>OND</th>
      <td>-196</td>
      <td>-34.205934</td>
    </tr>
  </tbody>
</table>
</div>




```python
'''Purchasing Analysis (Gender)
The below each broken by gender
Purchase Count
Average Purchase Price
Total Purchase Value
Normalized Totals'''
# Male Data:
male_df = new_data_df.loc[new_data_df["Gender"] == "Male"]
male_df.head()
male_PC = male_df["Item Name"].count()
print(f"male PC: {male_PC}")
male_APP = male_df["Price"].mean()
print(f"male APP: {male_APP}")
male_TPV = male_df["Price"].sum()
print(f"male TPV: {male_TPV}")
male_NT = np.std(male_APP)
print(f"male NT: {male_NT}")

```

    male PC: 633
    male APP: 2.9505213270142154
    male TPV: 1867.6799999999985
    male NT: 0.0



```python
# Female Data:
female_df = new_data_df.loc[new_data_df["Gender"] == "Female"]
female_df.head()
female_PC = female_df["Item Name"].count()
print(f"female PC: {female_PC}")
female_APP = female_df["Price"].mean()
print(f"female APP: {female_APP}")
female_TPV = female_df["Price"].sum()
print(f"female TPV: {female_TPV}")
female_NT = np.std(female_APP)
print(f"female NT: {female_NT}")
```

    female PC: 136
    female APP: 2.815514705882352
    female TPV: 382.90999999999985
    female NT: 0.0



```python
'''Age Demographics
The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
Purchase Count
Average Purchase Price
Total Purchase Value
Normalized Totals'''

age_bin_value = [0, 9, 14, 19, 24, 29, 34, 39, 44, 100]
age_bin_names = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45<']
new_data_df["Age Demographics"]= pd.cut(new_data_df["Age"], age_bin_value, labels=age_bin_names)


```


```python
demographic_group = new_data_df.groupby("Age Demographics")
demographic_group.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Demographics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>12</th>
      <td>30</td>
      <td>Male</td>
      <td>81</td>
      <td>Dreamkiss</td>
      <td>4.06</td>
      <td>Iskossa88</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>14</th>
      <td>40</td>
      <td>Male</td>
      <td>44</td>
      <td>Bonecarvin Battle Axe</td>
      <td>2.46</td>
      <td>Sundast29</td>
      <td>40-44</td>
    </tr>
    <tr>
      <th>18</th>
      <td>28</td>
      <td>Male</td>
      <td>91</td>
      <td>Celeste</td>
      <td>3.71</td>
      <td>Iskista88</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>19</th>
      <td>31</td>
      <td>Male</td>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
      <td>Assossa43</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11</td>
      <td>Female</td>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>Deural48</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>23</th>
      <td>19</td>
      <td>Male</td>
      <td>183</td>
      <td>Dragon's Greatsword</td>
      <td>2.36</td>
      <td>Chanosia65</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11</td>
      <td>Male</td>
      <td>65</td>
      <td>Conqueror Adamantite Mace</td>
      <td>1.96</td>
      <td>Qarwen67</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>26</th>
      <td>29</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Aerithllora36</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>27</th>
      <td>34</td>
      <td>Male</td>
      <td>106</td>
      <td>Crying Steel Sickle</td>
      <td>2.29</td>
      <td>Assastnya25</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>28</th>
      <td>15</td>
      <td>Male</td>
      <td>49</td>
      <td>The Oculus, Token of Lost Worlds</td>
      <td>4.23</td>
      <td>Ilariarin45</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>29</th>
      <td>16</td>
      <td>Female</td>
      <td>45</td>
      <td>Glinting Glass Edge</td>
      <td>2.46</td>
      <td>Phaedai25</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>31</th>
      <td>18</td>
      <td>Male</td>
      <td>37</td>
      <td>Shadow Strike, Glory of Ending Hope</td>
      <td>1.93</td>
      <td>Iarilis73</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>46</th>
      <td>11</td>
      <td>Male</td>
      <td>17</td>
      <td>Lazarus, Terror of the Earth</td>
      <td>3.47</td>
      <td>Palatyon26</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>54</th>
      <td>25</td>
      <td>Female</td>
      <td>101</td>
      <td>Final Critic</td>
      <td>4.62</td>
      <td>Minduli80</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>68</th>
      <td>11</td>
      <td>Male</td>
      <td>38</td>
      <td>The Void, Vengeance of Dark Magic</td>
      <td>2.82</td>
      <td>Qarwen67</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>70</th>
      <td>7</td>
      <td>Female</td>
      <td>158</td>
      <td>Darkheart, Butcher of the Champion</td>
      <td>3.56</td>
      <td>Eosurdru76</td>
      <td>&lt;10</td>
    </tr>
    <tr>
      <th>81</th>
      <td>38</td>
      <td>Male</td>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>Yaristi64</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>106</th>
      <td>37</td>
      <td>Female</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Chadossa56</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>117</th>
      <td>11</td>
      <td>Male</td>
      <td>160</td>
      <td>Azurewrath</td>
      <td>2.22</td>
      <td>Qarwen67</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>121</th>
      <td>7</td>
      <td>Male</td>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>Lassjask63</td>
      <td>&lt;10</td>
    </tr>
    <tr>
      <th>125</th>
      <td>7</td>
      <td>Female</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Heosurnuru52</td>
      <td>&lt;10</td>
    </tr>
    <tr>
      <th>170</th>
      <td>9</td>
      <td>Male</td>
      <td>71</td>
      <td>Demise</td>
      <td>4.07</td>
      <td>Reulae52</td>
      <td>&lt;10</td>
    </tr>
    <tr>
      <th>175</th>
      <td>35</td>
      <td>Male</td>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>Raillydeu47</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>179</th>
      <td>40</td>
      <td>Male</td>
      <td>70</td>
      <td>Hope's End</td>
      <td>3.89</td>
      <td>Chanosiaya39</td>
      <td>40-44</td>
    </tr>
    <tr>
      <th>186</th>
      <td>40</td>
      <td>Male</td>
      <td>144</td>
      <td>Blood Infused Guardian</td>
      <td>2.86</td>
      <td>Chanosiaya39</td>
      <td>40-44</td>
    </tr>
    <tr>
      <th>189</th>
      <td>35</td>
      <td>Male</td>
      <td>179</td>
      <td>Wolf, Promise of the Moonwalker</td>
      <td>1.88</td>
      <td>Raillydeu47</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>212</th>
      <td>40</td>
      <td>Male</td>
      <td>111</td>
      <td>Misery's End</td>
      <td>2.91</td>
      <td>Yarmol79</td>
      <td>40-44</td>
    </tr>
    <tr>
      <th>237</th>
      <td>7</td>
      <td>Male</td>
      <td>121</td>
      <td>Massacre</td>
      <td>3.42</td>
      <td>Lisistaya47</td>
      <td>&lt;10</td>
    </tr>
    <tr>
      <th>238</th>
      <td>40</td>
      <td>Female</td>
      <td>49</td>
      <td>The Oculus, Token of Lost Worlds</td>
      <td>4.23</td>
      <td>Chamadar27</td>
      <td>40-44</td>
    </tr>
    <tr>
      <th>264</th>
      <td>45</td>
      <td>Male</td>
      <td>124</td>
      <td>Venom Claymore</td>
      <td>2.72</td>
      <td>Marassaya49</td>
      <td>45&lt;</td>
    </tr>
  </tbody>
</table>
</div>




```python
demographic_group["Item Name"].count()
```




    Age Demographics
    10-14     35
    15-19    133
    20-24    336
    25-29    125
    30-34     64
    Name: Item Name, dtype: int64




```python
demographic_group["Price"].mean()
```




    Age Demographics
    10-14    2.770000
    15-19    2.905414
    20-24    2.913006
    25-29    2.962640
    30-34    3.082031
    35-39    2.842857
    40-44    3.189375
    45<      2.720000
    <10      2.980714
    Name: Price, dtype: float64




```python
demographic_group["Price"].sum()
```




    Age Demographics
    10-14     96.95
    15-19    386.42
    20-24    978.77
    25-29    370.33
    30-34    197.25
    35-39    119.40
    40-44     51.03
    45<        2.72
    <10       83.46
    Name: Price, dtype: float64




```python
'''**Top Spenders**

* Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
  * SN
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value'''

sn_users = new_data_df.groupby(["SN"])
sn_pur = new_data_df.groupby(["SN"])['Price'].count()
sn_price = new_data_df.groupby(["SN"])['Price'].sum()
avg_sn = sn_price/sn_pur

top_sn = pd.DataFrame({"Purchase Count": sn_pur, "Average Purchase Price":avg_sn, "Total Purchase Value":sn_price})
top_sn = top_sn.sort_values("Total Purchase Value", ascending=False)
top_sn = top_sn[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]

top_sn.reset_index(inplace=True)
top_sn.round(2)
top_sn.head()
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
      <th>SN</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Undirrala66</td>
      <td>5</td>
      <td>3.412000</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Saedue76</td>
      <td>4</td>
      <td>3.390000</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mindimnya67</td>
      <td>4</td>
      <td>3.185000</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Haellysu29</td>
      <td>3</td>
      <td>4.243333</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eoda93</td>
      <td>3</td>
      <td>3.860000</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
'''**Most Popular Items**

* Identify the 5 most popular items by purchase count, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value'''

by_itemid = new_data_df.groupby('Item ID')
pur_by_item = pd.DataFrame(by_itemid['Item ID'].count()) 
#counts occurance of item ID by grouping by item ID
pur_by_item.rename(columns = {"Item ID": "Number of Items Sold"}, inplace = True)
pur_by_item
ttlpchsvlu = pd.DataFrame(by_itemid['Price'].sum()) 
# sums Price grouped by item ID
ttlpchsvlu.rename(columns = {"Price": "Revenue"}, inplace =True)


no_dup_items = new_data_df.drop_duplicates('Item ID')

ttlpchsvlu
top5_pop = no_dup_items.merge(pur_by_item, left_on = "Item ID", right_index = True)
top5_pop = top5_pop.merge(ttlpchsvlu, left_on = "Item ID", right_index = True)
top5_pop = top5_pop[['Item ID', "Item Name", "Price", "Number of Items Sold", "Revenue"]]
top5_pop.sort_values("Number of Items Sold", ascending = False, inplace = True)
top5_pop = top5_pop.iloc[0:6][:] 
# Instead of top 5 did top six because 4 items had sales of 9 items each
top5_pop
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
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>Number of Items Sold</th>
      <th>Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>61</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>116</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>81</th>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>9</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>35</th>
      <td>13</td>
      <td>Serenity</td>
      <td>1.49</td>
      <td>9</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>56</th>
      <td>31</td>
      <td>Trickster</td>
      <td>2.07</td>
      <td>9</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>57</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
'''* Identify the 5 most profitable items by total purchase value, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value'''

top5_prof = no_dup_items.merge(pur_by_item, left_on = "Item ID", right_index = True)
top5_prof = top5_prof.merge(ttlpchsvlu, left_on = "Item ID", right_index = True)
top5_prof = top5_prof[['Item ID', "Item Name", "Number of Items Sold", "Price", "Revenue"]]
top5_prof.sort_values("Revenue", ascending = False, inplace = True)
top5_prof.head()
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
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Number of Items Sold</th>
      <th>Price</th>
      <th>Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>57</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>107</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>50</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>100</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>164</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
