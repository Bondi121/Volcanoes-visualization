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
