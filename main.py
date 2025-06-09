import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("Okami Haruka")
    content = """lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat"""
    st.info(content)

content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)

col3, col4 = st.columns(2)

# default separator is comma, change it to semicolon if needed
df = pandas.read_csv('007 data.csv', sep=";")

# st.write(df)

# with col3:
#     for index, row in df[:10].iterrows():
#         st.header(row["title"])
# with col4:
#     for index, row in df[10:].iterrows():
#         st.header(row["title"])


# iterrows() returns index values that can be of different types (not necessarily integers), especially if your DataFrame has a custom index.
# that is why we use enumerate() with i variable to access the index and row data from itterrows.
# literally i will be used as a counter to keep track of the current row index.
with col3:
    # Show even-indexed rows (0, 2, 4, ...)
    for i, (index, row) in enumerate(df.iterrows()):
        if i % 2 == 0:
            st.header(row["title"])

with col4:
    # Show odd-indexed rows (1, 3, 5, ...)
    for i, (index, row) in enumerate(df.iterrows()):
        if i % 2 == 1:
            st.header(row["title"])