import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
from typing import Union


st.set_page_config(page_title="Sahana", page_icon="	:cake:", layout="centered", initial_sidebar_state="auto", menu_items=None)

def animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def style():
    with open('style1.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

def hideAll():
    hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility:hidden;}
        </style>
        """   
    st.markdown(hide,unsafe_allow_html=True)


def main() -> None:

    st.write("---")
    with st.container():
        colm1,colm2 = st.columns(2)
        with colm1:
            st.image('demo.jpg')
        with colm2:
            st.title("Sahana Durgekar")
            st.subheader("CS Student and Python Developer")
            st.write("""Driven and motivated to help organizations thrive. Skilled in Prioritizing and Completing Tasks
independently. Extensive experience in Python""")
    st.write("---")
    with st.container():
        clm1,clm2 = st.columns(2)
        with clm1:
            st.header("EDUCATION")
            st.subheader("""Bachelor in Engineering""")
            st.markdown("""
            ##### M.S. Ramaiah Institute of Technology Bangalore
            - Information science and engineering""",
                unsafe_allow_html=True  )
        with clm2:
            anm: Union[dict, None] = animation("https://assets3.lottiefiles.com/packages/lf20_btjhwawa.json")
            st_lottie(anm,key="animation",width="250px",height="250px")

    st.write("---")
    st.header("WORK EXPERIENCE")
    st.markdown("""
        ### Intern/Python Developer
        ##### MoneyFactory""",
    unsafe_allow_html=True  )
 
    st.write("""
     #### Achievements/Tasks
        - Worked on Client Function to create database and executed necessary queries using Influx DB, MongoDB.
        - Worked on Welcome Page of MoneyFactory using HTML Using Figma Design Tool. 
    """)
    st.write("---")
    with st.container():
        last_colm1,last_colm2 = st.columns(2)
        with last_colm1:
            st.subheader("Skills")
            in_colm1,in_colm2 = st.columns(2)
            with in_colm1:
                st.write("""
                -  Python
                -  Html/css
                -  Javascript
                -  Communication
                """)
            with in_colm2:
                st.write("""
                -  MySQl
                -  Data Structures
                -  Java
                -  C
                """)
        st.write("---")
        with last_colm2:
            st.subheader("Place To Find Me : ")
            st.markdown("""
                - ###### [LinkedIn](https://www.linkedin.com/in/sahana-durgekar-a903a2186)
                - ###### [GitHub](https://github.com/sahana-github)
                - ###### [Gmail](https://sahanadurgekar18@gmail.com)
                """
                ,
                unsafe_allow_html=True)

if __name__ == "__main__":
    hideAll()
    style()
    main()



