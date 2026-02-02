import ler_mensagem
import enviar_mensagem
from driver_manager import get_driver

driver = get_driver()
driver.get("https://web.whatsapp.com")

if __name__ == "__main__":
    input("Escaneia pf o QR_code e aperte Enter para continuar")
    enviar_mensagem.mandar_mensagem_dentro_de_uma_conversa("oi, porra")
    """ try:
        while True:
            acho = ler_mensagem.ler_mensagem_quando_alguem_enviado()
            if acho:
                enviar_mensagem.mandar_mensagem_dentro_de_uma_conversa("oi, ola tudo bem?")
    except KeyboardInterrupt:
        print("Ctrl + C foi pressionado. Realizando limpeza...") """
