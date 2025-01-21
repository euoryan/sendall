# Send All

sendall é um script simples para envio automatizado de uma mensagem padrão para todos os contatos do Telegram. Ele utiliza a biblioteca **Telethon** para facilitar a interação com a API do Telegram.

## Sobre o Projeto
Este projeto automatiza o envio de uma mensagem para todos os contatos no Telegram, tornando o processo mais eficiente e escalável. Ele foi projetado para ser simples de usar, com a possibilidade de personalizar a mensagem e configurar uma pausa entre os envios para evitar bloqueios por flood.

## Funcionalidades
- **Envio Automático:** Envia uma mensagem padrão para todos os contatos do usuário no Telegram.
- **Pausa entre Envios:** Evita problemas de flood com uma pausa configurada entre cada mensagem.
- **Relatório:** Exibe no console os contatos alcançados e possíveis erros durante o envio.

## Tecnologias
- Python (100%)
- Telethon

## Configuração
### Obtenha suas credenciais da API do Telegram:
1. Acesse [my.telegram.org](https://my.telegram.org) e crie um aplicativo para obter seu API ID e API Hash.

### Edite o código:
- Substitua as variáveis `api_id` e `api_hash` pelas credenciais do seu aplicativo.
- Ajuste a mensagem no script, se necessário.

### Instale a biblioteca necessária:
```bash
pip install telethon
```

## Como Usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/euoryan/sendall
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd sendall
   ```
3. Execute o script:
   ```bash
   python sendall.py
   ```

O script irá:
- Solicitar autenticação no Telegram (via código enviado para o número associado à conta).
- Recuperar todos os contatos.
- Enviar a mensagem para cada contato encontrado.

### Acompanhe o console para:
- Ver os contatos alcançados.
- Conferir o total de mensagens enviadas.
- Identificar possíveis erros.

<br/>

<div align="center">
Feito com ☕ e código por Ryan ;) Se gostou, deixa uma estrela pra ajudar! ⭐
</div>
