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

#import seaborn as sns
#import plotly.express as px
#import plotly.graph_objects as go
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# set up google sheets connection
scopes = ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']
#creds = ServiceAccountCredentials.from_json_keyfile_name('.streamlit/pdt-abel-ramos-56af719122c8.json', scopes)
#client = gspread.authorize(creds)

gc = gspread.service_account(filename='.streamlit/pdt-abel-ramos-56af719122c8.json')
# get data from google sheets
spreadsheet_id = '1aWE7keEB3fj3VlQsS8Auyka2WMhq21Fakog7lvVxZIo'
sheet = gc.open_by_key(spreadsheet_id)
sheet_instance = sheet.get_worksheet(0)
data = sheet_instance.get_all_records()
df = pd.DataFrame(data)

st.dataframe(df)


search_string = 'abel'

# Create a boolean mask to identify rows containing the search_string in 'City' column
mask = df['a'].str.contains(search_string)

# Filter the DataFrame to get rows where 'City' contains the search_string
filtered_df = df[mask]

# Get values from other columns ('Name' and 'Age') in the same row
names = filtered_df['b','c']
ages = filtered_df['c']

# Display the results
print("b:", names.tolist())
print("c:", ages.tolist())

st.write(names)
st.write(ages)

#sheet_id = '1131997511'
#csv_url = f"https://docs.google.com/spreadsheets/d/1aWE7keEB3fj3VlQsS8Auyka2WMhq21Fakog7lvVxZIo/export?format=csv"
#database_df = pd.read_csv(csv_url, on_bad_lines='skip')
