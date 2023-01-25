import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.title("WE ARE CONDUCTING THE FOLLOWING PROJECTS; :blush:")
from streamlit_option_menu import option_menu

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#-----load assets----
lottie_coding=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_caltkbh1.json")

with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
          st.header("WELCOME TO DREAMFAR GROUP")
          st.write("##")
          st.write(
              """
              make with Dreamfar Group the following:
              (1)Low cost web development.
              (2)Low cost software application development.
              (3)Project designing and implimentation(Artificial Intelligence).
              (4)Research and project development (Artificial Intelligence).
              (5)Data analysis and problems simulations.
              If you will be interested to work with us, we assures you great perfomance in archieving your goals
              """
    
          )
          st.write("[Our official whatsapp link>](https://chat.whatsapp.com/ITE4Fh3XhctIG3To6m6Xzb)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.sidebar:
    selected = option_menu(
        menu_title="Our Projects",
        options=["Project 1","Projects 2","Project 3"],
        icons=["display","door-open","bar-chart"],
        styles={
            #"container":{"paddind":"0!important":"background color"},
            "icons":{"color":"orange","font-size":"25px"},
            "nav-link":{
                "font-size":"25px",
                "text-align":"left",
                "margin":"1px",
                "--hover-color":"#eee",
            },
            "nav-link-selected":{"background-color":"blue"},
        },
        #menu_icoon="cast"
        #orientation="horizontal",
    )

if selected =="Project 1":
    st.title(f"The first project that Dreamfar group impliments is all about web and app development")
if selected =="Projects 2":
    st.title(f"The second project that Dreamfar group impliments involes Artificial Intelligence researches and projects developments")
if selected =="Project 3":
    st.title(f"The third part of project that Dreamfar group impliments includes data analysis and problem simulations")
    
#st.set_page_config(page_title="Our webpage WELCOME",page_icon=":tada:",layout="centered")
#st.title("Main Page")
#st.sidebar.success("Select a page above")
