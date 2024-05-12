import streamlit as st
import pandas as pd

st.set_page_config(page_title='My site Streamlit')
with st.container():
    st.subheader('Meu primeiro site com o Streamlit')
    st.title('Dashboard de contratos')
    st.write('Informações sobre os contratos fechados pela Hash&Co ao longo de Maio.')
    st.write('Quer aprender Python ? link: [Clique aqui](https://github.com/LucasTorres3001)')

@st.cache_data
def tableData() -> pd.DataFrame:
    return pd.read_csv('resultados.csv')

with st.container():
    st.write('---')
    qntd_dias = st.selectbox(label='Selecione o periodo: ', options=['7D', '15D', '21D', '30D'])
    num_dias = int(qntd_dias.replace('D', ''))
    datas = tableData()
    datas = datas[-num_dias:]
    st.area_chart(datas, x='Data', y='Contratos')