import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

import streamlit as st
import pandasql as psql

import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.experimental_connection("gsheets", type=GSheetsConnection)
st.write(conn)
st.help(conn)


import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create GSheets connection
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# Read Google WorkSheet as DataFrame
df = conn.read(
    usecols=[
        0,
        1,
    ],  # specify columns which you want to get, comment this out to get all columns
)

# Display our Spreadsheet as st.dataframe
st.dataframe(df)
