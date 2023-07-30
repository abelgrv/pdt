import streamlit as st
from PIL import Image
from pages import Projects

favicon = "images/ucsp.ico"
st.set_page_config(layout="wide",
    page_title="Multipage App",
    page_icon=favicon,
)


st.title(':green[Proyecto de Desarrollo Tecnológico]')
st.header('Construcción de un prototipo electromagnético capaz de medir propiedades dieléctricas de tejidos biológicos no homogéneos en ambiente controlado, basado en una sonda coaxial de circuito abierto')
st.sidebar.success("Selecciona una página")

image = Image.open('images/logo.png')
st.sidebar.image(image)
st.sidebar.markdown("***")

consult = st.button("Consulta de Pacientes IREN")
if consult:
    Projects_content()

col1, col2 = st.columns(2)

with col1:

	
	st.markdown("***")

	":green[This interactive tool is a discrete event simulation model, developed as a single component of the larger Hospital Efficiency Project multi-study.]"

	":green[The model represents surgical joint replacement activity from theatre scheduling, to ward stay, to discharge for primary and revision hip and knee replacement surgeries, \
	and unicompartmental knee replacement surgery.]"
	st.markdown("***")


with col2:
	st.markdown("***")
	
	st.write(':blue[Figure 1: Orthopaedic Model Process Flow]')
	image = Image.open('apply.jpg')
	st.image(image)
	
	st.write(':blue[Figure 2: Model Outputs and Inputs]')
	image = Image.open('apply.jpg')
	st.image(image)

with col1:
	":green[Flexible Theatre Schedule]"

	"The theatre schedule is flexible. The number of sessions per weekday, the surgical categories per session, and the number of operating theatres can be selected."

	"These can be compared with a default schedule in which 4 theatres operate 5 days per week, with 3 sessions per day.  Of those sessions, two will randomly \
	allocate either 2 primary joint replacements or 1 revision joint replacement, while the third session will schedule 1 primary joint replacement."

	"The flexible schedule will enable experimentation with the model, for example the effects of increasing the number of sessions per weekday, of adding \
	weekend sessions, or of scheduling different surgical types across weekdays."  
	
	"The impacts of these changes on bed utilisation and total surgical throughput can be investigated."
	
	st.markdown("***")
	":green[Simulation Scenarios]"

	"Other scenarios can also be investigated in the model."

	"For example, the mean lengths-of-stay of different surgical types, and the number of ring-fenced beds available to patients can be changed to understand \
	effects on surgical throughput."
	
	"Additionally, the mean number of days delayed can be changed.  This represents a proportion of patients whose ward length-of-stay\
	is delayed for various reasons, such as awaiting a community package of care. The proportion of these patients can also be changed."


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Ingresa tu nombre o DNI o Nro de Historia", st.session_state["my_input"])
submit = st.button("Aceptar")
if submit:
    st.session_state["my_input"] = my_input
    st.write("Has ingresado: ", my_input)

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
df = df.astype(str)
st.dataframe(df)


search_string = my_input

# Create a boolean mask to identify rows containing the search_string in 'City' column
mask = (df['a'].str.contains(search_string) |
        df['b'].str.contains(search_string) |
        df['c'].str.contains(search_string))

# Filter the DataFrame to get rows where 'City' contains the search_string
filtered_df = df[mask]

# Get values from other columns ('Name' and 'Age') in the same row
d = filtered_df['d']
e = filtered_df['e']

st.write(d)
st.write(e)

concatenated_df = pd.concat([d, e], axis=1, keys=['d', 'e'])
# ,ignore_index=True

# Display the concatenated DataFrame
st.dataframe(concatenated_df)

#sheet_id = '1131997511'
#csv_url = f"https://docs.google.com/spreadsheets/d/1aWE7keEB3fj3VlQsS8Auyka2WMhq21Fakog7lvVxZIo/export?format=csv"
#database_df = pd.read_csv(csv_url, on_bad_lines='skip')
