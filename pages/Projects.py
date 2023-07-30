import streamlit as st

def Projects_content():
    my_input = st.text_input("Ingresa tu nombre o DNI o Nro de Historia", st.session_state["my_input"])
    submit = st.button("Aceptar")
    if submit:
    st.session_state["my_input"] = my_input
    st.write("Has ingresado: ", my_input)
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
  
Projects_content()
#st.title("Projects")
#st.write("You have entered")
