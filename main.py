import streamlit as st
from io import StringIO 
import scripture_index

st.title(" Add index tagging for Scripture references")
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

def btn_click(file):
    return True
    

uploaded_file = st.file_uploader("Choose a latex file", type=["tex"], accept_multiple_files=False)

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # To read file as string:
    # st.write(bytes_data)
    #string_data = stringio.read()
    # with open(uploaded_file.name, 'wb') as f: 
    #     f.write(bytes_data)

    
    #print(string_data)
    # st.write(string_data)
    #print(stringio.read())
    # st.write(bytes_data)
    #print(bytes_data)
    #st.write(uploaded_file.getP)
    
    if st.button("Add tag index"):
       
        scripture_index.add_index_faster(uploaded_file.name)

    st.download_button('Download file', "indexed-"+uploaded_file.name)
    # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)



