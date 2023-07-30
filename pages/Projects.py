import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def Projects_content():

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

    st.title("Consulta de pacientes IREN")
    
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""
    
    my_input = st.text_input("Ingresa tu nombre o DNI o Nro de Historia", st.session_state["my_input"])
    submit = st.button("Aceptar")
    if submit:
        st.session_state["my_input"] = my_input
        st.write("Has ingresado: ", my_input)
    search_string = my_input

    # Create a boolean mask to identify rows containing the search_string in 'City' column
    mask = (df['a'] == search_string) | (df['b'] == search_string) | (df['c'] == search_string)
    if not mask.any():
        st.write("Información incorrecta. Intente nuevamente.")
        
    # Filter the DataFrame to get rows where 'City' contains the search_string
    filtered_df = df[mask]

    # Get values from other columns ('Name' and 'Age') in the same row
    d = filtered_df['d']
    e = filtered_df['e']


    concatenated_df = pd.concat([d, e], axis=1, keys=['d', 'e'])
    # ,ignore_index=True

    # Display the concatenated DataFrame
    st.dataframe(concatenated_df)
  
Projects_content()
#st.title("Projects")
#st.write("You have entered")
