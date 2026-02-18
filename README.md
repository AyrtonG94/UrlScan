# Scanner de Diretórios Python

Este é um scanner de diretórios simples, paralelo e rápido, escrito em Python, que verifica a existência de diretórios em um host a partir de uma wordlist. Ele utiliza threads para realizar requisições simultâneas e retorna mensagens claras sobre sucesso e falhas.

---

## ⚡ Funcionalidades

- Verifica múltiplos diretórios simultaneamente usando `ThreadPoolExecutor`
- Suporte a **timeout** e tratamento de erros de conexão
- Retorno padronizado:
  - `[OK] Diretório encontrado: <url>`
  - `[ERRO][TIMEOUT] Diretório: <directory> - Timeout`
  - `[ERRO][CONEXAO] Diretório: <directory> - ConnectionError`
  - `[ERRO][HTTP] Diretório: <directory> - HTTPError`
- Permite ajustar número de threads para maior velocidade ou estabilidade
- Fácil de usar com qualquer wordlist simples em arquivo de texto

---

## 🛠 Requisitos

- Python 3.8+  
- Biblioteca `requests`  

Instalação do `requests`:

```bash
pip install requests
