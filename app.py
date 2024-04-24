import streamlit as st
import pandas as pd
import os
import sqlite3
from surveyInput import getSurvey,downloadDF,showDf
from streamlit_option_menu import option_menu

if __name__=="__main__":

    st.set_page_config(
        page_title="Drift Social",
            layout="wide",
            initial_sidebar_state="collapsed",
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"}
    )
    hide_menu_style ="""
            <style>
             #MainMenu {visibility: hidden;}
             </style>
             """

    st.markdown(hide_menu_style, unsafe_allow_html=True)
    no_sidebar_style = """
    <style>
        div[data-testid="collapsedControl"] {display: none;}
    </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    def streamlit_menu1():
        selected = option_menu(
        menu_title=None,  # required
        options=["Home","Admin"],  # required
        icons=["house","admin"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        )
        return selected


    menu= streamlit_menu1()

    if menu=='Home':
      
        # Streamlit app
        st.title("Surveying Social Media Interactions: Reporting Harmful Speech")
        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image('./assets/team-logo.png', caption='Strivers')
            st.title("Fill Details")
        # Input form to add members
        try:
            fname = str(st.text_input("Enter Full Name (optional) :"))
            age = st.selectbox("Select Age:", [i for i in range(16,45)])
            socialPlatform = st.selectbox("Experienced on : ", ["Instagram","Facebook (meta) ","Twitter","Snapchat"])
        except Exception as e:
            st.error("Due to some we cant get your detials , Please fill the details again", icon="🔥🔥🔥🔥")
            print(e)

        st.header("[1] Select Language :", divider='rainbow')
        language = st.selectbox("", ["Marathi","English ","Hindi"])
        st.header("[2] Enter word/sentece which you feel voilent :", divider='rainbow')
        violent_speech= str(st.text_input("",placeholder="voilent sentence/word"))
        st.header("[3] Enter word/sentece which you feel hateful :", divider='rainbow')
        hateful_speech= str(st.text_input("",placeholder="hateful sentence/word"))
        st.header("[4] Enter word/sentece which you feel harmful :", divider='rainbow')
        harmful_speech= str(st.text_input("",placeholder="harmful sentence/word"))
        st.header("[5] Enter word/sentece which you feel spam or misleading :", divider='rainbow')
        spam_misleading_speech= str(st.text_input("",placeholder="spam or mesleading sentence/word"))
        if st.button("Submit",key=1):
            if(violent_speech =='' and harmful_speech=='' and harmful_speech==''and spam_misleading_speech==''):
                st.error("You need to fill atleast one field")
            if getSurvey(fname,int(age),socialPlatform,violent_speech,hateful_speech,harmful_speech,spam_misleading_speech,language):
                st.success("submission successful")


    if menu=='Admin':
        st.header("Enter Admin Password", divider='rainbow')
        password=st.text_input("")
        if st.button("Enter"):
            if password==os.environ["realpass1"] or password==os.environ["realpass2"]:
                if showDf():
                    # df = pd.read_csv('df.csv',columns=['username','userage','social_platform','violent_speech','hateful_speech','harmful_speech','spam_misleading_speech','language'])
                    df= pd.read_csv('df.csv')
                    st.table(df) 
                if downloadDF():
                    with open('df.csv') as f:
                        st.download_button('Download CSV',
                                            data=f,
                                            file_name='social_survey.csv',)             
            if password !=os.environ["realpass1"] and password!=os.environ["realpass2"]:
                st.warning("Wrong Password")
