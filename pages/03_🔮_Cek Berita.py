import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from sklearn import preprocessing
from PIL import Image
import nltk
from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
import re, string
import requests
from bs4 import BeautifulSoup

# SET PAGE
pageicon = Image.open("aset_web/LOGO_HOAXCLICK.png")
st.set_page_config(page_title="HoaxClick Web App", page_icon=pageicon, layout="centered")

# SET TITLE
st.title('Yuk Cek Apakah Berita Anda Hoax/Clickbait!')

# DESCRIPTION
st.markdown('<div style="text-align: justify; font-size:160%"> Ayo berpartisipasi dalam usaha kami untuk memerangi berita hoax/clickbait! Kirimkan beberapa berita yang Anda temukan kepada kami, dan kami akan menggunakan teknologi kami untuk mengelompokkan berita tersebut menjadi yang benar dan yang tidak. Mari sama-sama membantu menjaga kebenaran informasi di internet! </div>',
            unsafe_allow_html=True)
st.write('')

# DEFINE PIPELINE TEXT PREPROCESSING
def remove_mention(text):
  return re.sub(r'@[A-Za-z0-9]+\s?', '', str(text))
def remove_hashtag(text):
  return re.sub(r'#[A-Za-z0-9]+\s?', '', str(text))
def remove_https(text):
  return re.sub(r'https:\/\/.*', '', str(text))
def remove_number(text):
  return re.sub(r'\d+', '', str(text))
def remove_punc(text):
  return text.translate(str.maketrans('','',string.punctuation+"“"+"🫶"))
def remove_whitespace(text):
  return text.strip()
def remove_whitespace_multi(text):
  return re.sub('\s+', ' ', text)
def remove_single_char(text):
  return re.sub(r'\b[a-zA-Z]\b', '', text)
def word_tokenize_wrapper(text):
  return word_tokenize(text)

# list_stopwords = stopwords.words('indonesian')
# list_stopwords = set(list_stopwords)
# def remove_stopwords(words):
#   return [word for word in words if word not in list_stopwords]

# LOAD MODEL HOAX & CLICKBAIT CLASSIFICATION
filename_model_hoax = 'model/Model_Final_Hoax.sav'
filename_tfidf_hoax = 'model/TFIDF_Final_Hoax.pickle'
filename_model_click = 'model/Model_Final_Clickbait_NB.sav'
filename_tfidf_click = 'model/TFIDF_Final_Clickbait.pickle'

@st.experimental_singleton
def load_model():
    model_hoax = pkl.load(open(filename_model_hoax, 'rb'))
    tfidf_hoax = pkl.load(open(filename_tfidf_hoax, 'rb'))
    model_clickbait = pkl.load(open(filename_model_click, 'rb'))
    tfidf_clickbait = pkl.load(open(filename_tfidf_click, 'rb'))
    return model_hoax, tfidf_hoax, model_clickbait, tfidf_clickbait

model_hoax, tfidf_hoax, model_clickbait, tfidf_clickbait = load_model()

# CHOOSE FILE
option = st.selectbox(
    'Apa yang ingin Anda cek?',
    ('Clickbait', 'Hoax', 'Link Berita'))

if option == 'Clickbait':
    judul = st.text_input('Judul Berita',
                          placeholder='Contoh : VIRAL! Ada kucing berkaki empat!')
    submit = st.button("Submit")

    ## SAVE INPUT IN DATAFRAME
    data_result = pd.DataFrame({'Judul': [judul]})
    data_result['Judul'] = data_result['Judul'].str.lower()
    data_result['Judul'] = data_result['Judul'].apply(remove_mention)
    data_result['Judul'] = data_result['Judul'].apply(remove_hashtag)
    data_result['Judul'] = data_result['Judul'].apply(remove_https)
    data_result['Judul'] = data_result['Judul'].apply(remove_number)
    data_result['Judul'] = data_result['Judul'].apply(remove_punc)
    data_result['Judul'] = data_result['Judul'].apply(remove_whitespace)
    data_result['Judul'] = data_result['Judul'].apply(remove_whitespace_multi)
    data_result['Judul'] = data_result['Judul'].apply(remove_single_char)
    data_result['Judul'] = data_result['Judul'].apply(word_tokenize_wrapper)
#     data_result['Judul'] = data_result['Judul'].apply(remove_stopwords)
    data_result['Judul'] = data_result['Judul'].agg(lambda x: ','.join(map(str, x)))
    y_pred = model_clickbait.predict(tfidf_clickbait.transform(data_result['Judul'].values))
    y_pred_proba = model_clickbait.predict_proba(tfidf_clickbait.transform(data_result['Judul'].values))

    if submit:
        y_pred = str(y_pred)
        y_pred_proba = np.max(y_pred_proba[0])
        y_pred_proba = np.round(y_pred_proba, 2)
        y_pred_proba = y_pred_proba * 100
        if y_pred[1] == '1':
            text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba) + '% Clickbait'
            st.error(text_result)
        else:
            text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba) + '% Tidak Clickbait'
            st.success(text_result)
elif option == 'Hoax':
    isi = st.text_input('Masukkan isi berita',
                        placeholder='Contoh : COVID-19 yang melanda negeri ini menguntungkan bagi beberapa pihak')
    submit = st.button("Submit")

    ## SAVE INPUT IN DATAFRAME
    data_result = pd.DataFrame({'Isi': [isi]})
    data_result['Isi'] = data_result['Isi'].str.lower()
    data_result['Isi'] = data_result['Isi'].apply(remove_mention)
    data_result['Isi'] = data_result['Isi'].apply(remove_hashtag)
    data_result['Isi'] = data_result['Isi'].apply(remove_https)
    data_result['Isi'] = data_result['Isi'].apply(remove_number)
    data_result['Isi'] = data_result['Isi'].apply(remove_punc)
    data_result['Isi'] = data_result['Isi'].apply(remove_whitespace)
    data_result['Isi'] = data_result['Isi'].apply(remove_whitespace_multi)
    data_result['Isi'] = data_result['Isi'].apply(remove_single_char)
    data_result['Isi'] = data_result['Isi'].apply(word_tokenize_wrapper)
#     data_result['Isi'] = data_result['Isi'].apply(remove_stopwords)
    data_result['Isi'] = data_result['Isi'].agg(lambda x: ','.join(map(str, x)))
    y_pred = model_hoax.predict(tfidf_hoax.transform(data_result['Isi'].values))
    y_pred_proba = model_hoax.predict_proba(tfidf_hoax.transform(data_result['Isi'].values))

    if submit:
        y_pred = str(y_pred)
        y_pred_proba = np.max(y_pred_proba[0])
        y_pred_proba = np.round(y_pred_proba, 2)
        y_pred_proba = y_pred_proba*100
        if y_pred[1] == '1':
            text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba) + '% Hoax'
            st.error(text_result)
        else:
            text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba) + '% Tidak Hoax'
            st.success(text_result)
else:
    st.error('WARNING : Fitur ini masih belum sempurna! Memasukkan link berita di luar sumber berita yang ada tidak direkomendasikan.')
    berita = st.selectbox(
        'Masukkan link dari berita ini: ',
        ('Detik', 'Kompas', 'Republika', 'Okezone', 'Liputan6'))
    if berita == 'Detik':
        url = st.text_input('Masukkan link berita',
                            placeholder='Contoh : https://finance.detik.com/moneter/d-6446090/suku-bunga-tinggi-bisa-bikin-sektor-jasa-keuangan-tertekan')
        submit = st.button("Submit")
        if submit:
            # Send a request to the URL and get the HTML response
            response = requests.get(url)
            # Parse the HTML response
            soup_judul = BeautifulSoup(response.text, "html.parser")
            soup_isi = BeautifulSoup(response.content, "html.parser")
            # Get the title and the text
            judul = soup_judul.find("title").text
            text = soup_isi.find_all("p")
            isi = ""
            for i in text:
                isi = isi + i.text
            result_judul = "Judul : " + str(judul)
            # Print the title and the text
            st.info(result_judul)
            ## SAVE INPUT IN DATAFRAME
            data_result = pd.DataFrame({'Judul': [judul],
                                        'Isi': [isi]})
            data_result['Judul'] = data_result['Judul'].str.lower()
            data_result['Judul'] = data_result['Judul'].apply(remove_mention)
            data_result['Judul'] = data_result['Judul'].apply(remove_hashtag)
            data_result['Judul'] = data_result['Judul'].apply(remove_https)
            data_result['Judul'] = data_result['Judul'].apply(remove_number)
            data_result['Judul'] = data_result['Judul'].apply(remove_punc)
            data_result['Judul'] = data_result['Judul'].apply(remove_whitespace)
            data_result['Judul'] = data_result['Judul'].apply(remove_whitespace_multi)
            data_result['Judul'] = data_result['Judul'].apply(remove_single_char)
            data_result['Judul'] = data_result['Judul'].apply(word_tokenize_wrapper)
#             data_result['Judul'] = data_result['Judul'].apply(remove_stopwords)
            data_result['Judul'] = data_result['Judul'].agg(lambda x: ','.join(map(str, x)))
            data_result['Isi'] = data_result['Isi'].str.lower()
            data_result['Isi'] = data_result['Isi'].apply(remove_mention)
            data_result['Isi'] = data_result['Isi'].apply(remove_hashtag)
            data_result['Isi'] = data_result['Isi'].apply(remove_https)
            data_result['Isi'] = data_result['Isi'].apply(remove_number)
            data_result['Isi'] = data_result['Isi'].apply(remove_punc)
            data_result['Isi'] = data_result['Isi'].apply(remove_whitespace)
            data_result['Isi'] = data_result['Isi'].apply(remove_whitespace_multi)
            data_result['Isi'] = data_result['Isi'].apply(remove_single_char)
            data_result['Isi'] = data_result['Isi'].apply(word_tokenize_wrapper)
#             data_result['Isi'] = data_result['Isi'].apply(remove_stopwords)
            data_result['Isi'] = data_result['Isi'].agg(lambda x: ','.join(map(str, x)))
            y_pred_judul = model_clickbait.predict(tfidf_clickbait.transform(data_result['Isi'].values))
            y_pred_proba_judul = model_clickbait.predict_proba(tfidf_clickbait.transform(data_result['Isi'].values))
            y_pred_isi = model_hoax.predict(tfidf_hoax.transform(data_result['Isi'].values))
            y_pred_proba_isi = model_hoax.predict_proba(tfidf_hoax.transform(data_result['Isi'].values))
            y_pred_isi = str(y_pred_isi)
            y_pred_judul = str(y_pred_judul)
            y_pred_proba_judul = np.max(y_pred_proba_judul[0])
            y_pred_proba_judul = np.round(y_pred_proba_judul, 2)
            y_pred_proba_judul = y_pred_proba_judul * 100
            y_pred_proba_isi = np.max(y_pred_proba_isi[0])
            y_pred_proba_isi = np.round(y_pred_proba_isi, 2)
            y_pred_proba_isi = y_pred_proba_isi * 100
            if y_pred_isi[1] == '1':
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_isi) + '% Hoax'
                st.error(text_result)
            else:
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_isi) + '% Tidak Hoax'
                st.success(text_result)
            if y_pred_judul[1] == '1':
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_judul) + '% Clickbait'
                st.error(text_result)
            else:
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_judul) + '% Tidak Clickbait'
                st.success(text_result)

    elif berita == 'Kompas':
        url = st.text_input('Masukkan link berita',
                            placeholder='Contoh : https://regional.kompas.com/read/2022/12/06/193951778/presiden-jokowi-akan-kenakan-surjan-saat-upacara-adat-panggih-pernikahan')
        submit = st.button("Submit")
        if submit:
            # Send HTTP request to the URL
            response = requests.get(url)
            # Parse HTML and save to BeautifulSoup object
            soup = BeautifulSoup(response.text, "html.parser")
            # Extract title
            title = soup.title.text
            # Extract content
            content = soup.find('div', {'class': 'read__content'}).text
            result_judul = "Judul : " + str(soup.find("title").text)
            # Print the title and the text
            st.info(result_judul)
            ## SAVE INPUT IN DATAFRAME
            data_result = pd.DataFrame({'Judul':[title],
                                        'Isi': [content]})
            data_result['Judul'] = data_result['Judul'].str.lower()
            data_result['Judul'] = data_result['Judul'].apply(remove_mention)
            data_result['Judul'] = data_result['Judul'].apply(remove_hashtag)
            data_result['Judul'] = data_result['Judul'].apply(remove_https)
            data_result['Judul'] = data_result['Judul'].apply(remove_number)
            data_result['Judul'] = data_result['Judul'].apply(remove_punc)
            data_result['Judul'] = data_result['Judul'].apply(remove_whitespace)
            data_result['Judul'] = data_result['Judul'].apply(remove_whitespace_multi)
            data_result['Judul'] = data_result['Judul'].apply(remove_single_char)
            data_result['Judul'] = data_result['Judul'].apply(word_tokenize_wrapper)
#             data_result['Judul'] = data_result['Judul'].apply(remove_stopwords)
            data_result['Judul'] = data_result['Judul'].agg(lambda x: ','.join(map(str, x)))
            data_result['Isi'] = data_result['Isi'].str.lower()
            data_result['Isi'] = data_result['Isi'].apply(remove_mention)
            data_result['Isi'] = data_result['Isi'].apply(remove_hashtag)
            data_result['Isi'] = data_result['Isi'].apply(remove_https)
            data_result['Isi'] = data_result['Isi'].apply(remove_number)
            data_result['Isi'] = data_result['Isi'].apply(remove_punc)
            data_result['Isi'] = data_result['Isi'].apply(remove_whitespace)
            data_result['Isi'] = data_result['Isi'].apply(remove_whitespace_multi)
            data_result['Isi'] = data_result['Isi'].apply(remove_single_char)
            data_result['Isi'] = data_result['Isi'].apply(word_tokenize_wrapper)
#             data_result['Isi'] = data_result['Isi'].apply(remove_stopwords)
            data_result['Isi'] = data_result['Isi'].agg(lambda x: ','.join(map(str, x)))
            y_pred_judul = model_clickbait.predict(tfidf_clickbait.transform(data_result['Isi'].values))
            y_pred_proba_judul = model_clickbait.predict_proba(tfidf_clickbait.transform(data_result['Isi'].values))
            y_pred_isi = model_hoax.predict(tfidf_hoax.transform(data_result['Isi'].values))
            y_pred_proba_isi = model_hoax.predict_proba(tfidf_hoax.transform(data_result['Isi'].values))
            y_pred_isi = str(y_pred_isi)
            y_pred_judul = str(y_pred_judul)
            y_pred_proba_judul = np.max(y_pred_proba_judul[0])
            y_pred_proba_judul = np.round(y_pred_proba_judul, 2)
            y_pred_proba_judul = y_pred_proba_judul * 100
            y_pred_proba_isi = np.max(y_pred_proba_isi[0])
            y_pred_proba_isi = np.round(y_pred_proba_isi, 2)
            y_pred_proba_isi = y_pred_proba_isi * 100
            if y_pred_isi[1] == '1':
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_isi) + '% Hoax'
                st.error(text_result)
            else:
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_isi) + '% Tidak Hoax'
                st.success(text_result)
            if y_pred_judul[1] == '1':
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_judul) + '% Clickbait'
                st.error(text_result)
            else:
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_judul) + '% Tidak Clickbait'
                st.success(text_result)

    elif berita == 'Republika':
        url = st.text_input('Masukkan link berita',
                            placeholder='Contoh : https://www.republika.co.id/berita/rmgz8r414/blackpink-dinobatkan-sebagai-entertainer-of-the-year-oleh-majalah-time')
        submit = st.button("Submit")
        if submit:
            # Send HTTP request to the URL
            response = requests.get(url)
            # Parse the HTML response
            soup_judul = BeautifulSoup(response.text, "html.parser")
            soup_isi = BeautifulSoup(response.content, "html.parser")
            # Get the title and the text
            judul = soup_judul.find("title").text
            text = soup_isi.find_all("p")
            isi = ""
            for i in text:
                isi = isi + i.text
            result_judul = "Judul : " + str(judul)
            # Print the title and the text
            st.info(result_judul)
            ## SAVE INPUT IN DATAFRAME
            data_result = pd.DataFrame({'Judul': [judul],
                                        'Isi': [isi]})
            data_result['Judul'] = data_result['Judul'].str.lower()
            data_result['Judul'] = data_result['Judul'].apply(remove_mention)
            data_result['Judul'] = data_result['Judul'].apply(remove_hashtag)
            data_result['Judul'] = data_result['Judul'].apply(remove_https)
            data_result['Judul'] = data_result['Judul'].apply(remove_number)
            data_result['Judul'] = data_result['Judul'].apply(remove_punc)
            data_result['Judul'] = data_result['Judul'].apply(remove_whitespace)
            data_result['Judul'] = data_result['Judul'].apply(remove_whitespace_multi)
            data_result['Judul'] = data_result['Judul'].apply(remove_single_char)
            data_result['Judul'] = data_result['Judul'].apply(word_tokenize_wrapper)
#             data_result['Judul'] = data_result['Judul'].apply(remove_stopwords)
            data_result['Judul'] = data_result['Judul'].agg(lambda x: ','.join(map(str, x)))
            data_result['Isi'] = data_result['Isi'].str.lower()
            data_result['Isi'] = data_result['Isi'].apply(remove_mention)
            data_result['Isi'] = data_result['Isi'].apply(remove_hashtag)
            data_result['Isi'] = data_result['Isi'].apply(remove_https)
            data_result['Isi'] = data_result['Isi'].apply(remove_number)
            data_result['Isi'] = data_result['Isi'].apply(remove_punc)
            data_result['Isi'] = data_result['Isi'].apply(remove_whitespace)
            data_result['Isi'] = data_result['Isi'].apply(remove_whitespace_multi)
            data_result['Isi'] = data_result['Isi'].apply(remove_single_char)
            data_result['Isi'] = data_result['Isi'].apply(word_tokenize_wrapper)
#             data_result['Isi'] = data_result['Isi'].apply(remove_stopwords)
            data_result['Isi'] = data_result['Isi'].agg(lambda x: ','.join(map(str, x)))
            y_pred_judul = model_clickbait.predict(tfidf_clickbait.transform(data_result['Isi'].values))
            y_pred_proba_judul = model_clickbait.predict_proba(tfidf_clickbait.transform(data_result['Isi'].values))
            y_pred_isi = model_hoax.predict(tfidf_hoax.transform(data_result['Isi'].values))
            y_pred_proba_isi = model_hoax.predict_proba(tfidf_hoax.transform(data_result['Isi'].values))
            y_pred_isi = str(y_pred_isi)
            y_pred_judul = str(y_pred_judul)
            y_pred_proba_judul = np.max(y_pred_proba_judul[0])
            y_pred_proba_judul = np.round(y_pred_proba_judul, 2)
            y_pred_proba_judul = y_pred_proba_judul * 100
            y_pred_proba_isi = np.max(y_pred_proba_isi[0])
            y_pred_proba_isi = np.round(y_pred_proba_isi, 2)
            y_pred_proba_isi = y_pred_proba_isi * 100
            if y_pred_isi[1] == '1':
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_isi) + '% Hoax'
                st.error(text_result)
            else:
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_isi) + '% Tidak Hoax'
                st.success(text_result)
            if y_pred_judul[1] == '1':
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_judul) + '% Clickbait'
                st.error(text_result)
            else:
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_judul) + '% Tidak Clickbait'
                st.success(text_result)
    elif berita == 'Okezone':
        url = st.text_input('Masukkan link berita',
                            placeholder='Contoh : https://economy.okezone.com/read/2022/12/06/320/2721886/heboh-kabar-phk-jiwasraya-direksi-dan-karyawan-dapat-insentif-0-8-kali-gaji')
        submit = st.button("Submit")
        if submit:
            # Send HTTP request to the URL
            response = requests.get(url)
            # Parse the HTML response
            soup_judul = BeautifulSoup(response.text, "html.parser")
            soup_isi = BeautifulSoup(response.content, "html.parser")
            # Get the title and the text
            judul = soup_judul.find("title").text
            text = soup_isi.find_all("p")
            isi = ""
            for i in text:
                isi = isi + i.text
            result_judul = "Judul : " + str(judul)
            # Print the title and the text
            st.info(result_judul)
            ## SAVE INPUT IN DATAFRAME
            data_result = pd.DataFrame({'Judul': [judul],
                                        'Isi': [isi]})
            data_result['Judul'] = data_result['Judul'].str.lower()
            data_result['Judul'] = data_result['Judul'].apply(remove_mention)
            data_result['Judul'] = data_result['Judul'].apply(remove_hashtag)
            data_result['Judul'] = data_result['Judul'].apply(remove_https)
            data_result['Judul'] = data_result['Judul'].apply(remove_number)
            data_result['Judul'] = data_result['Judul'].apply(remove_punc)
            data_result['Judul'] = data_result['Judul'].apply(remove_whitespace)
            data_result['Judul'] = data_result['Judul'].apply(remove_whitespace_multi)
            data_result['Judul'] = data_result['Judul'].apply(remove_single_char)
            data_result['Judul'] = data_result['Judul'].apply(word_tokenize_wrapper)
#             data_result['Judul'] = data_result['Judul'].apply(remove_stopwords)
            data_result['Judul'] = data_result['Judul'].agg(lambda x: ','.join(map(str, x)))
            data_result['Isi'] = data_result['Isi'].str.lower()
            data_result['Isi'] = data_result['Isi'].apply(remove_mention)
            data_result['Isi'] = data_result['Isi'].apply(remove_hashtag)
            data_result['Isi'] = data_result['Isi'].apply(remove_https)
            data_result['Isi'] = data_result['Isi'].apply(remove_number)
            data_result['Isi'] = data_result['Isi'].apply(remove_punc)
            data_result['Isi'] = data_result['Isi'].apply(remove_whitespace)
            data_result['Isi'] = data_result['Isi'].apply(remove_whitespace_multi)
            data_result['Isi'] = data_result['Isi'].apply(remove_single_char)
            data_result['Isi'] = data_result['Isi'].apply(word_tokenize_wrapper)
#             data_result['Isi'] = data_result['Isi'].apply(remove_stopwords)
            data_result['Isi'] = data_result['Isi'].agg(lambda x: ','.join(map(str, x)))
            y_pred_judul = model_clickbait.predict(tfidf_clickbait.transform(data_result['Isi'].values))
            y_pred_proba_judul = model_clickbait.predict_proba(tfidf_clickbait.transform(data_result['Isi'].values))
            y_pred_isi = model_hoax.predict(tfidf_hoax.transform(data_result['Isi'].values))
            y_pred_proba_isi = model_hoax.predict_proba(tfidf_hoax.transform(data_result['Isi'].values))
            y_pred_isi = str(y_pred_isi)
            y_pred_judul = str(y_pred_judul)
            y_pred_proba_judul = np.max(y_pred_proba_judul[0])
            y_pred_proba_judul = np.round(y_pred_proba_judul, 2)
            y_pred_proba_judul = y_pred_proba_judul * 100
            y_pred_proba_isi = np.max(y_pred_proba_isi[0])
            y_pred_proba_isi = np.round(y_pred_proba_isi, 2)
            y_pred_proba_isi = y_pred_proba_isi * 100
            if y_pred_isi[1] == '1':
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_isi) + '% Hoax'
                st.error(text_result)
            else:
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_isi) + '% Tidak Hoax'
                st.success(text_result)
            if y_pred_judul[1] == '1':
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_judul) + '% Clickbait'
                st.error(text_result)
            else:
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_judul) + '% Tidak Clickbait'
                st.success(text_result)
    elif berita == 'Liputan6':
        url = st.text_input('Masukkan link berita',
                            placeholder='Contoh : https://www.liputan6.com/bola/read/5146395/susunan-pemain-16-besar-piala-dunia-2022-maroko-vs-spanyol-matador-cadangkan-top-skor')
        submit = st.button("Submit")
        if submit:
            # Send HTTP request to the URL
            response = requests.get(url)
            # Parse the HTML response
            soup_judul = BeautifulSoup(response.text, "html.parser")
            soup_isi = BeautifulSoup(response.content, "html.parser")
            # Get the title and the text
            judul = soup_judul.find("title").text
            text = soup_isi.find_all("p")
            isi = ""
            for i in text:
                isi = isi + i.text
            result_judul = "Judul : " + str(judul)
            # Print the title and the text
            st.info(result_judul)
            ## SAVE INPUT IN DATAFRAME
            data_result = pd.DataFrame({'Judul': [judul],
                                        'Isi': [isi]})
            data_result['Judul'] = data_result['Judul'].str.lower()
            data_result['Judul'] = data_result['Judul'].apply(remove_mention)
            data_result['Judul'] = data_result['Judul'].apply(remove_hashtag)
            data_result['Judul'] = data_result['Judul'].apply(remove_https)
            data_result['Judul'] = data_result['Judul'].apply(remove_number)
            data_result['Judul'] = data_result['Judul'].apply(remove_punc)
            data_result['Judul'] = data_result['Judul'].apply(remove_whitespace)
            data_result['Judul'] = data_result['Judul'].apply(remove_whitespace_multi)
            data_result['Judul'] = data_result['Judul'].apply(remove_single_char)
            data_result['Judul'] = data_result['Judul'].apply(word_tokenize_wrapper)
#             data_result['Judul'] = data_result['Judul'].apply(remove_stopwords)
            data_result['Judul'] = data_result['Judul'].agg(lambda x: ','.join(map(str, x)))
            data_result['Isi'] = data_result['Isi'].str.lower()
            data_result['Isi'] = data_result['Isi'].apply(remove_mention)
            data_result['Isi'] = data_result['Isi'].apply(remove_hashtag)
            data_result['Isi'] = data_result['Isi'].apply(remove_https)
            data_result['Isi'] = data_result['Isi'].apply(remove_number)
            data_result['Isi'] = data_result['Isi'].apply(remove_punc)
            data_result['Isi'] = data_result['Isi'].apply(remove_whitespace)
            data_result['Isi'] = data_result['Isi'].apply(remove_whitespace_multi)
            data_result['Isi'] = data_result['Isi'].apply(remove_single_char)
            data_result['Isi'] = data_result['Isi'].apply(word_tokenize_wrapper)
#             data_result['Isi'] = data_result['Isi'].apply(remove_stopwords)
            data_result['Isi'] = data_result['Isi'].agg(lambda x: ','.join(map(str, x)))
            y_pred_judul = model_clickbait.predict(tfidf_clickbait.transform(data_result['Isi'].values))
            y_pred_proba_judul = model_clickbait.predict_proba(tfidf_clickbait.transform(data_result['Isi'].values))
            y_pred_isi = model_hoax.predict(tfidf_hoax.transform(data_result['Isi'].values))
            y_pred_proba_isi = model_hoax.predict_proba(tfidf_hoax.transform(data_result['Isi'].values))
            y_pred_isi = str(y_pred_isi)
            y_pred_judul = str(y_pred_judul)
            y_pred_proba_judul = np.max(y_pred_proba_judul[0])
            y_pred_proba_judul = np.round(y_pred_proba_judul, 2)
            y_pred_proba_judul = y_pred_proba_judul * 100
            y_pred_proba_isi = np.max(y_pred_proba_isi[0])
            y_pred_proba_isi = np.round(y_pred_proba_isi, 2)
            y_pred_proba_isi = y_pred_proba_isi * 100
            if y_pred_isi[1] == '1':
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_isi) + '% Hoax'
                st.error(text_result)
            else:
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_isi) + '% Tidak Hoax'
                st.success(text_result)
            if y_pred_judul[1] == '1':
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_judul) + '% Clickbait'
                st.error(text_result)
            else:
                text_result = 'Berita tersebut diprediksi ' + str(y_pred_proba_judul) + '% Tidak Clickbait'
                st.success(text_result)
