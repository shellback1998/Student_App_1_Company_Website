import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")


st.header("Company Website")
st.write("""
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam aut dignissimos, dolor dolores et eveniet ex
        magnam mollitia obcaecati, odio quae quasi sunt totam. Accusamus eaque eligendi harum in natus!
""")
st.subheader("Digital Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv")

with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the second column
with col2:
    # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])


with col3:
    # Iterate over rows 4 to 7
    for index, row in df[8:].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])