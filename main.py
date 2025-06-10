import streamlit as st
st.title("영준app")
st.write("hello")
name=st.text_input("코드입력")
if name:
  if name=="yj":
    st.success("반갑습니다. 유영준님!")
  else:
    st.warning("error401")
