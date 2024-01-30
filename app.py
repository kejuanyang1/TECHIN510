"""
A world clock app
"""

import time
import datetime
import pytz
import streamlit as st

# Define the list of time zones to choose from
time_zones = {
    "None": None,  # Option for no selection
    "UTC": "UTC",
    "New York": "America/New_York",
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Moscow": "Europe/Moscow",
    "New Delhi": "Asia/Kolkata",
    "Beijing": "Asia/Shanghai"
}

# Function to get the current time in a given time zone
def get_current_time_in_zone(zone):
    if zone:
        tz = pytz.timezone(zone)
        return datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    return None

# Create a two-column layout
col1, col2 = st.columns([2, 1])

# Placeholders for the time displays in the left column
with col1:
    placeholder1 = st.empty()
    placeholder2 = st.empty()
    placeholder3 = st.empty()
    placeholder4 = st.empty()

# Dropdowns for time zone selection in the right column
with col2:
    zone1 = st.selectbox("Select Time Zone 1", list(time_zones.keys()), key="1")
    zone2 = st.selectbox("Select Time Zone 2", list(time_zones.keys()), key="2")
    zone3 = st.selectbox("Select Time Zone 3", list(time_zones.keys()), key="3")
    zone4 = st.selectbox("Select Time Zone 4", list(time_zones.keys()), key="4")

# Update the time displays
while True:
    if time_zones[zone1]:
        placeholder1.metric(label=f"Time in {zone1}", value=get_current_time_in_zone(time_zones[zone1]))
    else:
        placeholder1.empty()

    if time_zones[zone2]:
        placeholder2.metric(label=f"Time in {zone2}", value=get_current_time_in_zone(time_zones[zone2]))
    else:
        placeholder2.empty()

    if time_zones[zone3]:
        placeholder3.metric(label=f"Time in {zone3}", value=get_current_time_in_zone(time_zones[zone3]))
    else:
        placeholder3.empty()

    if time_zones[zone4]:
        placeholder4.metric(label=f"Time in {zone4}", value=get_current_time_in_zone(time_zones[zone4]))
    else:
        placeholder4.empty()

    time.sleep(1)

