import streamlit as st

st.title('Aplicativo de IA')
nome = st.text_input('Digite o seu nome:')
if st.buttom('Clique aqui') :
   st.write('Bem vindo(a)',nome,'ao seu primerio aplicativo')
