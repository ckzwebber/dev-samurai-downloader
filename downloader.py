import os
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# caminho para salvar os arquivos, aqui exemplo usando um pendrive
PENDRIVE_PATH = "D:/DevSamurai"
os.makedirs(PENDRIVE_PATH, exist_ok=True)

# lista das URLs
urls = [
    "https://cursos.devsamurai.com.br/Aulas%20ao%20Vivo.zip",
    "https://cursos.devsamurai.com.br/Backend%20-%20Dominando%20o%20NodeJS.zip",
    "https://cursos.devsamurai.com.br/Backend%20-%20Dominando%20o%20Postgres.zip",
    "https://cursos.devsamurai.com.br/Carreira%20de%20Programador.zip",
    "https://cursos.devsamurai.com.br/Flutter%20-%20Calculadora%20IMC.zip",
    "https://cursos.devsamurai.com.br/Flutter%20-%20Card%C3%A1pio%20online.zip",
    "https://cursos.devsamurai.com.br/Flutter%20-%20Fluck%20Noris.zip",
    "https://cursos.devsamurai.com.br/Flutter%20-%20Lista%20de%20Leituras.zip",
    "https://cursos.devsamurai.com.br/Flutter%20Avan%C3%A7ado.zip",
    "https://cursos.devsamurai.com.br/Flutter%20B%C3%A1sico.zip",
    "https://cursos.devsamurai.com.br/Flutter%20Snippets.zip",
    "https://cursos.devsamurai.com.br/Frontend%20-%20Bootstrap.zip",
    "https://cursos.devsamurai.com.br/Frontend%20-%20Criando%20seu%20curr%C3%ADculo.zip",
    "https://cursos.devsamurai.com.br/Frontend%20-%20Criando%20seu%20portf%C3%B3lio.zip",
    "https://cursos.devsamurai.com.br/Frontend%20-%20Formul%C3%A1rio%20de%20Cadastro.zip",
    "https://cursos.devsamurai.com.br/Frontend%20-%20Loja%20de%20Caf%C3%A9.zip",
    "https://cursos.devsamurai.com.br/Frontend%20-%20Mobile%20First.zip",
    "https://cursos.devsamurai.com.br/Frontend%20-%20Preprocessadores%20(Sass).zip",
    "https://cursos.devsamurai.com.br/Frontend%20-%20Sua%20primeira%20p%C3%A1gina%20Web.zip",
    "https://cursos.devsamurai.com.br/Full%20Stack%20-%20Food%20Commerce.zip",
    "https://cursos.devsamurai.com.br/Ionic.zip",
    "https://cursos.devsamurai.com.br/JavaScript%20-%20Gerador%20Senhas.zip",
    "https://cursos.devsamurai.com.br/JavaScript%20B%C3%A1sico%20ao%20Avan%C3%A7ado.zip",
    "https://cursos.devsamurai.com.br/Kapi%20Academy%20-%20API%20Supreme.zip",
    "https://cursos.devsamurai.com.br/Linux%20para%20Programadores.zip",
    "https://cursos.devsamurai.com.br/L%C3%B3gica%20de%20Programa%C3%A7%C3%A3o%20Avan%C3%A7ada.zip",
    "https://cursos.devsamurai.com.br/L%C3%B3gica%20de%20Programa%C3%A7%C3%A3o%20B%C3%A1sica.zip",
    "https://cursos.devsamurai.com.br/Master%20Classes.zip",
    "https://cursos.devsamurai.com.br/Minha%20Primeira%20Oportunidade.zip",
    "https://cursos.devsamurai.com.br/Minicurso%20Programar%20do%20Zero.zip",
    "https://cursos.devsamurai.com.br/Monitoria%20Aberta.zip",
    "https://cursos.devsamurai.com.br/Montando%20o%20ambiente%20Dev.zip",
    "https://cursos.devsamurai.com.br/Primeira%20Oportunidade.zip",
    "https://cursos.devsamurai.com.br/Programar%20do%20Zero%20-%20HTML.zip",
    "https://cursos.devsamurai.com.br/Programar%20do%20Zero%20-%20Jokenpo.zip",
    "https://cursos.devsamurai.com.br/Programar%20do%20Zero%20-%20Ping-Pong.zip",
    "https://cursos.devsamurai.com.br/Programar%20do%20Zero.zip",
    "https://cursos.devsamurai.com.br/Python%20-%20Forca.zip",
    "https://cursos.devsamurai.com.br/Python%20-%20Jogo%20Adivinha.zip",
    "https://cursos.devsamurai.com.br/Python%20-%20Jogo%20Cobrinha.zip",
    "https://cursos.devsamurai.com.br/Python%20-%20Juros%20Compostos.zip",
    "https://cursos.devsamurai.com.br/Python%20-%20Tabela%20Fipe.zip",
    "https://cursos.devsamurai.com.br/Python%20Avan%C3%A7ado.zip",
    "https://cursos.devsamurai.com.br/Python%20B%C3%A1sico.zip",
    "https://cursos.devsamurai.com.br/React%20-%20API%20Github.zip",
    "https://cursos.devsamurai.com.br/React%20-%20Fundamentos.zip",
    "https://cursos.devsamurai.com.br/React%20-%20Lista%20de%20Leitura.zip",
    "https://cursos.devsamurai.com.br/React%20Native%20-%20Calculadora%20IMC.zip",
    "https://cursos.devsamurai.com.br/React%20Native%20-%20Publicando%20o%20Aplicativo.zip",
    "https://cursos.devsamurai.com.br/React%20Native%20-%20Smart%20Money%20-%20Firebase.zip",
    "https://cursos.devsamurai.com.br/React%20Native%20-%20Smart%20Money%20-%20Navigation%20V5.zip",
    "https://cursos.devsamurai.com.br/React%20Native%20-%20SmartMoney%20-%20Login.zip",
    "https://cursos.devsamurai.com.br/React%20Native%20-%20SmartMoney.zip",
    "https://cursos.devsamurai.com.br/React%20Native%20-%20TODO.zip",
    "https://cursos.devsamurai.com.br/React%20Native.zip",
    "https://cursos.devsamurai.com.br/Renda%20Extra%2010x%20-%20Entrevistas.zip",
    "https://cursos.devsamurai.com.br/Renda%20Extra%2010x%20-%20Mente%20Inabal..zip",
    "https://cursos.devsamurai.com.br/Renda%20Extra%2010x%20-%20Precifica%C3%A7%C3%A3o%20de%20Sistemas.zip",
    "https://cursos.devsamurai.com.br/Renda%20Extra%2010x%20-%20Treinamento%20extra.zip",
    "https://cursos.devsamurai.com.br/Renda%20Extra%2010x.zip",
    "https://cursos.devsamurai.com.br/TypeScript%20-%20TODO%20List.zip",
    "https://cursos.devsamurai.com.br/TypeScript%20B%C3%A1sico.zip",
]

MAX_THREADS = 5
RETRY_LIMIT = 3
TIMEOUT = 60
CHUNK_SIZE = 1024 * 256  # 256 KB - mais eficiente
LOG_FILE = os.path.join(PENDRIVE_PATH, "download_log.txt")

def download_file(url):
    filename = os.path.join(PENDRIVE_PATH, url.split("/")[-1])
    attempt = 0
    success = False
    error_msg = ""

    while attempt < RETRY_LIMIT and not success:
        attempt += 1
        try:
            headers = {}
            downloaded_bytes = 0

            # verifica se já existe parte do arquivo
            if os.path.exists(filename):
                downloaded_bytes = os.path.getsize(filename)
                headers["Range"] = f"bytes={downloaded_bytes}-"

            with requests.get(url, stream=True, headers=headers, timeout=TIMEOUT) as r:
                if r.status_code == 416:
                    # arquivo já completo
                    return f"Já baixado: {filename}"

                r.raise_for_status()
                total = int(r.headers.get("content-length", 0)) + downloaded_bytes

                mode = "ab" if "Range" in headers and r.status_code == 206 else "wb"
                if mode == "wb" and os.path.exists(filename):
                    os.remove(filename)  # recomeça do zero se servidor não suporta Range

                with open(filename, mode) as f, tqdm(
                    total=total,
                    initial=downloaded_bytes,
                    unit="B",
                    unit_scale=True,
                    desc=os.path.basename(filename),
                    leave=False,
                ) as pbar:
                    for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))

            success = True

        except requests.exceptions.RequestException as e:
            error_msg = f"Tentativa {attempt}/{RETRY_LIMIT} falhou: {e}"
            time.sleep(2)  # pequeno delay antes de tentar de novo
        except Exception as e:
            error_msg = f"Erro inesperado: {e}"
            break

    if success:
        return f"✅ Concluído: {filename}"
    else:
        if os.path.exists(filename):
            os.remove(filename)  # remove arquivo incompleto
        return f"❌ Falhou: {url} | Erro: {error_msg}"


def main():
    print(f"🚀 Iniciando download de {len(urls)} arquivos...\n")

    results = []
    try:
        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            futures = {executor.submit(download_file, url): url for url in urls}
            for future in tqdm(as_completed(futures), total=len(urls), desc="Progresso geral"):
                results.append(future.result())
    except KeyboardInterrupt:
        print("\nDownload interrompido pelo usuário.")
        return

    print("\nResultado final:")
    with open(LOG_FILE, "w", encoding="utf-8") as log:
        for r in results:
            print(r)
            log.write(r + "\n")

    print(f"\nTodos os downloads processados! Log salvo em: {LOG_FILE}")


if __name__ == "__main__":
    main()
