boz = input('gjhgjghjgjhgjgh: ')
import smtplib
import requests
from bs4 import BeautifulSoup as bs


#Burada ALTIN verisinin cekildigi kodlar var
url = "http://bigpara.hurriyet.com.tr/altin/ceyrek-altin-fiyati/"
r = requests.get(url)
soup = bs(r.content, 'html.parser')
kurbox = soup.find_all('div', {'class' : 'kurBox'})
alis = kurbox[1]
alis_fiyat = alis.find_all('span')
alis_fiyati = alis_fiyat[1].text
# content = str('Ceyrek altin alis fiyati: ' + alis_fiyati)
satis = kurbox[2]
satis_fiyat = satis.find_all('span')
satis_fiyati = satis_fiyat[1].text


#Burada DOVIZ verisi cekildigi kodlar var
url = "http://bigpara.hurriyet.com.tr/doviz/"
r = requests.get(url)
soup = bs(r.content, 'html.parser')
dovizler = soup.find_all('span', {'class' : 'value'})
dolar_degisim = dovizler[0].text
dolar_alis = dovizler[1].text
dolar_satis = dovizler[2].text
euro_degisim = dovizler[3].text
euro_alis = dovizler[4].text
euro_satis = dovizler[5].text
sterlin_degisim = dovizler[6].text
sterlin_alis = dovizler[7].text
sterlin_satis = dovizler[8].text

#Burada HAVA DURUMU verisi cekildigi kodlar var
url = 'http://www.e-sehir.com/hava_durumu/hollanda-deventer-hava-durumu-tahmini.html'
r = requests.get(url)
soup = bs(r.content, 'html.parser')
tum_tr = soup.find_all('tr')
bugun_tr = tum_tr[1]
bugun_veri = bugun_tr.find_all('td')
bugun_tarih = bugun_veri[0].text
bugun_hava = bugun_veri[1].text
bugun_en_yuksek = bugun_veri[2].text
bugun_en_dusuk = bugun_veri[3].text
bugun_hissedilen = bugun_veri[4].text
bugun_gunes = bugun_veri[6].text


#Burada NAMAZ VAKITLERI cekildigi kodlar var.
url = ('https://www.huzursayfasi.com/namaz-vakitleri/deventer-namaz-vakitleri.html')
r = requests.get(url)
soup = bs(r.content, 'html.parser')
tumu = soup.find('table').text
imsak = tumu[30:35]
gunes = tumu[35:40]
ogle = tumu[40:45]
ikindi = tumu[45:50]
aksam = tumu[50:55]
yatsi = tumu[55:60]
tarih = soup.find('h2').text



#MAIL GONDERIMI ISLEMI ICIN GEREKLI VERILER
# Hesap bilgilerimiz
kullanici="pythoncoderrs@gmail.com"
kullanici_sifresi = 'Python-7890'
alici = 'ramazansakrs@gmail.com'            # alıcının mail adresi
konu = 'Python Daily Mail'
msj = (
'-'*40 + '\n' +  '\n' +
'Su an Ceyrek Altin alis fiyati:  ' + str(alis_fiyati) + '\n' + 
'Su an Ceyrek Altin satis fiyati:  ' + str(satis_fiyati) + '\n' + '\n' +
'-'*40 + '\n' + '\n' +
('Su an Dolar alis fiyati:  ' + str(dolar_alis)) + '\n' +
('Su an Dolar satis fiyati:  ' + str(dolar_satis)) + '\n' +
('Su an Euro alis fiyati:  ' + str(euro_alis)) + '\n' +
('Su an Euro satis fiyati:  ' + str(euro_satis)) + '\n' +
('Su an Sterlin alis fiyati:  ' + str(sterlin_alis)) + '\n' +
('Su an Sterlin satis fiyati:  ' + str(sterlin_satis)) + '\n' + '\n' +
'-'*40 +'\n' + '\n' +
(bugun_tarih + ' tarihi itibari ile Deventer\'da') + '\n' +
('') + '\n' +
('Hava durumu         : ' + bugun_hava) + '\n' +
('En yuksek sicaklik  : ' + bugun_en_yuksek) + '\n' +
('En dusuk Sicaklik   : ' + bugun_en_dusuk) + '\n' +
('Hissedilen sicaklik : ' + bugun_hissedilen) + '\n' +
('Gunes dogus-batis   : ' + bugun_gunes) + '\n' + '\n' +
'-'*40 + '\n' +
"""
{} :

Imsak   :{}
Gunes   :{}
Ogle    :{}
Ikindi  :{}
Aksam   :{}
Yatsi   :{}
""" .format(tarih,imsak, gunes, ogle,ikindi,aksam,yatsi) + '\n' +
'-'*40
)

# MAIL ICERIGI bir metinde derledik
email_text = """
From: {}
To: {}
Subject: {}
{}
""" .format(kullanici,alici, konu, msj)

email_text = email_text.replace('\u0131' , 'i')
email_text = email_text.replace('\xa0' , ' ')
email_text = email_text.replace('\xfc' , 'u')
email_text = email_text.replace('\u011f' , 'g')
email_text = email_text.replace('\xb0' , 'o')
email_text = email_text.replace('\u015f' , 's')
email_text = email_text.replace('\xfd' , 'i')
email_text = email_text.replace('\xe7' , 'c')
email_text = email_text.replace('\xf0' , 'g')
email_text = email_text.replace('\xfe' , 's')
email_text = email_text.replace('\xc7' , 'c')


"""print(email_text)
input('Bu veriler ile ' + alici + ' adresine bu maili gondermek istiyor musunuz?')"""

try:
    server = smtplib.SMTP('smtp.gmail.com:587')   #servere bağlanmak için gerekli host ve portu belirttik
    
    server.starttls() #serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
    
    server.login(kullanici, kullanici_sifresi)   # Gmail SMTP server'ına giriş yaptık
    
    server.sendmail(kullanici, alici, email_text) # Mail'imizi gönderdik 
    
    server.close()     # SMTP serverimizi kapattık
    
    print ('Email basari ile ' + alici + ' adresine gönderildi')
    
except Exception as e:
    print(e)
    print("bir hata oluştu")


"""input()"""
