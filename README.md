# Send All

## Sobre o Projeto

**sendall** é um script simples para envio automatizado de uma mensagem padrão para todos os contatos do Telegram. Ele utiliza a biblioteca Telethon para facilitar a interação com a API do Telegram.

## Funcionalidades

- **Envio Automático**: Envia uma mensagem padrão para todos os contatos do usuário no Telegram.
- **Pausa entre Envios**: Evita problemas de flood com uma pausa configurada entre cada mensagem.
- **Relatório**: Exibe no console os contatos alcançados e possíveis erros durante o envio.

## Configuração

1. **Obtenha suas credenciais da API do Telegram**:
   - Acesse [my.telegram.org](https://my.telegram.org/) e crie um aplicativo para obter seu `API ID` e `API Hash`.

2. **Edite o código**:
   - Substitua as variáveis `api_id` e `api_hash` pelas credenciais do seu aplicativo.
   - Ajuste a mensagem no script, se necessário.

3. **Instale a biblioteca necessária**:
   ```bash
   pip install telethon
   ```

## Como Usar

1. Execute o script:
   ```bash
   python sendall.py
   ```

2. O script irá:
   - Solicitar autenticação no Telegram (via código enviado para o número associado à conta).
   - Recuperar todos os contatos.
   - Enviar a mensagem para cada contato encontrado.

3. Acompanhe o console para:
   - Ver os contatos alcançados.
   - Conferir o total de mensagens enviadas.
   - Identificar possíveis erros.

---

<br/>

<div align="center">

Feito com ☕ e código por Ryan ;) Se gostou, deixa uma estrela pra ajudar! ⭐

</div>