import streamlit as st

# Menentukan nilai kolesterol dalam bahan pangan
cholesterol_values = {
    'Daging dan Unggas': {'Daging kambing': 71, 'Daging sapi': 70, 'Daging ayam': 63, 'Daging bebek': 65, 'Daging babi': 80,
                          'Daging anjing': 44.4, 'Daging kalkun': 77, 'Daging unta': 61},
    'Ikan': {'Ikan tuna': 45, 'Ikan salmon': 48, 'Ikan lele': 60, 'Ikan mujair': 55, 'Ikan tongkol': 60, 'Ikan gurame': 66,
             'Ikan patin': 39},
    'Susu dan Telur': {'Susu sapi': 250, 'Telur': 155, 'Mentega': 215, 'Yogurt': 45, 'Kuning telur': 550, 'Keju': 140},
    'Makanan lainnya': {'Sosis daging': 150, 'Hamburger': 47, 'Seblak': 121, 'Bakso': 74, 'Kebab': 79, 'Coklat': 290}
}

# Fungsi untuk menghitung kolesterol
def calculate_cholesterol(jenis_makanan, nama_makanan, bobot):
    if jenis_makanan in cholesterol_values and nama_makanan in cholesterol_values[jenis_makanan]:
        cholesterol_per_100g = cholesterol_values[jenis_makanan][nama_makanan]
        total_cholesterol = (cholesterol_per_100g / 100) * bobot
        return total_cholesterol
    else:
        return f"Tidak ada data kolesterol untuk {nama_makanan} dalam kategori {jenis_makanan}."

# Fungsi untuk evaluasi resiko kolesterol
def evaluate_risk(total_cholesterol):
    if total_cholesterol < 200:
        return "Risiko kolesterol rendah."
    elif 200 <= total_cholesterol < 240:
        return "Risiko kolesterol sedang."
    else:
        return "Risiko kolesterol tinggi."

# Bagian Depan Aplikasi
st.title('Cholesterol Calculator For Foods🥩')  

st.markdown('''Cholesterol Calculator For Foods digunakan untuk menghitung kandungan kolesterol pada makanan, 
            menyajikan data jumlah kolesterol dalam tubuh sesuai usia, serta menyajikan panduan makanan sehat.
            ☆: .｡. o(≧▽≦)o .｡.:☆''')
st.markdown('---')

# Sidebar navigation
selected = st.sidebar.radio('Menu', ['Perkenalan dan Penjelasan Singkat', 'Perhitungan Kolesterol', 'Evaluasi Risiko Kolesterol', 
                                     'Panduan Makanan Sehat'])

if selected == 'Perkenalan dan Penjelasan Singkat':
    st.markdown('KELOMPOK 7 (1E-PMIP):')
    st.write('''
    1. Kalisa Khatelya (2320532)
    2. Nayla Shafa Aulia (2320541)
    3. Selvi Wardayanti (2320555)
    4. Syifa Aprilya (2320558)
    5. Zikri (2320562)''')

    st.header('💡 Tahukah Anda??', divider='rainbow')
    st.write('''
            Bahwa sama sekali tidak ada kolesterol dalam makanan nabati apa pun, 
            termasuk sereal, buah-buahan, sayuran, dan biji-bijian? 
            Kolesterol hanya berasal dari makanan hewani🐓🐄🐟''')
    st.write('''
                Kalkulator kolesterol adalah alat yang dapat membantu kita untuk mengetahui berapa 
                banyak kolesterol dalam makanan yang kita makan. Dengan kalkulator kolesterol ini, 
                kita dapat dengan cepat menentukan asupan kolesterol harian dan melacaknya. Seseorang 
                yang berisiko terkena penyakit jantung harus menjaga konsumsi kolesterol hariannya 
                sekitar 200 mg.''')

elif selected == 'Perhitungan Kolesterol':
    st.header('Perhitungan Kolesterol', divider='rainbow')
    jenis_makanan = st.selectbox('Pilih Jenis Bahan Pangan', list(cholesterol_values.keys()))
    nama_makanan = st.selectbox('Pilih Jenis Makanan', list(cholesterol_values[jenis_makanan].keys()))
    bobot = st.number_input('Masukkan bobot yang diinginkan (gram)', min_value=1, value=100)

    if st.button('Hitung Kolesterol'):
        total_cholesterol = calculate_cholesterol(jenis_makanan, nama_makanan, bobot)
        if isinstance(total_cholesterol, str):
            st.error(total_cholesterol)
        else:
            st.success(f'Perkiraan kolesterol dalam {nama_makanan} ({bobot}g): {total_cholesterol} mg')
            st.balloons()

elif selected == 'Evaluasi Risiko Kolesterol':
    st.header('Evaluasi Risiko Kolesterol', divider='blue')
    st.write('''Menu "Evaluasi Risiko Kolesterol" digunakan untuk mengevaluasi risiko kesehatan berdasarkan tingkat kolesterol total dalam darah. Evaluasi risiko ini didasarkan pada kategori kolesterol total yang diberikan oleh American Heart Association (AHA). 
            Berikut adalah kategori risiko kolesterol menurut AHA:''')
    st.write('''
             1. Risiko Kolesterol Rendah : Kolesterol total kurang dari 200 mg/dL.
             2. Risiko Kolesterol Sedang : Kolesterol total antara 200 hingga 239 mg/dL.
             3. Risiko Kolesterol Tinggi : Kolesterol total 240 mg/dL atau lebih.
            
             Melalui menu ini, Anda dapat memasukkan nilai kolesterol total Anda dalam satuan mg/dL, lalu mengevaluasi risiko kesehatannya.
             Tujuan evaluasi risiko ini adalah untuk membantu Anda memahami tingkat kolesterol Anda dan mengambil langkah-langkah yang sesuai untuk menjaga kesehatan jantung Anda.
             Klik menu 'Panduan Makanan Sehat' untuk mengetahuinya!''')
    st.markdown('''
            | Jenis kolesterol| Total Usia kurang dari 19 tahun| Pria dewasa berusia diatas 20 tahun|Wanita dewasa berusia diatas 20 tahun|
            | --------------- | -------------------------------|------------------------------------|-------------------------------------|  
            | LDL             | < 100 mg/dL                    | <100 mg/dL                         | <100 mg/dL                          |
            | HDL             | <45 mg/dL                      | 40 mg/dL atau lebih                | 50 mg/dL atau lebih                 |
            | Non-HDL         | <120 mg/dL                     | <130 mg/dL                         | <130 mg/dL                          |
            | Total Kolesterol| <170 mg/dL                     | 125-200 mg/dL                      | 125-200 mg/dL                       |                 
            ''')
    
    total_cholesterol = st.number_input('Masukkan total kolesterol (mg/dL)', min_value=0)
    if st.button('Evaluasi Risiko'):
        risk_evaluation = evaluate_risk(total_cholesterol)
        st.success(f'Hasil evaluasi risiko: {risk_evaluation}')
        st.balloons()

elif selected == 'Panduan Makanan Sehat':
    st.header('❤️‍🩹Panduan Makanan Sehat🥦', divider='green')
    st.write('''
            1. Yuk, makan yang rendah lemak jenuh dan kolesterol, seperti buah, sayur, ikan, dan biji-bijian!
            2. Hindari makanan olahan berlemak trans dan kolesterol tinggi, seperti makanan cepat saji.
            3. Pilih camilan tinggi serat, seperti oatmeal, kacang, dan biji-bijian.
            4. Kurangi makanan manis, makanan olahan, dan minuman bergula.
            5. Tetap aktif dengan bergerak dan berolahraga secara teratur.
            6. Konsultasikan dengan dokter atau ahli gizi untuk rencana makan yang sesuai dengan kebutuhan kesehatan Anda.''')
