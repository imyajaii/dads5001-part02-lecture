import streamlit as st
import pandas as pd
import numpy as np
 
st.text('สู่ความเวิ้งว้างอันไกลโพ้น')
x1 = st.number_input('insert your number กงนี้จ้ะ')
#st.text(x1)
 
 
#st.text('สู่ความเวิ้งว้างอันไกลโพ้น')
x2 = st.number_input('insert your second number นะก๊ะ',key='x2')
#st.text(x1+ x2)
 
 
if st.button("calculate"):
    st.markdown(x1+ x2) # st.write able to use but using st.markdow just to make the result looks better instead !
 
 
if "counter" not in st.session_state:
    st.session_state.counter = 0
 
st.session_state.counter += 1
 
st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")
 
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])
 
st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)