import argparse
import concurrent.futures
import requests
parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, required=True)
parser.add_argument('--list', required=True)
args = parser.parse_args()

def url_scan(url: str, directory: str):
    try:
        req = requests.get(f'{url}/{directory}',timeout=2)
        req.raise_for_status()
        if req.status_code == 200:
            return f"[OK] Diretório encontrado: {req.url}"
    except requests.exceptions.Timeout as erro:
        return f"[ERRO] [TIMEOUT] Diretório: {directory} -  {erro}"
    except requests.exceptions.ConnectionError as erro:
        return f"[ERRO] [CONEXAO] Diretório: {directory} -  {erro}"
    except requests.exceptions.HTTPError as erro:
        return f"[ERRO] [HTTP] Diretório: {directory} - {erro}"
    except requests.exceptions.RequestException as erro:
        return f"[ERRO] [REQUISIÇÃO] {directory} -  {erro}"

try:
    with open(f'{args.list}', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
except FileNotFoundError:
    exit(f'Arquivo não encontrado: {args.list}')



with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    result = executor.map(url_scan, [args.host] * len(lines), lines)
    for i in result:
        if i is not None:
            print(i)
