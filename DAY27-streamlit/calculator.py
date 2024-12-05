import streamlit as st

operation =""
num1= st.text_input('Type number A:')
num2= st.text_input('Type number B:')

a=int(num1)
b=int(num2)

operation=st.selectbox("Select your Operation :",("ADD","SUB","MUL","DIV"),)
st.write("User selection : ",operation)

if operation=="ADD":
    st.write("SUM = ",a+b)
elif operation=="SUB":
    st.write("SUB =",a-b)
elif operation=="MUL":
    st.write("MUL =",a*b)
elif operation=="DIV":
    st.write("DIV =",a/b)
