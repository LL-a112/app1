import streamlit as st

# Define the pages
main_page = st.Page("main.py", title="Main Page", icon="🎈")
page_2 = st.Page("page1.py", title="Page 2", icon="❄️")
page_3 = st.Page("page2.py", title="Page 3", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()