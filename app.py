import streamlit as st


st.write('my first world')
peng_csv = pd.read_csv('peng.csv')
st.write(peng_csv)
