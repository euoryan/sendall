import asyncio
from telethon import TelegramClient
from telethon.tl.types import InputPeerUser

# Suas credenciais da API
api_id = 'API ID'
api_hash = 'API HASH'

# Mensagem formatada
mensagem = (
    "Esse é um teste, desenvolvido by: euoryan\n\n"
    "Acompanhe mais informações em euoryan.com\n"
    "Seja feliz ;)"
)

async def main():
    async with TelegramClient('meu_bot', api_id, api_hash) as client:
        # Recupera todos os diálogos (contatos)
        dialogs = await client.get_dialogs()
        
        enviadas = 0
        
        for dialog in dialogs:
            try:
                # Verifica se é um usuário individual
                if hasattr(dialog.entity, 'first_name') or hasattr(dialog.entity, 'username'):
                    await client.send_message(
                        dialog.entity, 
                        mensagem, 
                        link_preview=False
                    )
                    enviadas += 1
                    print(f"Mensagem enviada para: {dialog.name}")
                    await asyncio.sleep(1)  # Pausa entre envios para evitar flood
            except Exception as e:
                print(f"Erro ao enviar para {dialog.name}: {e}")
        
        print(f"Total de mensagens enviadas: {enviadas}")

if __name__ == '__main__':
    asyncio.run(main())