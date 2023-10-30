import streamlit as st
import pandas as pd
from views import View
import datetime

class AgendaHojeUI:
    def main():
        agendas = View.agenda_listar_hoje()
        dic = []
        for obj in agendas:
            if obj.get_confirmado() == False and obj.get_data().day == datetime.datetime.now().day:
                dic.append(obj.to_json())
        df = pd.DataFrame(dic)
        st.dataframe(df)
