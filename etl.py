import streamlit as st 
import pandas as pd 

data = {
        "task" : ["Extract","Transform","Load"],
        "Status":["completed","Processing","Pending"]
        }

df = pd.DataFrame(data)

st.title("Streamlit App : Welcome Priti")
st.write(df)