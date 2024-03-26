import streamlit as st
import pandas as pd
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title='Tradutor',
    layout='wide'
)

col1, col2, col3, col4, col5 = st.columns(5)
st.title('Tradutor para ELDER FUTHARK')

option2 = col1.selectbox(
    'Selecione a linguagem original',
    ('Português', 'Islandês', 'Inglês'))
if option2 == 'Português':
    sour = 'pt'

if option2 == 'Islandês':
    sour = 'is'

if option2 == 'Inglês':
    sour = 'en'

txt = st.text_area(
    "Texto para traduzir",
    "Digite aqui seu texto",
    )

option = col2.selectbox(
    'Selecione para qual lingua traduzir',
    ('Português', 'Islandês', 'Inglês'))
if option == 'Português':
    linguagem = 'pt'

if option == 'Islandês':
    linguagem = 'is'

if option == 'Inglês':
    linguagem = 'en'

tradutor = GoogleTranslator(source=sour, target=linguagem)
traducao = tradutor.translate(txt)

st.write(f'Tradução do {option}: {traducao}')

traducao = traducao.upper()

traducao = traducao.replace('F', '\u16A0')
traducao = traducao.replace('U', '\u16A2')
traducao = traducao.replace('TH', '\u16A6')
traducao = traducao.replace('R', '\u16B1')
traducao = traducao.replace('A', '\u16AB')
traducao = traducao.replace('C', '\u16B2')
traducao = traducao.replace('Q', '\u16B2')
traducao = traducao.replace('K', '\u16B2')
traducao = traducao.replace('G', '\u16B7')
traducao = traducao.replace('W', '\u16B9')
traducao = traducao.replace('V', '\u16B9')
traducao = traducao.replace('H', '\u16BA')
traducao = traducao.replace('N', '\u16BE')
traducao = traducao.replace('I', '\u16C1')
traducao = traducao.replace('J', '\u16C3')
traducao = traducao.replace('EO', '\u16C7')
traducao = traducao.replace('P', '\u16C8')
traducao = traducao.replace('Z', '\u16C9')
traducao = traducao.replace('Y', '\u16C3')
traducao = traducao.replace('S', '\u16CB')
traducao = traducao.replace('T', '\u16CF')
traducao = traducao.replace('B', '\u16D2')
traducao = traducao.replace('E', '\u16D6')
traducao = traducao.replace('M', '\u16D7')
traducao = traducao.replace('L', '\u16DA')
traducao = traducao.replace('ING', '\u16DC')
traducao = traducao.replace('O', '\u16DF')
traducao = traducao.replace('D', '\u16DE')
traducao = traducao.replace('X', '\u16B2' + '\u16CA')
traducao = traducao.replace(' ', ':')
traducao = traducao.replace('Á', '\u16AB')
traducao = traducao.replace('É', '\u16D6')
traducao = traducao.replace('Ó', '\u16DF')
traducao = traducao.replace('Ý', '\u16C3')
traducao = traducao.replace('Æ', '\u16AB' + '\u16D6')
traducao = traducao.replace('Ú', '\u16A2')
traducao = traducao.replace('Ð', '\u16DE')
traducao = traducao.replace('Í', '\u16C1')
traducao = traducao.replace(',', '')
traducao = traducao.replace('Þ', '\u16A6')
traducao = traducao.replace('.', '')


st.write(f'Tradução do {option} para Elder Futhark: {traducao}')