# IMPORT LIBRARY
import streamlit as st
from PIL import Image

# SET PAGE
pageicon = Image.open("aset_web/LOGO_HOAXCLICK.png")
st.set_page_config(page_title="HoaxClick Web App", page_icon=pageicon, layout="centered")

# ---- SIDEBAR ----
st.sidebar.header("Articles")

jenis_berita = st.sidebar.selectbox(
    'Pilih berita di sini',
    ('Yuk Berkenalan dengan Berita Hoax dan Clickbait!',
     'Mengenali Berita Hoax/Clickbait: Tips dan Trik untuk Menjaga Diri dari Penipuan Informasi',
     'Berita Hoax/Clickbait: Dampak Negatif dan Cara Pencegahannya',
     'Pentingnya Daya Kritis Masyarakat dalam Menangkal Berita Hoax dan Clickbait',
     'Edukasi Menyikapi Berita Hoax dan Clickbait'))

# MENAMPILKAN BERITA
if jenis_berita == 'Yuk Berkenalan dengan Berita Hoax dan Clickbait!':
    st.header('Yuk Berkenalan dengan Berita Hoax dan Clickbait!')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Pernahkah Anda mendapatkan sebuah berita yang terlihat menarik dan mengundang penasaran, namun ternyata setelah dicek lebih lanjut, beritanya tidak benar atau bahkan bersifat menyesatkan? Atau mungkin Anda pernah menemukan sebuah judul yang menjanjikan sesuatu yang menggiurkan, tapi setelah diklik ternyata hanya sekedar trik untuk menarik perhatian? Jika ya, maka Anda sudah pernah menemui dua istilah dalam dunia media sosial yang cukup populer saat ini, yaitu berita hoax dan clickbait.</div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Berita hoax adalah berita bohong atau palsu yang disebarkan dengan sengaja untuk menipu atau menyesatkan pembacanya. Berita hoax biasanya dibuat untuk mencapai tujuan tertentu, seperti menyebarkan propaganda, mempengaruhi opini publik, atau bahkan menimbulkan kepanikan di masyarakat. Berita hoax seringkali dibuat sedemikian rupa sehingga terlihat seperti berita asli dan dapat dipercaya, sehingga mudah menjebak pembaca yang tidak cermat dalam memeriksa kebenarannya.</div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Sedangkan clickbait adalah teknik pemasaran yang menggunakan judul atau headline yang menggiurkan atau menarik perhatian, tetapi tidak sejalan dengan isi atau konten dari berita tersebut. Clickbait biasanya menjanjikan sesuatu yang tidak realistis atau tidak sesuai dengan kenyataan, hanya untuk menarik perhatian dan meningkatkan jumlah klik atau trafik ke situs terkait.</div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Clickbait dan berita hoax seringkali muncul bersamaan dan saling melengkapi. Judul yang menggiurkan dari clickbait bisa memancing minat pembaca untuk membaca berita terkait, dan isi berita yang hoax dapat memperkuat opini atau pandangan yang salah di benak pembaca. Menghadapi fenomena berita hoax dan clickbait yang semakin marak di era digital ini, sebagai pembaca yang cerdas, kita perlu berhati-hati dan selalu memeriksa kebenaran sebuah berita sebelum mempercayainya atau membagikannya kepada orang lain.</div>',
        unsafe_allow_html=True)
elif jenis_berita == 'Mengenali Berita Hoax/Clickbait: Tips dan Trik untuk Menjaga Diri dari Penipuan Informasi':
    st.header('Mengenali Berita Hoax/Clickbait: Tips dan Trik untuk Menjaga Diri dari Penipuan Informasi')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Berita hoax/clickbait telah menjadi masalah yang semakin mengkhawatirkan di era digital saat ini. Berita-berita yang tidak benar atau yang dibuat hanya untuk menarik perhatian sering kali disebarkan di media sosial dan dapat menimbulkan kerugian baik secara materiil maupun non-materiil. Oleh karena itu, penting bagi kita semua untuk dapat mengenali berita hoax/clickbait dan menjaga diri dari terjebak oleh penipuan informasi. Berikut adalah beberapa tips dan trik yang dapat Anda gunakan untuk mengenali berita hoax/clickbait: </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Periksa sumber berita. Pastikan bahwa berita yang Anda baca berasal dari sumber yang terpercaya dan memiliki reputasi baik. Jangan percaya pada berita yang tidak memiliki sumber atau yang berasal dari situs-situs yang tidak dapat diandalkan.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Cari tahu tanggal terbit. Jika sebuah berita sudah lama diterbitkan, maka kemungkinan besar berita tersebut sudah tidak relevan lagi. Jadi, pastikan untuk memeriksa tanggal terbit berita sebelum mempercayainya.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Periksa fakta-fakta yang disajikan. Banyak berita hoax/clickbait yang menyajikan fakta-fakta yang tidak benar atau yang tidak lengkap. Jadi, pastikan untuk memeriksa kebenaran fakta-fakta yang disajikan dalam sebuah berita dengan mencari informasi dari sumber-sumber yang terpercaya.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Berhati-hati dengan judul yang menyesatkan. Banyak berita hoax/clickbait yang menggunakan judul yang menyesatkan untuk menarik perhatian. Jadi, pastikan untuk tidak terlalu terpengaruh oleh judul saja dan baca seluruh berita sebelum memutuskan apakah berita tersebut benar atau tidak.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Waspada dengan berita yang terlalu menggoda. Banyak berita hoax/clickbait yang menjanjikan hadiah atau keuntungan besar jika kita melakukan suatu tindakan tertentu, seperti mengklik link tertentu atau membagikan berita tersebut ke teman-teman kita. Jadi, pastikan untuk tidak terlalu tergoda oleh janji-janji yang terlalu menggoda dan selalu berhati-hati dengan berita seperti ini.</li> </ul></div>',
        unsafe_allow_html=True)

elif jenis_berita == 'Berita Hoax/Clickbait: Dampak Negatif dan Cara Pencegahannya':
    st.header('Berita Hoax/Clickbait: Dampak Negatif dan Cara Pencegahannya')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Berita hoax/clickbait adalah salah satu ancaman yang sering dihadapi saat ini, terutama di era informasi yang cepat berkembang seperti saat ini. Berita hoax/clickbait sering dibuat dengan tujuan untuk menipu atau menyesatkan pembaca, dan bisa berpotensi menimbulkan kerugian baik secara materiil maupun non-materiil. Oleh karena itu, penting bagi kita untuk mengetahui dampak negatif dari berita hoax/clickbait dan cara pencegahannya. Dampak negatif dari berita hoax/clickbait dapat berupa: </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Penyebaran informasi yang tidak benar. Berita hoax/clickbait seringkali mengandung informasi yang tidak benar atau bahkan bertentangan dengan fakta. Penyebaran informasi yang tidak benar dapat menimbulkan kerugian baik bagi individu maupun masyarakat secara keseluruhan.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Penipuan. Berita hoax/clickbait seringkali digunakan oleh para penipu untuk mengelabui pembaca dan menarik uang atau informasi pribadi dari mereka. Penipuan ini bisa menimbulkan kerugian materiil bagi korban penipuan.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Penyebaran hoax yang berbahaya. Berita hoax/clickbait yang mengandung informasi yang berbahaya, seperti tentang kesehatan atau keamanan, dapat menyebabkan kerugian yang lebih besar lagi. Misalnya, berita hoax tentang obat yang menyembuhkan COVID-19 dapat menyebabkan orang tidak mempercayai vaksin yang telah teruji dan terbukti aman, sehingga meningkatkan risiko penularan virus.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Untuk mengurangi dampak negatif dari berita hoax/clickbait, berikut adalah beberapa cara yang dapat Anda lakukan:  </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Teliti sumber berita. Pastikan bahwa sumber berita yang Anda baca terpercaya dan dapat diandalkan. Hindari membaca berita dari sumber yang tidak jelas atau tidak terverifikasi.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Teliti judul berita. Judul yang menggunakan kalimat provokatif atau sensationalistik seringkali merupakan tanda-tanda dari berita hoax/clickbait. Jadi, selalu periksa kembali judul berita sebelum membacanya lebih lanjut.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Teliti tanggal publikasi. Berita hoax/clickbait seringkali dibuat dengan mengambil berita lama dan memberikan judul yang menyesatkan, sehingga terlihat seolah-olah berita tersebut baru saja terjadi. Jadi, selalu periksa tanggal publikasi berita untuk memastikan bahwa berita tersebut benar-benar baru.</li> </ul></div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%;"> <ul> <li>Teliti konten berita.</li> </ul></div>',
        unsafe_allow_html=True)

elif jenis_berita == 'Pentingnya Daya Kritis Masyarakat dalam Menangkal Berita Hoax dan Clickbait':
    st.header('Pentingnya Daya Kritis Masyarakat dalam Menangkal Berita Hoax dan Clickbait')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Masyarakat yang memiliki daya kritis tinggi merupakan aset penting dalam menangkal berita hoax dan clickbait. Hal ini dikarenakan, tingkat kecerdasan seseorang dalam memilih dan memeriksa kebenaran sebuah berita akan sangat mempengaruhi kemampuannya dalam menghadapi informasi yang tidak benar atau bersifat menyesatkan. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Daya kritis adalah kemampuan seseorang untuk mempertanyakan, menganalisis, dan mengevaluasi suatu informasi secara kritis sebelum mempercayainya atau memutuskan sesuatu berdasarkan informasi tersebut. Daya kritis ini sangat penting karena dapat membantu kita menghindari terjebak dalam berita hoax atau clickbait, serta dapat membantu kita dalam membuat keputusan yang tepat dan bijaksana. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Untuk meningkatkan daya kritis masyarakat, kita perlu terus belajar dan membiasakan diri untuk selalu memperiksa kebenaran sebuah informasi sebelum mempercayainya. Kita juga perlu mempertanyakan sumber berita, memverifikasi fakta yang ada, dan mencari informasi dari sumber lain yang lebih terpercaya. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Selain itu, pemerintah juga perlu turut serta dalam membantu masyarakat dalam meningkatkan daya kritisnya. Pemerintah dapat melakukan hal-hal seperti memberikan edukasi tentang media literacy, menyediakan fasilitas untuk memverifikasi kebenaran sebuah berita, dan menindak tegas pelaku-pelaku berita hoax atau clickbait. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Dengan demikian, daya kritis masyarakat yang tinggi akan menjadi senjata paling ampuh dalam menangkal berita hoax dan clickbait, sehingga masyarakat dapat terhindar dari informasi yang tidak benar atau menyesatkan, dan dapat membuat keputusan yang tepat dan bijaksana. </div>',
        unsafe_allow_html=True)

elif jenis_berita == "Edukasi Menyikapi Berita Hoax dan Clickbait":
    st.header('Edukasi Menyikapi Berita Hoax dan Clickbait')
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Edukasi mengenai bagaimana menyikapi berita hoax dan clickbait sangat penting untuk dilakukan di tengah masyarakat. Hal ini dikarenakan, fenomena berita hoax dan clickbait semakin marak di era digital ini, sehingga masyarakat perlu diberikan pengetahuan dan keterampilan untuk dapat menghindari dan menangkal berita-berita tersebut. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Untuk memberikan edukasi mengenai berita hoax dan clickbait, kita perlu memahami terlebih dahulu apa itu berita hoax dan clickbait. Berita hoax adalah berita bohong atau palsu yang disebarkan dengan sengaja untuk menipu atau menyesatkan pembacanya. Sedangkan clickbait adalah teknik pemasaran yang menggunakan judul atau headline yang menggiurkan atau menarik perhatian, tetapi tidak sejalan dengan isi atau konten dari berita tersebut. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Setelah memahami apa itu berita hoax dan clickbait, kita perlu memberikan edukasi tentang cara menghindari dan menangkal berita-berita tersebut. Kita dapat memberikan tips seperti memeriksa kebenaran sebuah berita sebelum mempercayainya atau membagikannya, memverifikasi fakta yang ada di dalamnya, dan mencari informasi dari sumber lain yang lebih terpercaya. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Selain itu, edukasi juga perlu diberikan tentang pentingnya daya kritis masyarakat dalam menangkal berita hoax dan clickbait. Daya kritis adalah kemampuan seseorang untuk mempertanyakan, menganalisis, dan mengevaluasi suatu informasi secara kritis sebelum mempercayainya atau memutuskan sesuatu berdasarkan informasi tersebut. Dengan memiliki daya kritis yang tinggi, masyarakat akan lebih mudah dalam menghindari dan menangkal berita hoax dan clickbait. </div>',
        unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Melalui edukasi yang tepat, diharapkan masyarakat dapat lebih waspada dan cerdas dalam menyikapi berita hoax dan clickbait, sehingga dapat terhindar dari informasi yang tidak benar atau menyesatkan, dan dapat membuat keputusan yang tepat dan bijaksana. </div>',
        unsafe_allow_html=True)