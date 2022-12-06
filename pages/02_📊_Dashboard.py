# IMPORT LIBRARY
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import requests
from PIL import Image

# SET PAGE
pageicon = Image.open("aset_web/LOGO_HOAXCLICK.png")
st.set_page_config(page_title="HoaxClick Web App", page_icon=pageicon, layout="wide")

# IMPORT DATASET
# df = pd.read_excel('DATA_DATMIN_KEL11_CREDIT SCORING.xlsx')

# ---- LOAD ASSETS ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_ajzyv37m.json")

# HEADER
intro_column_left, intro_column_right = st.columns(2)
with st.container():
    with intro_column_left:
        # st.title(":bar_chart: Dashboard")
        st.markdown('<div style="text-align: justify; font-size:210%; line-height: 150%; margin-top: 10px;"> <b><br>Dashboard Analisis Berita Hoax & Clickbait di Indonesia </b> </div>',
            unsafe_allow_html=True)
    with intro_column_right:
        st_lottie(lottie_coding, height=250, key="dashboard")

# st.markdown("##")
st.markdown('<hr>', unsafe_allow_html=True)

# LOAD TOPIC CLICKBAIT DATASET
data_topic_clickbait = pd.read_excel('model/Kel5_Topic_Clickbait.xlsx')
data_topic_clickbait['Topic'] = data_topic_clickbait['Topic'].ffill()
data_topic_clickbait = data_topic_clickbait.rename(columns = {'Label_Akhir.1':'Jumlah', 'Label_Akhir':'Label_Clickbait'})
data_topic_clickbait = data_topic_clickbait.sort_values(by=['Jumlah', 'Label_Clickbait'], ascending=[True, False])

# LOAD TOPIC HOAX DATASET
data_topic_hoax = pd.read_excel('model/Kel5_Topic_Hoax.xlsx')
data_topic_hoax['Topic'] = data_topic_hoax['Topic'].ffill()
data_topic_hoax = data_topic_hoax.rename(columns = {'Label_Hoax.1':'Jumlah'})
data_topic_hoax = data_topic_hoax.sort_values(by=['Jumlah', 'Label_Hoax'], ascending=[True, False])

# ANGKA STATISTIK
left_column1, middle1_column1, middle2_column1, middle3_column1, right_column1 = st.columns(5)
with left_column1:
    st.subheader("Jumlah Berita Hoax / Palsu")
    sum_hoax = data_topic_hoax[data_topic_hoax['Label_Hoax'] == 'Hoax']['Jumlah'].sum()
    text_sum_hoax = "### " + str(sum_hoax)
    st.write(text_sum_hoax)
with middle1_column1:
    st.subheader("Jumlah Berita Non-Hoax")
    text_sum_nonhoax = "### " + str(data_topic_hoax['Jumlah'].sum() - sum_hoax)
    st.write(text_sum_nonhoax)
with middle2_column1:
    st.subheader("Jumlah Berita Clickbait")
    sum_clickbait = data_topic_clickbait[data_topic_clickbait['Label_Clickbait'] == 'Clickbait']['Jumlah'].sum()
    text_sum_clickbait = "### " + str(sum_clickbait)
    st.write(text_sum_clickbait)
with middle3_column1:
    st.subheader("Jumlah Berita Non-Clickbait")
    text_sum_nonclick = "### " + str(data_topic_clickbait['Jumlah'].sum() - sum_clickbait)
    st.write(text_sum_nonclick)
with right_column1:
    st.subheader("Jumlah Berita Keseluruhan")
    text_sum = "### " + str(data_topic_hoax['Jumlah'].sum() + data_topic_clickbait['Jumlah'].sum())
    st.write(text_sum)

st.markdown('<hr>', unsafe_allow_html=True)

# PIE CHART PROPORSI HOAX & CLICKBAIT
prop_clickbait = data_topic_clickbait.groupby('Label_Clickbait')['Jumlah'].sum()
prop_clickbait = pd.DataFrame(prop_clickbait)
prop_hoax = data_topic_hoax.groupby('Label_Hoax')['Jumlah'].sum()
prop_hoax = pd.DataFrame(prop_hoax)

fig_pie_clickbait = px.pie(prop_clickbait,
                           values="Jumlah",
                           names=prop_clickbait.index,
                           title="<b>Proporsi Berita Clickbait & Non-Clickbait</b>")
fig_pie_hoax = px.pie(prop_hoax,
                      values="Jumlah",
                      names=prop_hoax.index,
                      title="<b>Proporsi Berita Hoax & Non-Hoax</b>")

# BAR CHART PERBANDINGAN HOAX & NON-HOAX BERDASAR TOPIK
fig_bar_hoax = px.bar(data_topic_hoax, x="Jumlah", y="Topic", color="Label_Hoax", height=600,
                      barmode='group', orientation='h', title = 'Perbandingan Jumlah Berita Hoax & Non-Hoax berdasarkan Topik')
fig_bar_hoax.update_yaxes(matches=None, showticklabels=True, visible=True)
fig_bar_hoax.update_yaxes(automargin=True)

# BAR CHART PERBANDINGAN CLICKBAIT & NON-CLICKBAIT BERDASAR TOPIK
fig_bar_clickbait = px.bar(data_topic_clickbait, x="Jumlah", y="Topic", color="Label_Clickbait", height=600,
                      barmode='group', orientation='h', title = 'Perbandingan Jumlah Berita Clickbait & Non-Clickbait berdasarkan Topik')
fig_bar_clickbait.update_yaxes(matches=None, showticklabels=True, visible=True)
fig_bar_clickbait.update_yaxes(automargin=True)

# WORDCLOUD
wc_hoax = Image.open('aset_web/Viz_WordCloud_Hoax_Dataset.png')
wc_nonhoax = Image.open('aset_web/Viz_WordCloud_Non-Hoax_Dataset.png')
wc_clickbait = Image.open('aset_web/Viz_WordCloud_Clickbait_Dataset.png')
wc_nonclickbait = Image.open('aset_web/Viz_WordCloud_Non-Clickbait_Dataset.png')

# DASHBOARD
left_column2, right_column2 = st.columns(2)
left_column2.plotly_chart(fig_pie_hoax, use_container_width=True)
right_column2.plotly_chart(fig_pie_clickbait, use_container_width=True)

st.markdown('<hr>', unsafe_allow_html=True)
_, mid_column3 = st.columns([0.1, 7.9])
mid_column3.plotly_chart(fig_bar_hoax, use_container_width=True)

st.markdown('<hr>', unsafe_allow_html=True)
_, mid_column4 = st.columns([0.1, 7.9])
mid_column4.plotly_chart(fig_bar_clickbait, use_container_width=True)

st.markdown('<hr>', unsafe_allow_html=True)
left_column5, right_column5 = st.columns(2)
left_column5.image(wc_hoax, caption = "WordCloud Hoax Dataset", use_column_width=True)
right_column5.image(wc_nonhoax, caption = "WordCloud Non-Hoax Dataset", use_column_width=True)
left_column6, right_column6 = st.columns(2)
left_column6.image(wc_clickbait, caption = "WordCloud Clickbait Dataset", use_column_width=True)
right_column6.image(wc_nonclickbait, caption = "WordCloud Non-Clickbait Dataset", use_column_width=True)

