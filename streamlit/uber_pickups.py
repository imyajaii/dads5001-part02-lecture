import streamlit as st
import pandas as pd
import numpy as np

#Every good app has a title, so let's add one:
st.title('Uber pickups in NYC')

#Let's start by writing a function to load the data. Add this code to your script:

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Now let's test the function and review the output. Below your function, add these lines:
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

#Try adding @st.cache_data before the load_data declaration:
@st.cache_data
def load_data(nrows):
