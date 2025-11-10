# 🔎 [EKS] EKAP Kurum Sorgu Aracı

Bu Python tabanlı masaüstü uygulaması, Elektronik Kamu Alımları Platformu (EKAP) üzerinde, girilen Kurum ID ve Yıl bilgisine göre ilgili kurumu hızlıca sorgulayan otomatik bir araçtır.

Selenium otomasyonu sayesinde EKAP'ın resmi arama sayfasını arka planda (headless değil bot algılama olasılığından dolayı 'headless' kullanmadım) ziyaret ederek verileri çeker ve kullanıcı dostu bir arayüzde sunar.

✨ Özellikler

Hızlı ve Otomatik Sorgulama: Seçilen Yıl (2022-2025) ve Kurum ID'ye göre EKAP'ta otomatik arama.

Modern Arayüz: Customtkinter ile oluşturulmuş şık ve kullanımı kolay masaüstü uygulaması.

Gizli Çalışma: Selenium, Chrome tarayıcısını görünmez modda çalıştırarak kullanıcı deneyimini kesintiye uğratmaz.

Hata Yönetimi: Geçersiz veya kayıt bulunamayan durumlarda EKAP sistem mesajını doğrudan kullanıcıya iletir.

🚀 Kurulum
1. Sayfanın sağ tarafından 'Relase' kısmına tıklayınız.
  <img width="307" height="104" alt="image" src="https://github.com/user-attachments/assets/6105d703-61d5-409c-b67e-e27f291009c7" />
  
2. 'EKS-EKAP_Kurum_Sorgu.exe' tıklayınız ve inmesini bekleyiniz.
<img width="1195" height="96" alt="image" src="https://github.com/user-attachments/assets/6284b494-668c-4689-acde-090bea555390" />

3. 'İndirilenler' den uygulamayı açınız
<img width="303" height="95" alt="image" src="https://github.com/user-attachments/assets/04423788-2b1f-4eec-90e1-da2906aebbbe" />


4. Windows uyarısı 'Ek bilgi' dedikten sonra 'Yine de çalıştır' deyiniz.
   <img width="527" height="495" alt="image" src="https://github.com/user-attachments/assets/d588720b-a03a-4890-8b89-8941832b5558" />



🖥️ Kullanım

Açılan arayüzde:
<img width="500" height="412" alt="image" src="https://github.com/user-attachments/assets/59e9e10c-0441-44a5-9e38-b23ce5fe56a2" />


Sorgulama yapmak istediğiniz Yılı seçin.
<img width="178" height="197" alt="image" src="https://github.com/user-attachments/assets/fc270c96-4561-479d-89e2-b73a1026c056" />


Sorgulamak istediğiniz Kurum ID'yi (DT No) girin.
<img width="190" height="128" alt="image" src="https://github.com/user-attachments/assets/44e24d91-fe17-483e-80f4-e6e137acf0a6" />


"Sorgula" butonuna tıklayın. Sonuç, saniyeler içinde arayüzde görüntülenecektir.
<img width="386" height="285" alt="image" src="https://github.com/user-attachments/assets/bb8b9d4b-a3ed-45ea-915e-04b25321fa7a" />


