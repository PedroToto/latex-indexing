import streamlit as st
from io import StringIO
import os
import time
import scripture_index


st.set_page_config(
    page_title="Latext indexing",
    page_icon="chart_with_upwards_trend",
    
    initial_sidebar_state="expanded",
    
)
st.markdown(
    f""" 
    <style>
    #.reportview-container .main .block-container{{
        padding-top: {1.3}rem;
        padding-right: {2.5}rem;
        padding-left: {3.4}rem;
        padding-bottom: {3.4}rem;
    }} 
    </style> 
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    footer:after {
        content:"  ·  Latex indexing ·  "; 
        visibility: visible;
        display: block;
        position: 'fixed';
        #background-color: red;
        padding: 5px;
        top: 2px;
    }
    </style>
    """
    , unsafe_allow_html=True
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

import warnings
warnings.filterwarnings("ignore")

st.title(" Add index tagging for Scripture references")


uploaded_file = st.file_uploader("Choose a latex file", type=["tex"], accept_multiple_files=False)

global result

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # To read file as string:
    # st.write(bytes_data)
    #string_data = stringio.read()
    with open(uploaded_file.name, 'wb') as f: 
        f.write(bytes_data)

    
    #print(string_data)
    # st.write(string_data)
    #print(stringio.read())
    # st.write(bytes_data)
    #print(bytes_data)
    #st.write(uploaded_file.getP)

    
    
    if st.button("Add tag index"):

        with st.spinner('Please wait while the file is procesing...'):
            result = scripture_index.add_index_faster(uploaded_file.name)

    
        if result:
            st.success('Done!')
            with open('indexed-'+uploaded_file.name, 'rb') as f:
                st.download_button('Download indexed file', f, file_name='indexed-'+uploaded_file.name)
            os.unlink('indexed-'+uploaded_file.name)
    
    #st.download_button('Download file', "indexed-"+uploaded_file.name)

    os.unlink(uploaded_file.name)
    
    # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)



