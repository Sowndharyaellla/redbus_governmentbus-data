import streamlit as st
import pymysql
import pandas as pd
import re

# Initialize Streamlit page configuration

st.set_page_config(
    initial_sidebar_state="expanded",
    page_title="REDBUS",
    layout="wide",
)

# Load your logo image
logo_url = "C:\\Users\\SOWNDHARYA SRINATH\\Downloads\\redbus.jpg"
st.image(logo_url, width=100)

# Introduction
st.header('Government Bus Data')
st.markdown('_redBus is India’s largest online bus ticketing platform that has transformed bus travel in the country by bringing ease and convenience to millions of Indians who travel using buses. Founded in 2006, redBus is part of India’s leading online travel company MakeMyTrip Limited (NASDAQ: MMYT). By providing widest choice, superior customer service, lowest prices and unmatched benefits, redBus has served over 18 million customers. redBus has a global presence with operations across Indonesia, Singapore, Malaysia, Colombia and Peru apart from India')
with st.expander("Expand for more details"):
    st.write("Book affordable Indian Bus bus tickets online on redBus India with redDeals. Enjoy up to 25% off, plus additional savings on every online booking. Choose from various redDeals like Return trip, Early bird, Round Trip, Last minute, Trial, Festive tickets for maximum savings. Secure the lowest prices for your journey only on redBus.Indian Bus is currently offering 1 redDeals:")


# Establish database connection
try:
    mydb = pymysql.connect(host='localhost', user='root', password='', database='project_redbus')
    mycursor = mydb.cursor()
except pymysql.Error as e:
    st.error(f"Error connecting to database: {e}")

# Get state names
state_name = ['Kerala', 'Kadamba(KTCL)', 'Rajasthan(RSRTC)', 'Himachal(HPTDC)', 'Uttarpradesh(UPSRTC)', 'Bihar(BSRTC)', 'Southbengal(SBSTC)', 'Andhra(APSRTC)', 'Chandigarh(CTU)', 'Assam(ASTC)']

# Function to get route names based on selected state
def get_route_name(selected_state):
    query = "SELECT DISTINCT route_name FROM bus_data WHERE state_name = %s"
    mycursor.execute(query, (selected_state,))
    route_name = [row[0] for row in mycursor.fetchall()]
    return route_name

# Function to get bus types based on selected route 
def get_bus_type(selected_route):
    query = "SELECT DISTINCT bus_type FROM bus_data WHERE route_name = %s"
    mycursor.execute(query, (selected_route,))  # Pass selected_route as argument
    bus_type = [row[0] for row in mycursor.fetchall()]
    return bus_type

# Sidebar selection
with st.sidebar:
    st.markdown("""
    <style>
    .stButton > button {
        background-color: #4CAF50; /* light Green */
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;   

    }
    </style>
    """, unsafe_allow_html=True)

    selected_state = st.selectbox("Select State Name:", state_name)
    route_name = get_route_name(selected_state)
    selected_route = st.selectbox("Select Route Name:", route_name)

    # Get bus types based on selected route and populate dropdown
    bus_type = get_bus_type(selected_route)  # Call function with selected_route
    selected_bus_type = st.selectbox('Select the bus type:', bus_type)

    rating_filter = st.slider("Select minimum rating", 0.0, 5.0, 0.0)
    price_filter = st.slider("Select maximum price", 0, 10000, 0)

# Execute the query when the user clicks the "SEARCH" button
if st.button("SEARCH"):
        query = """
                SELECT bus_name, bus_type, departing, duration, reaching, rating, price, availability
                FROM bus_data
                WHERE state_name = %s
                AND route_name = %s
                AND bus_type = %s
                AND rating >= %s
                AND price <= %s
            """
        parameters = (selected_state, selected_route, selected_bus_type, rating_filter, price_filter)
        mycursor.execute(query, parameters)
        data = mycursor.fetchall()

        if data:
            df = pd.DataFrame(data, columns=['bus_name', 'bus_type', 'departing', 'duration', 'reaching', 'rating', 'price', 'availability'])
            st.write(df)
        else:
            st.info("No data found for the selected criteria.")
