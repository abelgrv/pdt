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

st.subheader("📗 Google Sheets st.connection using Service Account")

st.write("#### 1. API Reference")
with st.echo():
    import streamlit as st
    from streamlit_gsheets import GSheetsConnection

    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    st.write(conn)
    st.help(conn)

st.write("#### 2. Initial setup")
st.markdown(
    """
## Initial setup for CRUD mode

1. Setup `.streamlit/secrets.toml` inside your Streamlit app root directory,  
check out [Secret management documentation](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management) for references.
2. [Enable API Access for a Project](https://docs.gspread.org/en/v5.7.1/oauth2.html#enable-api-access-for-a-project)
    * Head to [Google Developers Console](https://console.developers.google.com/) and create a new project (or select the one you already have).
    * In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.
    * In the box labeled “Search for APIs and Services”, search for “Google Sheets API” and enable it.
3. [Using Service Account](https://docs.gspread.org/en/v5.7.1/oauth2.html#for-bots-using-service-account)
    * Enable API Access for a Project if you haven’t done it yet.
    * Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
    * Fill out the form
    * Click “Create” and “Done”.
    * Press “Manage service accounts” above Service Accounts.
    * Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.
    * Select JSON key type and press “Create”.

You will automatically download a JSON file with credentials. It may look like this:
```
{
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    ...
}
```
Remember the path to the downloaded credentials file. Also, in the next step you’ll need the value of client_email from this file.
* **:red[Very important!]** Go to your spreadsheet and share it with a client_email from the step above. Just like you do with any other Google account. If you don’t do this, you’ll get a `gspread.exceptions.SpreadsheetNotFound` exception when trying to access this spreadsheet from your application or a script.

4. Inside `streamlit/secrets.toml` place `service_account` configuration from downloaded JSON file, in the following format (where `gsheets` is your `st.connection` name):
```
# .streamlit/secrets.toml

[connections.gsheets]
spreadsheet = "<spreadsheet-name-or-url>"
worksheet = "<worksheet-gid-or-folder-id>"  # worksheet GID is used when using Public Spreadsheet URL, when usign service_account it will be picked as folder_id
type = ""  # leave empty when using Public Spreadsheet URL, when using service_account -> type = "service_account"
project_id = ""
private_key_id = ""
private_key = ""
client_email = ""
client_id = ""
auth_uri = ""
token_uri = ""
auth_provider_x509_cert_url = ""
client_x509_cert_url = ""
```
"""
)

st.write("#### 3. Load DataFrame into Google Sheets")

with st.echo():
    import streamlit as st
    from streamlit_gsheets import GSheetsConnection

    # Create GSheets connection
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)

    # Demo Births DataFrame
    df = psql.load_births()

    # set create_spreadsheet to True to create spreadsheet,
    # create_spreadsheet is False by default to avoid exceeding Google API Quota
    create_spreadsheet = False

    if create_spreadsheet:
        df = conn.create(
            worksheet="Example 1",
            data=df,
        )

    # Display our Spreadsheet as st.dataframe
    st.dataframe(df.head(10))

st.write("#### 4. Read Google WorkSheet as DataFrame")
with st.echo():
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
