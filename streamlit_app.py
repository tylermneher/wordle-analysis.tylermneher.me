import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('World Distribution by Letter Position')

df = pd.read_json("wordle-words.json")
df.rename(columns={"message": "word"}, inplace=True)
df.sort_values(by="word", inplace=True)

expandeds = []

for index, row in df.iterrows():
    word = list(row["word"])
    expandeds.append(word)

expandeds_df = pd.DataFrame(
    expandeds,
    columns=[
        "0_char",
        "1_char",
        "2_char",
        "3_char",
        "4_char",
    ],
)
expandeds_df["word"] = df["word"]


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(expandeds_df)

fig0 = px.histogram(expandeds_df["0_char"].sort_values(),
                    title="First Letter Frequency Distribution")
fig1 = px.histogram(
    expandeds_df["1_char"].sort_values(), title="Second Letter Frequency Distribution"
)
fig2 = px.histogram(expandeds_df["2_char"].sort_values(),
                    title="Third Letter Frequency Distribution")
fig3 = px.histogram(
    expandeds_df["3_char"].sort_values(), title="Fourth Letter Frequency Distribution"
)
fig4 = px.histogram(expandeds_df["4_char"].sort_values(),
                    title="Fifth Letter Frequency Distribution")


st.plotly_chart(fig0)
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)
