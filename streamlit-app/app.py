import streamlit as st
import requests

# Set the API URL
# API_URL = "http://dummy-api-service/api/data"
API_URL = "http://127.0.0.1:5001/api/data"

# Streamlit App
st.title("Streamlit App with Dummy API")

st.write("This app fetches data from the Dummy API.")

# Button to fetch data
if st.button("Fetch Data"):
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            st.success("Data fetched successfully!")
            st.json(data)  # Display data in JSON format
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error occurred: {e}")
