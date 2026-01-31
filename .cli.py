import ler_mensagem
import enviar_mensagem
if __name__ == "__main__":
    try:
        while True:
            acho = ler_mensagem.ler_mensagem_quando_alguem_enviado()
            if acho:
                enviar_mensagem.mandar_mensagem_dentro_de_uma_conversa("oi, ola tudo bem?")
    except KeyboardInterrupt:
        print("Ctrl + C foi pressionado. Realizando limpeza...")
