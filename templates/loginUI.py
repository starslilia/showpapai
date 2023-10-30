import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Login")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Login"):
            if View.cliente_login(email, senha): st.write("Login realizado com sucesso!")
            else: st.write("Usuário ou senha inválido(s)")
            