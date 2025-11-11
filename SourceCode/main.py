import customtkinter as ctk
from utils import center_window
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import threading
#TODOD: Multithreading UI ve Selenium işlemleri ayrı çalışır.

ctk.set_appearance_mode("gray")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("[EKS] EKAP_Kurum_Sorgu ")
app.resizable(False,False)
center_window(app, 500, 380)

#! --------------------_UI_-------------------- #FE
yil_label = ctk.CTkLabel(app, text="Yıl:")
yil_label.pack(pady=(20,5))
yil_var = ctk.StringVar(value="25")
yil_option = ctk.CTkOptionMenu(app, values=["25", "24", "23", "22"], variable=yil_var)
yil_option.pack(pady=(0,10))

id_label = ctk.CTkLabel(app, text="Kurum ID:")
id_label.pack(pady=(10,5))
id_entry = ctk.CTkEntry(app)
id_entry.pack(pady=(0,10)) 
 

#! --------------------_SELENİUM_-------------------- #BE
def sorgula():
    yil = yil_var.get()
    kurumID = id_entry.get()

    if kurumID == "":
        update_label = lambda txt, color="red": app.after(0, lambda: kurum_label.configure(text=txt, text_color=color))
        update_label("ID kısmı boş bırakılamaz", "red")
        return("Null")
    

    chromedriver_autoinstaller.install()
    options = Options()
    #! bot algılama olasılığından dolayı 'headless' kullanmadım
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--window-position=-32000,-32000")
    driver = webdriver.Chrome(options=options)

    url = "https://ekap.kik.gov.tr/EKAP/YeniIhaleArama.aspx?qs=1&dt=true"
    driver.get(url)
    driver.implicitly_wait(10)

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
                
                app.after(0, lambda: kurum_label.configure(text="EKAP Sistem Mesajı: " + "Aradığınız kriterlere uygun kayıt bulunamadı. \n" + "ID: " + "["+ str(kurumID) + "]\n" + "Yıl: " + str(yil), text_color="red"))
        except:
            print("Hiç alert bulunamadı.")
            driver.find_element(By.CSS_SELECTOR, ".fa.fa-th").click()
            kurum = driver.find_element(By.CSS_SELECTOR, ".idareIl.ng-binding").get_attribute("innerHTML")
            print("Kurum:", kurum)
            app.after(0, lambda: kurum_label.configure(text="Kurumu: " + str(kurum)  + "\n ID: " + "["+ str(kurumID) + "]\n" + "Yıl: " + str(yil), text_color="white"))
            

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

byDev = ctk.CTkLabel(app, text="//Alperen (GitHub)", text_color="#0090C0")
byDev.pack(side="bottom", pady=1)
byDev.bind("<Button-1>", lambda e: callback("https://github.com/AlperenScript1"))

start_button = ctk.CTkButton(app, text="Sorgula", command=start_sorgula)
start_button.pack(pady=1)

kurum_label = ctk.CTkLabel(app, text="Kurumu: ")
kurum_label.pack(side="bottom", pady=1)

app.mainloop()
