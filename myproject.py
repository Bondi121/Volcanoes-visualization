import streamlit as st
import streamlit.components.v1 as components

# Set the title of the Streamlit app
st.title('Active Volcanoes Visualization')

# Add a brief description
st.markdown('''
This application displays an interactive visualization of active volcanoes around the world. The data includes various attributes of each volcano, such as location, eruption history, and more.
''')

# Read the HTML file
with open('./data/active_volcanoes.html', 'r', encoding='utf-8') as file:
    html_data = file.read()

# Display the HTML file in Streamlit
components.html(html_data, height=600)  # Adjust height as needed

# Additional information or notes
st.markdown('''
### Notes:
- The visualization is interactive; you can zoom in and out to explore different regions.
- Click on the volcano markers to see more details about each volcano.
- The data is regularly updated to reflect the latest information on volcanic activity.
''')


with open('./data/active_volcanoes.html', 'r', encoding='utf-8') as file:
    html_data = file.read()

components.html(html_data, height=600)  # Adjust height as needed

# Additional information or notes for the first visualization
st.markdown('''
### Notes:
- The visualization is interactive; you can zoom in and out to explore different regions.
- Click on the volcano markers to see more details about each volcano.
- The data is regularly updated to reflect the latest information on volcanic activity.
''')

# Display the second HTML file
st.header('Active Volcanoes by Country')
st.markdown('''
The scatter plot below illustrates the number of active volcanoes by country, color-coded by volcano status. This visualization helps to understand the distribution of volcanic activity in relation to the population of different countries.
''')

with open('./data/active_volcanoes_countries.html', 'r', encoding='utf-8') as file:
    html_data_countries = file.read()

components.html(html_data_countries, height=600)  # Adjust height as needed

# Additional information or notes for the second visualization
st.markdown('''
### Notes:
- Each bubble represents a country, with the size proportional to the number of active volcanoes.
- The colors indicate different statuses of volcanic activity (e.g., Holocene, Historical, Fumarolic, Seismicity).
- Hover over the bubbles to see the detailed information for each country.
''')