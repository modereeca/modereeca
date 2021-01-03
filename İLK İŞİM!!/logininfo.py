from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
url = "https://www.denizpazari.com/kategori.asp?balikciteknesi=3&suratteknesi=4&hizmetteknesi=16&fibertekne=12&ahsaptekne=13&fiyat=&parabirimi=&govde=&boy1=&boy2=&en1=&en2=&derinlik1=&derinlik2=&kabinadedi=&motoradedi=&yakittipi="
browser.get(url)
ilanlar = browser.find_elements_by_class_name("ilan")
for ilan in ilanlar:
    ilan.click()
    isim = browser.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/div[3]/table[2]/tbody/tr[1]/td")
    gsm = browser.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/div[3]/table[2]/tbody/tr[2]/td[2]")
    istelefonu = browser.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/div[3]/table[2]/tbody/tr[3]/td[2]")
    sehir = browser.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/div[3]/table[2]/tbody/tr[4]/td[2]")
    print("İsim:",isim.text)
    print("Cep :",gsm.text)
    print("İş Telefonu:",istelefonu.text)
    print("Şehir:",sehir.text)
    browser.back()

browser.close()

