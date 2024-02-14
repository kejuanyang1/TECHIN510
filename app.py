import streamlit as st
import pandas as pd
import altair as alt

from db import get_db_conn

# Connect to the database and fetch data
def fetch_data(query):
    conn = get_db_conn()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Prepare the main DataFrame from the events table
def get_events_data():
    query = "SELECT * FROM events;"
    df_events = fetch_data(query)
    df_events['date'] = pd.to_datetime(df_events['date'])  # Ensure 'date' is datetime type
    df_events['day_of_week'] = df_events['date'].dt.day_name()  # Add day of the week
    return df_events

df_events = get_events_data()

# Streamlit controls
category_filter = st.sidebar.selectbox('Filter by Category', options=['All'] + list(df_events['category'].unique()))
date_range = st.sidebar.date_input('Event Date Range', value=[df_events['date'].min(), df_events['date'].max()])
location_filter = st.sidebar.selectbox('Filter by Location', options=['All'] + list(df_events['location'].unique()))

# Filtering the DataFrame based on controls
if category_filter != 'All':
    df_events = df_events[df_events['category'] == category_filter]
if location_filter != 'All':
    df_events = df_events[df_events['location'] == location_filter]
df_events = df_events[(df_events['date'].dt.date >= date_range[0]) & (df_events['date'].dt.date <= date_range[1])]

# Chart 1: What category of events are most common in Seattle?
chart1 = alt.Chart(df_events).mark_bar().encode(
    x='category',
    y='count()',
    color='category',
    tooltip=['category', 'count()']
).properties(title='Event Categories in Seattle')

# Chart 2: What day of the week has the most number of events?
chart2 = alt.Chart(df_events).mark_bar().encode(
    x='day_of_week',
    y='count()',
    color='day_of_week',
    tooltip=['day_of_week', 'count()']
).properties(title='Events by Day of the Week')

# Chart 3: Where are events often held?
chart3 = alt.Chart(df_events).mark_bar().encode(
    x='venue',
    y='count()',
    color='venue',
    tooltip=['venue', 'count()']
).properties(title='Top Venues for Events')

# Display charts
st.altair_chart(chart1, use_container_width=True)
st.altair_chart(chart2, use_container_width=True)
st.altair_chart(chart3, use_container_width=True)