import streamlit as st
from PIL import Image

# SET PAGE
pageicon = Image.open("aset_web/LOGO_HOAXCLICK.png")
st.set_page_config(page_title="HoaxClick Web App", page_icon=pageicon, layout="centered")

# SET TITLE AND LOGO IMAGE
intro_col_left, intro_col_mid, intro_col_right = st.columns([1.5,6,0.5])
intro_col_mid.image('aset_web/LOGO_HOAXCLICK.png')
st.markdown('<div style="text-align: justify; font-size:250%"> <b>Web App Dashboard dan Klasifikasi Berita Hoax & Clickbait </b> </div>',
            unsafe_allow_html=True)

# DESCRIPTION
st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> Web App ini merupakan suatu aplikasi web di mana kita bisa mengklasifikasikan suatu berita apakah berita tersebut tergolong ke berita <i>hoax</i> maupun <i>clickbait</i>. Tidak hanya itu, aplikasi web ini juga memiliki fitur artikel dan <i>dashboard</i> yang diharapkan dapat menambah wawasan pengguna mengenai berita <i>hoax</i> dan <i>clickbait</i>. </div>',
            unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> <b>HoaxClick</b> merupakan kependekan dari <b>Hoax & Clickbait Classification with Dashboard Web App</b>. Dengan adanya <i>Web App</i> ini, kami punya harapan agar masyarakat Indonesia bisa jauh lebih cerdas dan selektif dalam mengenali berita <i>hoax</i> dan <i>clickbait</i></div>',
            unsafe_allow_html=True)

# ANGGOTA TIM
st.write('####')
st.write('## Anggota Tim :')

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns([4,1,4])

foto_adam = Image.open('aset_foto/foto_adam.jpeg').resize((400,400))
foto_grei = Image.open('aset_foto/foto_greiva.jpg').resize((400,400))
foto_ratu = Image.open('aset_foto/foto_ratu.jpeg').resize((400,400))
foto_anis = Image.open('aset_foto/foto_anis.jpeg').resize((300,300))
foto_kiki = Image.open('aset_foto/foto_kiki.jpg').resize((300,300))

# For columns 1 : Introduce Greiva Viandra Zahrani
col1.write('### Greiva Viandra Zahrani')
col1.image(foto_grei, caption = "162012133045")

# For columns 2 : Introduce Adam Maurizio Winata
col2.write('### Adam Maurizio Winata')
col2.image(foto_adam, caption = "162012133053")

# For columns 3 : Introduce Ratu
col3.write("### Qothrotunnidha' Almaulidiyah")
col3.image(foto_ratu, caption = "162012133093")

# For columns 4 : Introduce Anis
col4.write('### Anisyaul Fitria')
col4.image(foto_anis, caption = "162012133007")

# For columns 5 : Introduce Kiki
col6.write('### Kiki Triwidiyanti')
col6.image(foto_kiki, caption = "162012133003")