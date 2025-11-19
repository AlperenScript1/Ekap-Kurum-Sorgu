from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from utils import center_window
from selenium import webdriver
import customtkinter as ctk
import webbrowser
import threading
import time
import re
#TODOD: Multithreading UI ve Selenium işlemleri ayrı çalışır.

ctk.set_appearance_mode("gray")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("[EKS] EKAP_Kurum_Sorgu v1.2")
app.resizable(False,False)
center_window(app, 500, 380)

#! 25DT silip sadece ID kısmını almak için.
def normalize_kurum_id(s: str) -> str:
    if not s:
        return ""
    s = s.strip()
    groups = re.findall(r"\d+", s)
    return groups[-1] if groups else ""

#! --------------------_UI_-------------------- #Front
yil_label = ctk.CTkLabel(app, text="Yıl:")
yil_label.pack(pady=(20,5))
yil_var = ctk.StringVar(value="25")
yil_option = ctk.CTkOptionMenu(app, values=["25", "24", "23", "22"], variable=yil_var)
yil_option.pack(pady=(0,10))

id_label = ctk.CTkLabel(app, text="Kurum ID:")
id_label.pack(pady=(10,5))
id_entry = ctk.CTkEntry(app)
id_entry.pack(pady=(0,10)) 


#! --------------------_SELENİUM_-------------------- #Back
def sorgula():
    yil = yil_var.get()
    kurumID_input = id_entry.get()
    kurumID = normalize_kurum_id(kurumID_input)

    if kurumID == "":
        update_label = lambda txt, color="red": app.after(0, lambda: kurum_label.configure(text=txt, text_color=color))
        update_label("ID kısmı boş bırakılamaz", "red")
        return("Null")
    
    chromedriver_autoinstaller.install();
    options = Options();
    #! bot algılama olasılığından dolayı 'headless' kullanmadım
    options.add_argument("--headless");
    options.add_argument("--window-size=1920,1080");
    options.add_argument("--window-position=-32000,-32000");
    driver = webdriver.Chrome(options=options);

    url = "https://ekap.kik.gov.tr/EKAP/YeniIhaleArama.aspx?qs=1&dt=true";
    driver.get(url);
    driver.implicitly_wait(10);

    try:
        if yil == "25":
            yil_index = "0"
        elif yil == "24":
            yil_index = "1"
        elif yil == "23":
            yil_index = "2"
        elif yil == "22":
            yil_index = "3"
        else:
            print("Yıl hatalı veya 22-25 arasında değil.")
            driver.quit()
            return

        kurum_label.configure(text="Kurum aranıyor.. \n süre uzunluğu Ekap'ın yoğunluğuna göre değişebilir.", text_color="white", font=("Helvetica", 16));
        id_entry.delete(0, ctk.END)
        driver.find_element(By.CSS_SELECTOR, "div[placeholder='Lütfen Yıl Seçiniz'] span[aria-label='Select box activate']").click()
        driver.find_element(By.CSS_SELECTOR, f"div[id='ui-select-choices-row-0-{yil_index}'] a[class='ui-select-choices-row-inner']").click()

        driver.find_element(By.CSS_SELECTOR, "input[placeholder='DT No']").send_keys(kurumID)
        driver.find_element(By.ID, "btnFilter").click()

        try:
            wait = WebDriverWait(driver, 10)
            toast_locator = (By.CSS_SELECTOR, ".alert.alert-info")
            elements = wait.until(EC.presence_of_all_elements_located(toast_locator))
            if elements:
                print("Alert:", elements[0].get_attribute("innerText"))
                
                app.after(0, lambda: kurum_label.configure(text="EKAP Sistem Mesajı: " + "Aradığınız kriterlere uygun kayıt bulunamadı. \n Lütfen Kurum id ve yılını kontrol ediniz. \n" + "ID: " + "["+ str(kurumID) + "]\n" + "Yıl: " + str(yil), text_color="red", font=("Helvetica", 16)))
        except:
            print("Hiç alert bulunamadı.");
            driver.find_element(By.CSS_SELECTOR, ".fa.fa-th").click()
            kurum = driver.find_element(By.CSS_SELECTOR, ".idareIl.ng-binding").get_attribute("innerHTML")
            print("Kurum:", kurum)
            app.after(0, lambda: kurum_label.configure(text="Kurumu: " + str(kurum)  + "\n ID: " + "["+ str(kurumID) + "]\n" + "Yıl: " + str(yil), text_color="white", font=("Helvetica", 15)));
    except Exception as e:
        print("Hata:", e)
    
    driver.quit()

#! Selenium ile etkileşimde kalır ve işlem bittiğinde butonu aktif eder.
def _set_button_state(state: str): 
    app.after(0, lambda: start_button.configure(state=state))

#? Arayüz çökmemesi için belli işlemleri devre dışı bırakır.
def start_sorgula():
    #! Selenium işlemi devam ederken butonları seçilemez yapıyoruz.
    _set_button_state("disabled")

    def worker():
        try:
            sorgula()
        finally:
                #! İşlem bittikten sonra ise tekrardan aktif hale getiriyoruz.        
            _set_button_state("normal")

    threading.Thread(target=worker, daemon=True).start()

def callback(url):
    webbrowser.open_new(url)

help_window = None

def show_help():
    global help_window
    
    if help_window is not None and help_window.winfo_exists(): #? Yardım penceresi için öncelik
        help_window.lift()
        help_window.focus()
        return
    
    help_window = ctk.CTkToplevel(app)
    help_window.title("Nasıl Kullanılır?")
    help_window.geometry("400x300")
    help_window.resizable(False, False)
    center_window(help_window, 400, 300)
    help_window.attributes('-topmost', True)
    help_window.grab_set()
    
    help_text = ctk.CTkLabel(help_window, text="Kullanım Talimatları:\n\n1. Yıl seçin (25, 24, 23, 22)\n \n2. Kurum ID girin\n   • Örnek: 1889896\n   • Veya: 25DT1889896\n\n 3. 'Sorgula' butonuna basın\n •  Sistem otomatik olarak (25DT) kaldırır.        Bu yüzden direkt ihale id olarak kolaylıkla kopyala yapıştır yapabilirsiniz.", justify="left", wraplength=300, font=("Helvetica", 16))
    help_yonlendir = ctk.CTkLabel(help_window, text="Daha fazla detay için aşağıdaki bağlantıya tıklayınız", font=("Helvetica", 16))
    help_link = ctk.CTkLabel(help_window, text="https://github.com/AlperenScript1/Ekap-Kurum-Sorgu", text_color="#0090C0", font=("Helvetica", 16), wraplength=900)
    def _open_help_link(event=None): #? Link açıldığı zaman 'Nasıl kullanılır' penceresi kapanır.
        callback("https://github.com/AlperenScript1/Ekap-Kurum-Sorgu")
        try:
            help_window.destroy()
        except Exception:
            pass

    help_link.bind("<Button-1>", _open_help_link)

    help_link.pack(side="bottom", pady=5)
    help_text.pack(pady=20, padx=20);

    close_btn = ctk.CTkButton(help_window, text="Kapat", command=help_window.destroy);
    close_btn.pack(pady=5);

byDev = ctk.CTkLabel(app, text="//Alperen (GitHub)", text_color="#0090C0", font=("Helvetica", 15));
byDev.pack(side="bottom", pady=1); 
byDev.bind("<Button-1>", lambda e: callback("https://github.com/AlperenScript1"))

start_button = ctk.CTkButton(app, text="Sorgula", command=start_sorgula)
start_button.pack(pady=1)

kurum_label = ctk.CTkLabel(app, text="Kurumu: ", font=("Helvetica", 16));
kurum_label.pack(side="bottom", pady=1)

#! Nasıl kullanılır ?
nasilKullanilir = ctk.CTkButton(app, text="Nasıl kullanılır?", command=show_help)
nasilKullanilir.pack(pady=1)

app.mainloop()
