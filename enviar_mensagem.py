from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas
import time

df = pandas.read_csv("read.csv")
driver = webdriver.Edge()
wait = WebDriverWait(driver, 20)

def enviar_quandor_achar_button():
    elemento = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'button[aria-label="Enviar"]')
        )
    )
    time.sleep(1)
    elemento.click()
    time.sleep(2)

def enviar_pelo_arquivo_csv():
    for index, row in df.iterrows():
        driver.get(
            f"https://web.whatsapp.com/send/?phone={row.to_dict()['numero_de_telefone']}&text={row.to_dict()[' mensagem']}"
        )
        enviar_quandor_achar_button()

def qualquer_numero_quiser(telefone: str, mensagem: str):
    driver.get(f"https://web.whatsapp.com/send/?phone={telefone}&text={mensagem}")
    assert "WhatsApp" in driver.title
    enviar_quandor_achar_button()

def mandar_mensagem_dentro_de_uma_conversa(mensagem: str):
    elemento = wait.until(EC.presence_of_all_elements_located(By.CSS_SELECTOR, ""))
    elemento = elemento[1]
    time.sleep(1)
    elemento.click()
    elemento.send_keys(mensagem)
    time.sleep(2)
    enviar_quandor_achar_button()

def colocar_mensagem(mensagem: str):
    elemento = wait.until(EC.presence_of_all_elements_located(By.CSS_SELECTOR, 'p[dir="auto"]'))
    elemento = elemento[1]
    time.sleep(1)
    elemento.click()
    elemento.send_keys(mensagem)
    time.sleep(2)