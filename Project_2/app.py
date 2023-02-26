from matplotlib import image as im
import os
import plotly.express as px
import pandas as pd
import streamlit as st 
import webbrowser

st.title("S Dheeraj Reddy")
st.header("Data Science Internship ")




st.snow()

b_click=st.button("Click Me!!")

if b_click == True:
    st.subheader("It is Intresting to work in DS_Intership")
    st.balloons()


st.title("My first :black[steamlit app] :sunglasses:")

st.header("Hello, Welcome to my web based data app.")

linkdin_link = 'https://www.linkedin.com/in/dheeraj-reddy-491aa0234/'

github_link='https://github.com/Dheeraj-2022'

st.write("Connect with me")

Linkedin=st.button('Linkedin')
Github=st.button('Github')

if Linkedin:
    webbrowser.open_new_tab(linkdin_link)
elif Github:   
    webbrowser.open_new_tab(github_link)

c=st.button("My portfolio")

if c == True:
    por="https://github.com/Dheeraj-2022?tab=repositories"
    st.write("These my own projects.")

    pf=st.button("Please check my projects.")
    if pf ==True:
        webbrowser.open_new_tab(por)





