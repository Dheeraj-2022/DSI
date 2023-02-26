import streamlit as st
from matplotlib import image as im
import pandas as pd
import plotly.express as px
import os


FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images","t.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

st.title("Titanic page")

img = im.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Survived = st.selectbox("Select the Survived:", df['survived'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['survived'] == Survived], x="sex")
col1.plotly_chart(fig_1, use_container_width=True)


fig_2 = px.box(df[df['survived'] == Survived], y="sex")
col2.plotly_chart(fig_2, use_container_width=True)
