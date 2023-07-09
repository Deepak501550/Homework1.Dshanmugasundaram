#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. The starting state is Rest. Calculate the probability of possible activity on the 15th day.


# In[3]:


import numpy as np

 

state = {
    0: "Rest",
    1: "Sweeties",
    2: "Exercise"
}

 

A = np.array([[0.2, 0.2, 0.6], [0.2, 0.1, 0.7], [0.1, 0.3, 0.6]])

 

start_state = 0
curr_state = start_state
n = 15

 

for _ in range(n - 1):
    curr_state = np.random.choice([0, 1, 2], p=A[curr_state])

 

activity = state[curr_state]
print("Activity on the 15th day:", activity)


# In[ ]:


# 2. What about the state and probability after 10000 days?


# In[4]:


import numpy as np

 

state = {
    0: "Rest",
    1: "Sweeties",
    2: "Exercise"
}

 

A = np.array([[0.2, 0.2, 0.6], [0.2, 0.1, 0.7], [0.1, 0.3, 0.6]])

 

start_state = 0
curr_state = start_state
n = 10000

 

state_count = {state_id: 0 for state_id in state}

 

for _ in range(n):
    curr_state = np.random.choice([0, 1, 2], p=A[curr_state])
    state_count[curr_state] += 1

 

state_probabilities = {state_id: count / n for state_id, count in state_count.items()}

 

print("State counts after 10000 days:")
for state_id, count in state_count.items():
    print(state[state_id], ":", count)

 

print("\nState probabilities after 10000 days:")
for state_id, prob in state_probabilities.items():
    print(state[state_id], ":", prob)


# In[ ]:


# 3. What do you observe from the above two?


# In[ ]:


# Activity on day 15: Looking at a single instance of a Markov chain 
# starting from an "inactive state", the activity on  day 15 can 
# vary due to the randomness of the process. The specific activity 
# observed on  day 15 depends on the probabilities defined in  transition matrix A.  
# State and probability after 10,000 days: By running a Monte Carlo simulation and running
# the Markov chain for a large number of days (in this case 10,000 days),
# we can gather statistics about the states visited. State counters indicate the 
# number of times each state was visited, while  state probabilities indicate the relative 
# frequency of each state during the simulation period. These probabilities 
# can give us insight into the long-term behavior of the Markov chain. 
# In summary, simulations allow the analysis of short and long-term results of the
# Markov chain and provide information about possible actions and their  probabilities at certain points 
# in time and over a longer period of time.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




