# 🔎 [EKS] EKAP Kurum Sorgu Aracı

Bu Python tabanlı masaüstü uygulaması, Elektronik Kamu Alımları Platformu (EKAP) üzerinde, girilen Kurum ID ve Yıl bilgisine göre ilgili kurumu hızlıca sorgulayan otomatik bir araçtır.

Selenium otomasyonu sayesinde EKAP'ın resmi arama sayfasını arka planda (headless değil bot algılama olasılığından dolayı 'headless' kullanmadım) ziyaret ederek verileri çeker ve kullanıcı dostu bir arayüzde sunar.

✨ Özellikler

Hızlı ve Otomatik Sorgulama: Seçilen Yıl (2022-2025) ve Kurum ID'ye göre EKAP'ta otomatik arama.

Modern Arayüz: Customtkinter ile oluşturulmuş şık ve kullanımı kolay masaüstü uygulaması.

Gizli Çalışma: Selenium, Chrome tarayıcısını görünmez modda çalıştırarak kullanıcı deneyimini kesintiye uğratmaz.

Hata Yönetimi: Geçersiz veya kayıt bulunamayan durumlarda EKAP sistem mesajını doğrudan kullanıcıya iletir.

🚀 Kurulum

Uygulamayı çalıştırmadan önce Python'ın kurulu olduğundan emin olun. Ardından gerekli tüm kütüphaneleri (customtkinter, selenium, chromedriver-autoinstaller) tek bir komutla kurabilirsiniz:

pip install customtkinter selenium chromedriver-autoinstaller


🖥️ Kullanım

Uygulamayı indirdiğiniz dizinde terminali açın ve çalıştırın:

python main.py


Açılan arayüzde:

Sorgulama yapmak istediğiniz Yılı seçin.

Sorgulamak istediğiniz Kurum ID'yi (DT No) girin.

"Sorgula" butonuna tıklayın. Sonuç, saniyeler içinde arayüzde görüntülenecektir.
