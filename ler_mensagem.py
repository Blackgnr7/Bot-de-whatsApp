from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

driver = webdriver.Edge()
mensagens_para_ler = int


def ler_mensagem_quando_alguem_enviado():
    print("iniciado")
    driver.get("https://web.whatsapp.com/")
    assert "WhatsApp" in driver.title
    wait = WebDriverWait(driver, 10)
    time.sleep(20)
    elemento = achar_se_tem()
    while True:
        if len(elemento) > 2:
            print("Nova mensagem")
            break
        else:
            elemento = achar_se_tem()
    elemento = elemento[2]
    print(elemento.get_attribute("aria-label"))
    mensagens_para_ler = int(
        re.search(r"\d+", elemento.get_attribute("aria-label")).group()
    )
    for i in range(4):
        elemento = elemento.find_element(By.XPATH, "..")
    print(elemento.get_attribute("class"))
    elemento.click()
    time.sleep(5)
    mensagens = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'span[dir="ltr"][data-testid="selectable-text"]')
        )
    )
    for msg in mensagens[-mensagens_para_ler:]:
        print(msg.text)
    return True


def achar_se_tem():
    while True:
        try:
            elemento = driver.find_elements(
                By.CSS_SELECTOR, 'span[aria-label*="não lida"]'
            )
            break
        except NoSuchElementException:
            time.sleep(1)
    return elemento
