import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from PIL import Image

def page_content():

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
    #st.dataframe(df)

    st.title("Consulta de pacientes IREN")
    
    image = Image.open('images/logo.png')
    st.sidebar.image(image)
    st.sidebar.markdown("***")
    
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""
    
    my_input = st.text_input("Ingresa tu nombre o DNI o Nro de Historia", st.session_state["my_input"])
    submit = st.button("Aceptar")
    if submit:
        st.session_state["my_input"] = my_input
        st.write("Has ingresado: ", my_input)
    search_string = my_input

    # Create a boolean mask to identify rows containing the search_string in '' column
    mask = (df['d'] == search_string) | (df['e'] == search_string) | (df['k'] == search_string)
    if my_input:
        if not mask.any():
            st.write("Información incorrecta. Intente nuevamente.")
        
    # Filter the DataFrame to get rows where '' contains the search_string
    filtered_df = df[mask]

    # Get values from other columns ('' and '') in the same row
    d = filtered_df['d']
    e = filtered_df['e']
    k = filtered_df['k']
    g = filtered_df['g']
    l = filtered_df['l']
    t = filtered_df['t']
    x = filtered_df['x']
    y = filtered_df['y']

    aa = filtered_df['aa']
    ab = filtered_df['ab']
    
    columns = ['d', 'e', 'k', 'g', 'l', 't', 'x', 'y']
    columns1 = ['aa', 'ab']
    first_row_data_loc = df.loc[0, columns]
    first_row_data_loc1 = df.loc[0, columns1]


    
    concatenated_df = pd.concat([d, e, k, g, l, t, x, y], axis=1, keys=first_row_data_loc)
    concatenated_df1 = pd.concat([aa, ab], axis=1, keys=first_row_data_loc1)
    # ,ignore_index=True

    def make_hyperlink(url):
        return f"[{url}]({url})" if url.startswith("http") else url

    df_hlinks = concatenated_df1.applymap(make_hyperlink)
    
    # Display the concatenated DataFrame
    if my_input:
        st.dataframe(concatenated_df)
        st.dataframe(df_hlinks)
        #st.dataframe(concatenated_df1)
  
page_content()
#st.title("Projects")
#st.write("You have entered")
