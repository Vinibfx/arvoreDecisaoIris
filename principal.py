import streamlit as st

st.title('Aplicativo de IA')
nome = st.input_text('Digite o seu nome:')
st.write('Bem vindo(a)',nome,'ao seu primerio aplicativo')
