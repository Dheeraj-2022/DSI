import streamlit as st 
from matplotlib import image as im
import pandas as pd
import plotly.express as px
import os


FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images" , "i.jpg")
DATA_PATH=os.path.join(dir_of_interest,"data","ipl_2023_dataset.csv")

st.title("IPL 2023 page")

img=im.imread(IMAGE_PATH)
st.image(img)

df=pd.read_csv(DATA_PATH)
st.dataframe(df)

Team=st.selectbox("Select the Team:",df['Team'].unique())

col1,col2=st.columns(2)

fig_1 = px.histogram(df[df['Team'] == Team], x="Price Cr")
col1.plotly_chart(fig_1, use_container_width=True)


fig_2 = px.box(df[df['Team'] == Team], y="Price Cr")
col2.plotly_chart(fig_2, use_container_width=True)
