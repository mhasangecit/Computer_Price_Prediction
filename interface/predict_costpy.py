import joblib
import pandas as pd

def predict(ekran_karti, ram, islemci_modeli, nesil, islemci, ekran_boyutu,
            ekran_karti_hafizasi, ekran_karti_tipi, ekran_yenileme_hizi, ram_tipi,
            ekran_karti_bellek_tipi, ssd_kapasitesi, temel_islemci_hizi, cozunurluk,
            islemci_cekirdek_sayisi, isletim_sistemi):

    input_data = pd.DataFrame({
        'Ekran Kartı': [ekran_karti],
        'İşlemci': [islemci_modeli],
        'İşlemci Nesli': [nesil],
        'İşlemci Modeli': [islemci],
        'Ram': [ram],
        'Ekran Boyutu': [ekran_boyutu],
        'Ekran Kartı Bellek Tipi': [ekran_karti_bellek_tipi],
        'Ekran Kartı Hafızası': [ekran_karti_hafizasi],
        'Ekran Kartı Tipi': [ekran_karti_tipi],
        'Ekran Yenileme Hızı': [ekran_yenileme_hizi],
        'Garanti Süresi': [0],
        'Ram Tipi': [ram_tipi],
        'SSD Kapasitesi': [ssd_kapasitesi],
        'Temel İşlemci Hızı': [temel_islemci_hizi],
        'Çözünürlük': [cozunurluk],
        'İşlemci Çekirdek Sayısı': [islemci_cekirdek_sayisi],
        'İşletim Sistemi': [isletim_sistemi],
    })

    svr_model = joblib.load('svr_model.sav')

    prediction = svr_model.predict(input_data)

    return prediction[0] 
