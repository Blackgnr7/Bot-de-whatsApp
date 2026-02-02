from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from driver_manager import get_driver
from selenium.webdriver.support import expected_conditions as EC
import pandas
import time

df = pandas.read_csv("read.csv")


def achar_button():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)
    elemento = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Enviar"]'))
    )
    time.sleep(1)
    elemento.click()
    time.sleep(2)

def enviar_pelo_arquivo_csv():
    driver = get_driver()
    for index, row in df.iterrows():
        driver.get(
            f"https://web.whatsapp.com/send/?phone={row.to_dict()['numero_de_telefone']}&text={row.to_dict()[' mensagem']}"
        )
        achar_button()


def mandar_mensagem_pelo_numero(telefone: str, mensagem: str):
    driver = get_driver()
    driver.get(f"https://web.whatsapp.com/send/?phone={telefone}&text={mensagem}")
    assert "WhatsApp" in driver.title
    achar_button()


def mandar_mensagem(mensagem: str):
    driver = get_driver()
    wait = WebDriverWait(driver, 20)
    while True:
        try:
            elemento = driver.find_elements(By.CSS_SELECTOR, 'p[dir="auto"]')
            break
        except NoSuchElementException:
            time.sleep(1)
    elemento = elemento[1]
    time.sleep(1)
    elemento.click()
    elemento.send_keys(mensagem)
    time.sleep(2)
    achar_button()


def colocar_mensagem(mensagem: str):
    driver = get_driver()
    wait = WebDriverWait(driver, 20)
    elemento = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'p[dir="auto"]')
        )
    )
    elemento = elemento[1]
    time.sleep(1)
    elemento.click()
    elemento.send_keys(mensagem)
    time.sleep(2)
