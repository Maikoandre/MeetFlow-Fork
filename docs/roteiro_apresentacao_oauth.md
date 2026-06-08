# Roteiro de Apresentação Prática: Fluxo OAuth2 no MeetFlow

Este roteiro guiará você passo a passo em uma demonstração prática do funcionamento do fluxo OAuth2 no sistema **MeetFlow** durante a apresentação do trabalho. Você fará requisições manuais para mostrar o que acontece "por baixo dos panos" quando o aplicativo Flutter se autentica na API Django.

---

## 🧭 Visão Geral do Fluxo Utilizado
O projeto utiliza o fluxo **Resource Owner Password Credentials Grant** (fluxo de senha) do OAuth2, implementado com o **Django OAuth Toolkit (DOT)**. É o fluxo ideal para aplicações móveis próprias de alta confiabilidade, onde o próprio aplicativo coleta as credenciais e as envia de forma segura para o servidor em troca de um token de acesso (`access_token`) e um token de atualização (`refresh_token`).

---

## 🛠️ Passo 1: O Setup da Aplicação OAuth
Primeiro, mostre como o Django está configurado para reconhecer o aplicativo móvel como um cliente válido.

1. **Gere/Garanta a configuração da aplicação:**
   No terminal, execute o comando de setup do OAuth (caso use Docker, use o primeiro comando; caso use localmente, o segundo):
   ```bash
   # Usando Docker:
   docker compose exec web python manage.py setup_oauth

   # Executando direto na máquina local:
   python manage.py setup_oauth
   ```
   *O que explicar:* Esse comando cria um registro de aplicação do tipo **Public** com o ID `meetflow-mobile-client` e com a concessão do tipo `password`.

2. **Demonstre no Painel de Administração (Django Admin):**
   * Acesse `http://localhost:8000/admin/` no navegador.
   * Faça login com seu superusuário (crie um com `python manage.py createsuperuser` se necessário).
   * Navegue até **Django OAuth Toolkit > Applications**.
   * Abra a aplicação **MeetFlow Mobile App** e mostre as configurações na tela (Client ID, Client Type, Authorization Grant Type).

---

## 🔑 Passo 2: Requisição Manual de Tokens (Login)
Demonstre a troca direta de usuário/senha pelos tokens OAuth2 usando o terminal (`curl`) or ferramentas como Postman/Insomnia.

> **Importante:** Substitua `seu_usuario` e `sua_senha` por credenciais válidas cadastradas no banco de dados.

Execute a seguinte requisição POST para o endpoint `/o/token/`:
```bash
curl -X POST http://localhost:8000/o/token/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=password" \
  -d "username=seu_usuario" \
  -d "password=sua_senha" \
  -d "client_id=meetflow-mobile-client"
```

### 📥 Resposta Esperada (Sucesso - HTTP 200)
Explique o significado de cada campo retornado no JSON:
```json
{
  "access_token": "gR23...yT49",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "read write",
  "refresh_token": "mK78...pL02"
}
```
* **`access_token`**: O token que dá direito a acessar as rotas protegidas da API.
* **`expires_in`**: O tempo de validade do token de acesso em segundos (geralmente 10 horas).
* **`refresh_token`**: O token que será guardado no celular para renovar o acesso sem pedir a senha novamente.

---

## 🔒 Passo 3: Acesso Protegido a Recursos da API
Mostre a segurança em ação tentando acessar a rota do perfil do usuário logado (`/api/users/me/`).

### Cenário A: Acesso Sem Token (Bloqueado)
Faça a requisição direta sem nenhum cabeçalho de autenticação:
```bash
curl -i -X GET http://localhost:8000/api/users/me/
```
*   **Resultado:** Você receberá um erro **HTTP 401 Unauthorized** com a mensagem `"Authentication credentials were not provided."`.
*   *O que explicar:* Isso mostra que a API está protegida e exige autenticação ativa.

### Cenário B: Acesso Com Token (Autorizado)
Adicione o token recebido no Passo 2 como um cabeçalho `Authorization: Bearer <access_token>`:
```bash
curl -X GET http://localhost:8000/api/users/me/ \
  -H "Authorization: Bearer gR23...yT49"
```
*   **Resultado:** Sucesso (**HTTP 200 OK**), retornando os dados do perfil do usuário autenticado no formato JSON.

---

## 🔄 Passo 4: O Fluxo de Refresh Token (Renovação Silenciosa)
Explique que o token de acesso tem um tempo curto de expiração por motivos de segurança. Demonstre como o app renova o acesso em segundo plano usando apenas o `refresh_token`, sem incomodar o usuário para digitar a senha novamente.

Execute a seguinte requisição:
```bash
curl -X POST http://localhost:8000/o/token/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=mK78...pL02" \
  -d "client_id=meetflow-mobile-client"
```
*   **Resultado:** O servidor invalida o antigo e gera um novo par de `access_token` e `refresh_token`.

---

## 📱 Passo 5: Onde isso acontece no Flutter? (Código do Cliente)
Para fechar com chave de ouro, mostre rapidamente no editor de código onde essa lógica está implementada de forma automática no app Flutter:

1.  **[login_viewmodel.dart](file:///home/maiko/Projects/MeetFlow-Fork/client/lib/viewmodels/login_viewmodel.dart):**
    *   Mostre a função `login()`, onde os parâmetros de form-urlencoded (`grant_type`, `client_id`, `username`, `password`) são montados e enviados à API, e os tokens recebidos são persistidos com segurança.
2.  **[api_service.dart](file:///home/maiko/Projects/MeetFlow-Fork/client/lib/services/api_service.dart):**
    *   Aponte o interceptador `onRequest` onde o cabeçalho `Authorization: Bearer <token>` é adicionado automaticamente a todas as requisições futuras.
    *   Aponte o interceptador `onError` onde o erro `401 Unauthorized` é tratado. Se o token expirou, o app dispara silenciosamente a chamada de `refresh_token`, salva as novas chaves, e tenta re-executar a requisição original de forma transparente para o usuário final.
