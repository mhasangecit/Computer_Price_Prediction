import streamlit as st
import numpy as np
import joblib
import pandas as pd
from predict_costpy import predict

st.markdown('##Bilgisayar Fiyat Tahmini')  # markDown -> markdown
st.write('-----------------------')

ekran_karti_secenekleri = ["Dahili Ekran Kartı","AMD Radeon Graphics", "Intel Iris Graphics", "AMD Radeon RX 550","Intel UHD Graphics 600","Nvidia GeForce GTX 1650","Nvidia GeForce MX450","AMD Radeon RX 580","Nvidia Geforce GT 740"]
islemci_option = ["AMD Ryzen 7", "Intel Core i5", "AMD Ryzen 5","Intel Xeon","Intel Celeron","MediaTek P60T"]
i_NesilOption = ["5. Nesil", "7. Nesil", "9. Nesil","10. Nesil","11. Nesil"]
islemci_modeli_options = ["1135G7", "5700U", "X5660","4800HS"]
ram_options = [8,16,32,64]
ekran_boyutu_options = ["14 inç", "15,6 inç", "18 inç","25 + inç"]
ekran_karti_hafizasi_options = ["Paylaşımlı", "2GB", "4GB","8GB"]
ekran_karti_tipi_options = ["Dahili", "Harici"]
ekran_yenileme_hizi_options = ["60 Hz", "75 Hz", "90 Hz"]
ram_tipi_options = ["DDR4", "LPDDR4"]
ekran_karti_bellek_tipi_options = ["Dahili","GDDR5", "DDR3", "DDR", "DDR5"]
ssd_kapasitesi_options = ["32 GB", "120 GB","256 GB", "512GB"]
temel_islemci_hizi_options = [1.1,2.9,3.1,3.6]
cozunurluk_options = ["1366 x 768", "1920 x 1080", "4480 x 2520"]
islemci_cekirdek_sayisi_options = [2, 4, 6, 8,10]
isletim_sistemi_options = ["Windows","Free Dos"]



secilen_ekran_karti = st.selectbox('Ekran Kartı:', ekran_karti_secenekleri)
secilenIslemci = st.selectbox('İşlemci:', islemci_option)
secilenI_nesil = st.selectbox('İşlemci Nesli:', i_NesilOption)
secilen_islemci_modeli = st.selectbox('İşlemci Modeli:', islemci_modeli_options)
secilen_ram_sec = st.selectbox('Ram:', ram_options)
secilen_ekran_boyutu = st.selectbox('Ekran Boyutu:', ekran_boyutu_options)
secilen_ekran_karti_hafizasi = st.selectbox('Ekran Kartı Hafızası:', ekran_karti_hafizasi_options)
secilen_ekran_karti_tipi = st.selectbox('Ekran Kartı Tipi:', ekran_karti_tipi_options)
secilen_ekran_yenileme_hizi = st.selectbox('Ekran Yenileme Hızı:', ekran_yenileme_hizi_options)
secilen_ram_tipi = st.selectbox('Ram Tipi:', ram_tipi_options)
secilen_ekran_karti_bellek_tipi = st.selectbox('Ekran Kartı Bellek Tipi:', ekran_karti_bellek_tipi_options)
secilen_ssd_kapasitesi = st.selectbox('SSD Kapasitesi:', ssd_kapasitesi_options)
secilen_temel_islemci_hizi = st.selectbox('Temel İşlemci Hızı:', temel_islemci_hizi_options)
secilen_cozunurluk = st.selectbox('Çözünürlük:', cozunurluk_options)
secilen_islemci_cekirdek_sayisi = st.selectbox('İşlemci Çekirdek Sayısı:', islemci_cekirdek_sayisi_options)
secilen_isletim_sistemi = st.selectbox('İşletim Sistemi:', isletim_sistemi_options)


fiyat = predict(ekran_karti_secenekleri.index(secilen_ekran_karti), secilen_ram_sec, secilen_islemci_modeli.index(secilen_islemci_modeli),
                i_NesilOption.index(secilenI_nesil), islemci_option.index(secilenIslemci), ekran_boyutu_options.index(secilen_ekran_boyutu),
                ekran_karti_hafizasi_options.index(secilen_ekran_karti_hafizasi) , ekran_karti_tipi_options.index(secilen_ekran_karti_tipi),
                ekran_yenileme_hizi_options.index(secilen_ekran_yenileme_hizi),  ram_tipi_options.index(secilen_ram_tipi), ekran_karti_bellek_tipi_options.index(secilen_ekran_karti_bellek_tipi),
                ssd_kapasitesi_options.index(secilen_ssd_kapasitesi), temel_islemci_hizi_options.index(secilen_temel_islemci_hizi), cozunurluk_options.index(secilen_cozunurluk) ,
                secilen_islemci_cekirdek_sayisi, isletim_sistemi_options.index(secilen_isletim_sistemi) ) #x_options.index(sceilenx)
                #secilen_islemci_modeli[secilen_islemci_modeli]
st.write(f"Tahmini Fiyat: {fiyat}")
