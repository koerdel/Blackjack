#!/usr/bin/env python
# coding: utf-8

# # Importera bibliotek

# In[33]:


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[34]:


import requests


# In[77]:


Adresser = []
Länkar = []

for i in range(1,10):
    try:
        url = f"https://www.hemnet.se/bostader?item_types%5B%5D=bostadsratt&location_ids%5B%5D=925970&new_construction=exclude&page={i}&upcoming=exclude"
        Länk = [i["href"] for i in bs.select("a") if "https://www.hemnet.se/bostad/lagenhet" in i["href"]]
        Adress = [i.text[9:-7] for i in bs.select("h2.listing-card__street-address")]
        
        

        # Gör så att request kommer från en browser (i det här fallet från Mozilla version 5.0)
        req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
        # Läs info från url
        webpage = urlopen(req).read()
        # skapa en BeatifulSoup
        bs = soup(webpage, "html.parser")
        Länkar.append(Länk)        
        Adresser.append(Adress)


    except:
        break


# In[ ]:





# In[78]:


Adresser


# In[79]:


Adresser1 = []
for i in Adresser:
    for j in i:
        Adresser1.append(j)


# In[80]:


len(Adresser1)


# In[83]:


for i in Adresser1:
    if Adresser1.count(i) > 1:
        print(i)


# In[84]:


listan = list(set(Adresser1))


# In[85]:


len(Adresser1)


# In[86]:


Länkar1 = []
for i in Länkar:
    for j in i:
        Länkar1.append(j)


# In[87]:


len(Länkar1)


# In[44]:


from bs4 import BeautifulSoup as soup


# # Rubriker

# In[45]:


Länkar


# In[46]:


len(Länkar)


# In[47]:


Adresser


# In[48]:


len(Adresser)


# # Färdig kod

# In[49]:


url = "https://www.hemnet.se/bostad/lagenhet-3rum-vasastan-stockholms-kommun-sveavagen-121a,-3-tr-17451982"
# Gör så att request kommer från en browser (i det här fallet från Mozilla version 5.0)
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
# Läs info från url
webpage = urlopen(req).read()
# skapa en BeatifulSoup
bs = soup(webpage, "html.parser")
[i.text for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-visits-counter.qa-property-visits-counter > div:nth-child(1) > div.property-visits-counter__row-value")]
    


# In[69]:


print(len(lst))
print(len(lst1))
print(len(Rum_lst))
print(len(Kvm_lst))
print(len(Våning_lst))
print(len(Byggår_lst))
print(len(Avgift_lst))
print(len(Premium_lst))
print(len(Pris_m2_lst))
print(len(Pris_lst))
print(len(Mäklare_lst))


# In[50]:


lst = []
lst1 = []
Rum_lst = []
Kvm_lst = []
Våning_lst = []
Byggår_lst = []
Avgift_lst = []
Premium_lst = []
Pris_m2_lst = []
Pris_lst = []
Mäklare_lst = []

for i in Länkar1:  
    # Gör så att request kommer från en browser (i det här fallet från Mozilla version 5.0)
    req = Request(i , headers={'User-Agent': 'Mozilla/5.0'})
    # Läs info från url
    webpage = urlopen(req).read()
    # skapa en BeatifulSoup
    bs = soup(webpage, "html.parser")
    test=[i.text[9:-7].replace(u"\xa0", u"") for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-visits-counter.qa-property-visits-counter > div:nth-child(1) > div.property-visits-counter__row-value")]
    test1=[i.text[9:-7] for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-visits-counter.qa-property-visits-counter > div:nth-child(2) > div.property-visits-counter__row-value")]
    Rum = [i.text[0:-4].replace(u",", u".") for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-attributes-table > dl:nth-child(1) > div:nth-child(3) > dd")]
    Kvm = [i.text[0:-3].replace(u",", u".") for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-attributes-table > dl:nth-child(1) > div.property-attributes-table__row.qa-living-area-attribute > dd")]
    Våning = [i.text for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-attributes-table > dl:nth-child(1) > div.property-attributes-table__row.qa-floor-attribute > dd")]
    Byggår = [i.text for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-attributes-table > dl:nth-child(1) > div:nth-child(5) > dd")]
    Avgift = [i.text[8:-8].replace(u"\xa0", u"") for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-attributes-table > dl:nth-child(2) > div:nth-child(1)")]
    Premium =[i.text[1:-1] for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-visits-counter.qa-property-visits-counter > div:nth-child(3) > div.property-visits-counter__row-label > div > div")]
    Pris_m2 = [i.text for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-attributes-table > dl:nth-child(2)")]
    Pris = [i.text[0:-3].replace(u"\xa0", u"") for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__content > section > div > div.property-info__price-container > p")]
    Mäklare = [i.text[11:-2] for i in bs.select("#maklarinfo > div > div.broker-card__body > div.broker-card__info > a")]
    
    
    if test:
        lst.append(test[0])
    else:
        lst.append(np.nan)       
    if test1:
        lst1.append(test1[0])
    else:
        lst1.append(np.nan)       
    if Rum:
        Rum_lst.append(Rum[0])
    else:
        Rum_lst.append(np.nan)       
    if Kvm:
        Kvm_lst.append(Kvm[0])
    else:
        Kvm_lst.append(np.nan)     
    if Våning:
        Våning_lst.append(Våning[0])     
    else:
        Våning_lst.append(np.nan)
    if Byggår:
        Byggår_lst.append(Byggår[0])
    else:
        Byggår_lst.append(np.nan)       
    if Avgift:
        Avgift_lst.append(Avgift[0])
    else:
        Avgift_lst.append(np.nan)       
    if Premium:
        Premium_lst.append(Premium[0])
    else:
        Premium_lst.append("Bas")
    if Pris_m2:
        Pris_m2_lst.append(Pris_m2[0])
    else:
        Pris_m2_lst.append(np.nan)
    if Pris:
        Pris_lst.append(Pris[0])
    else:
        Pris_lst.append(np.nan)
    if Mäklare:
        Mäklare_lst.append(Mäklare[0])
    else:
        Mäklare_lst.append(np.nan)
    


# In[51]:


[i.text[1:-1] for i in bs.select("body > div.listing-container.qa-listing-container > div > div.listing__property-info.qa-property-info > div.property-info__container > div.property-info__attributes-and-description > div.property-attributes.qa-property-attributes > div.property-visits-counter.qa-property-visits-counter > div:nth-child(3) > div.property-visits-counter__row-label > div > div")]


# In[52]:


pd.set_option('display.max_rows', 1000)


# In[53]:


df.reset_index()


# In[98]:


pd.set_option('display.max_colwidth', 200)

df = pd.DataFrame({'Pris':Pris_lst, 'Antal rum':Rum_lst, 'Kvm':Kvm_lst, 
                   'Avgift':Avgift_lst, 'Antal besök':lst, 'Antal dagar':lst1, 'Kategori':Premium_lst,
                   'Mäklare':Mäklare_lst, 'Länkar':Länkar1})


# In[99]:


df = df.dropna(subset = ["Antal besök"])


# In[125]:


df['Pris'] = df['Pris'].astype(int)
df['Antal rum'] = df['Antal rum'].astype(float)
df['Kvm'] = df['Kvm'].astype(float)
df['Avgift'] = df['Avgift'].astype(int)
df['Antal besök'] = df['Antal besök'].astype(int)
df['Antal dagar'] = df['Antal dagar'].astype(int)
df.insert(1,'Pris/m2',(df['Pris']/df['Kvm']))
df['Pris/m2'] = df['Pris/m2'].astype(int)


# In[142]:


df.sort_values(by=['Antal besök'], inplace=True, ascending=False)


# In[149]:


df


# In[148]:


# Function to convert file path into clickable form.
def fun(path):
    f_url = "Länk"
    # returns the final component of a url
    #f_url = o.path.basename(path)
    # convert the url into link
    return f'<a href="{path}">{f_url}</a>'
df = df.style.format({'Länkar' : fun})


# In[145]:


df.sort_index(inplace=True)


# In[146]:


plt.figure(figsize=(12,8))
sns.barplot(data = df[2:10000], x = "Kategori", y = "Antal besök", hue = "Dagar",
            order=["Bas", "Plus", "Premium"], hue_order = ["10 eller färre dagar", "10 eller fler dagar"], palette="viridis")


# In[96]:


df[1:10000]


# In[97]:


df["Dagar"] = df["Antal dagar"].apply(lambda x: "10 eller färre dagar" if x <= 10 else "10 eller fler dagar") 


# In[124]:


sns.histplot(data = df[2:1000], x = "Kvm", bins=20)


# In[1477]:


sns.pieplot(df.Kategori[2:1000], bins=3)


# In[ ]:





# In[1434]:


summe.plot(kind = "bar", figsize = (12,8), fontsize = 15)
plt.title("Mäklare", fontsize = 20)
plt.show()


# In[1466]:


plt.figure(figsize=(12,8))
sns.barplot(data = df, x = "Kategori", y = "Antal rum", hue = "Dagar",
            order=["Bas", "Plus", "Premium"], hue_order = ["10 eller färre dagar", "10 eller fler dagar"], palette="viridis")


# In[129]:


pie, ax = plt.subplots(figsize=[10,6])
labels = ["Bas","Premium","Plus"]
plt.pie(x=df.Kategori.value_counts(), autopct="%.1f%%", labels=labels, pctdistance=0.5)


# In[138]:


sns.histplot(data = df[2:1000], x = "Kategori", bins=20, shrink=0.8)


# In[ ]:




