import streamlit as st
import pandas as pd
from views import View

class AgendaHojeUI:
    def main():
        agendas = View.agenda_listar_hoje()
        dic = []
        for obj in agendas:
            if obj.get_confirmado() == False:
                dic.append(obj.to_json())
        df = pd.DataFrame(dic)
        st.dataframe(df)
