import os
import streamlit as st
import json
import subprocess


def Web_Desing():
    st.set_page_config(
        page_title='Scrapy BD',
        layout="wide",
        page_icon='🔎'
    )
    with open('style.css') as style:
        st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)
    st.title('Scrapy Web')
    texto = st.text_input("Digite o nome do Banco:")
    if st.button('Confirmar', ):
        if 'data.json' in os.listdir():
            with open('data.json', 'w') as Data:
                Data.write('')
        process = subprocess.Popen(["scrapy", "runspider", "Web_Scrapy.py", "-a", f"start_urls={f"https://bancodata.com.br/relatorio/{texto}/"}", "-o", "data.json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            with open('data.json', 'r') as file:
                data = json.load(file)
            if not data:

                st.title(('Banco ' + texto.capitalize() + ' não encontrado !'))
            else:
                st.balloons()
                st.divider()
                st.title('Banco ' + texto.capitalize())
                title = []
                value = []
                for x in data:
                    title.append(str(x['title']))
                    value.append(str(x['value']))
                col1, col2, col3 = st.columns(3)
                col4, col5, col6 = st.columns(3)
                col7, col8, col9 = st.columns(3)
                col1.metric(title[0], value[0])
                col2.metric(title[1], value[1])
                col3.metric(title[2], value[2])
                col4.metric(title[3], value[3])
                col5.metric(title[4], value[4])
                col6.metric(title[5], value[5])
                col7.metric(title[6], value[6])
                col8.metric(title[7], value[7])
                col9.metric(title[8], value[8])
                st.divider()
                st.download_button('dowloand', 'a')

Web_Desing()
