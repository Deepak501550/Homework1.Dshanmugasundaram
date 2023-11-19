#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import plotly.express as px


# In[ ]:





# In[34]:



covid_data = pd.read_csv('COVID-19 in Alabama.csv')  



# In[ ]:





# In[35]:


column_headings = covid_data.columns
print("Column Headings:")
print(column_headings)


# In[ ]:





# In[36]:


covid_data['Deaths'] = pd.to_numeric(covid_data['Deaths'], errors='coerce')   
covid_data['Cases'] = pd.to_numeric(covid_data['Cases'], errors='coerce')


covid_data['death_rate'] = (covid_data['Deaths'] / covid_data['Cases']) * 100



# In[ ]:





# In[50]:


sorted_covid_data = covid_data[['Counties', 'Cases', 'Total Tested By County', 'Deaths', 'death_rate']].sort_values(by='death_rate', ascending=False)

sorted_covid_data


# In[ ]:





# In[25]:


import pandas as pd
import matplotlib.pyplot as plt


# In[29]:





vaccine_providers_data = pd.read_csv('COVID-19 in Alabama Vaccine Providers.csv') 

providers_count_by_county = vaccine_providers_data.groupby('County')['Name'].count().reset_index()



# In[30]:


plt.figure(figsize=(12, 6))
plt.bar(providers_count_by_county['County'], providers_count_by_county['Name'])
plt.xlabel('County')
plt.ylabel('Number of Providers')
plt.title('Number of Vaccine Providers in Each County')
plt.xticks(rotation=90)
plt.show()


# In[59]:


pip install pandas


# In[60]:


pip install plotly


# In[ ]:





# In[ ]:





# In[61]:


import pandas as pd


vaccine_data = pd.read_csv('COVID-19 County Vaccine Data.csv') 


# In[ ]:





# In[110]:


vaccine_data['complete_vaccination_rate'] = (vaccine_data['People Completely Vaccinated'] / vaccine_data['Doses Administered']) * 100
sorted_vaccine_data = vaccine_data.sort_values(by='complete_vaccination_rate', ascending=False)
sorted_vaccine_data[['County', 'People Completely Vaccinated', 'complete_vaccination_rate']]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[111]:


plt.figure(figsize=(12, 12))
fig = px.bar(sorted_vaccine_data, x='County', y='People Completely Vaccinated',
             title='Complete Vaccination Rate by County in descending Order',
             labels={'complete_vaccination_rate': 'Complete Vaccination Rate (%)'},
             hover_data=['Doses Administered', 'complete_vaccination_rate'])


# In[112]:


fig.update_layout(xaxis_title='County', yaxis_title='Complete Vaccination Rate (%)')
fig.show()


# In[ ]:





# In[115]:


descriptive_stats = sorted_vaccine_data[['complete_vaccination_rate','People Completely Vaccinated']].describe()
print(descriptive_stats)


# In[116]:


correlation_matrix = sorted_vaccine_data[['complete_vaccination_rate','People Completely Vaccinated']].corr()
print(correlation_matrix)


# In[ ]:





# In[117]:


import plotly.express as px

fig = px.histogram(sorted_vaccine_data, x='complete_vaccination_rate', nbins=20,
                   title='Distribution of Complete Vaccination Rate')
fig.show()


# In[119]:


state_stats = sorted_vaccine_data.groupby('County')['complete_vaccination_rate'].mean().reset_index()
state_stats


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[89]:


fig = px.pie(sorted_vaccine_data, names='County', values='complete_vaccination_rate',
             title='Complete Vaccination Rate by County')


# In[ ]:





# In[ ]:





# In[ ]:





# In[90]:


fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




