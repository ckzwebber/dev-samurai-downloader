# 📦 DevSamurai Downloader — Download Automático com Retomada e Multithreading

> ⚠️ **Atenção:** Os cursos da [DevSamurai](https://class.devsamurai.com.br/) foram disponibilizados gratuitamente até **dezembro de 2025**.  
> Todas as URLs e os materiais pertencem exclusivamente à **DevSamurai**.  
> Este script é apenas uma ferramenta auxiliar para facilitar o download de conteúdo **público e autorizado**.

O **DevSamurai Downloader** é um utilitário em **Python 3** para realizar o download de múltiplos arquivos de forma **confiável, rápida e paralela**, com **retomada automática de downloads interrompidos**, **barra de progresso (tqdm)** e **registro detalhado em log**.

O script foi projetado para facilitar o download de arquivos de cursos da DevSamurai (ou qualquer outra lista de URLs), diretamente para uma unidade local — como um pendrive, HD externo ou pasta do sistema.

---

## 🧭 Visão Geral

- Faz **download simultâneo** de múltiplos arquivos usando **ThreadPoolExecutor**.
- **Retoma** downloads interrompidos via cabeçalho `Range`.
- Exibe **barra de progresso** individual por arquivo e uma **barra geral** de progresso total.
- Tenta automaticamente até **3 vezes** em caso de falhas de conexão.
- Gera um **log de resultado completo** (`download_log.txt`) com sucesso ou erro de cada arquivo.
- Permite configurar facilmente o **número máximo de threads**, **timeout**, **tamanho dos chunks** e **caminho de destino**.

---

## ⚙️ Tecnologias e Bibliotecas

- **Python 3.10+**
- **requests** — para requisições HTTP com suporte a stream e cabeçalho Range
- **tqdm** — exibição de barras de progresso
- **concurrent.futures** — controle de execução concorrente
- **os / time** — manipulação de sistema de arquivos e atrasos entre tentativas

---

## 🚀 Funcionalidades Principais

| Funcionalidade                | Descrição                                                                  |
| ----------------------------- | -------------------------------------------------------------------------- |
| 🧵 **Download paralelo**      | Baixa múltiplos arquivos simultaneamente (configurável via `MAX_THREADS`). |
| 💾 **Retomada automática**    | Se o download for interrompido, ele é retomado do ponto onde parou.        |
| ⏳ **Barra de progresso**     | Mostra o progresso individual e o progresso total.                         |
| 🔁 **Tentativas automáticas** | Reexecuta até 3 vezes se o download falhar.                                |
| 📜 **Registro em log**        | Cria `download_log.txt` com o resultado detalhado de cada URL.             |
| 🧹 **Limpeza automática**     | Remove arquivos incompletos após falhas repetidas.                         |

---

## 📂 Estrutura do Projeto

```
devsamurai-downloader/
├─ downloader.py           # Script principal
├─ requirements.txt        # Dependências do projeto
└─ README.md               # Este arquivo
```

> 💡 Você pode renomear `downloader.py` como quiser (ex: `main.py` ou `devsamurai_downloader.py`).

---

## 🧰 Configuração & Uso

### 1. Clonar o repositório

```bash
git clone https://github.com/ckzwebber/dev-samurai-downloader.git
cd dev-samurai-downloader
```

### 2. Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

> O arquivo `requirements.txt` deve conter:
>
> ```txt
> requests
> tqdm
> ```

### 4. Configurar o caminho de destino

No topo do script (`PENDRIVE_PATH`), altere a linha para o diretório onde deseja salvar os arquivos:

```python
PENDRIVE_PATH = "D:/DevSamurai"
```

O script criará automaticamente a pasta caso não exista.

### 5. Executar o script

```bash
python downloader.py
```

Durante a execução, você verá barras de progresso individuais e uma barra geral indicando o andamento total.

---

## ⚙️ Parâmetros de Configuração

| Variável        | Descrição                                 | Padrão            |
| --------------- | ----------------------------------------- | ----------------- |
| `PENDRIVE_PATH` | Caminho onde os arquivos serão salvos     | `"D:/DevSamurai"` |
| `MAX_THREADS`   | Número máximo de downloads simultâneos    | `5`               |
| `RETRY_LIMIT`   | Tentativas de download antes de desistir  | `3`               |
| `TIMEOUT`       | Tempo limite (em segundos) por requisição | `60`              |
| `CHUNK_SIZE`    | Tamanho de cada parte do download (bytes) | `256 KB`          |

---

## 📋 Exemplo de Saída

```
🚀 Iniciando download de 60 arquivos...

Progresso geral:  42%|███████████████▍                     | 25/60 [00:54<00:49,  1.17s/it]
✅ Concluído: D:/DevSamurai/React - Fundamentos.zip
✅ Concluído: D:/DevSamurai/Python - Forca.zip
❌ Falhou: https://cursos.devsamurai.com.br/Linux.zip | Erro: Timeout

Todos os downloads processados! Log salvo em: D:/DevSamurai/download_log.txt
```

---

## 🧠 Dicas e Boas Práticas

- Se o servidor não suportar **requisições parciais (`Range`)**, o arquivo será refeito do zero.
- Se você for baixar muitos arquivos grandes, reduza `MAX_THREADS` para evitar bloqueios de rede.
- O log (`download_log.txt`) é sobrescrito a cada execução — salve-o antes de rodar novamente se quiser preservar o histórico.
- Para pausar o processo, pressione **Ctrl + C** — o script será interrompido de forma segura.

---

## 🧪 Testado em

- ✅ **Windows 10 / 11**
- ✅ **MacOS**
- ✅ **Python 3.10 / 3.11**
- ✅ **Conexões instáveis** (retomada validada)
- ✅ **Pendrive / SSD externo**

---

## 🤝 Contribuições

Contribuições são muito bem-vindas!  
Fluxo sugerido:

1. Faça um **fork** do repositório
2. Crie uma branch:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Faça commit das alterações:
   ```bash
   git commit -m "feat: adiciona suporte a downloads via proxy"
   ```
4. Envie sua branch e abra um **Pull Request**

---

## ⚖️ Licença

Este projeto é distribuído sob a licença **MIT**.  
Sinta-se livre para usar, modificar e compartilhar.

---

## 📞 Contato

Criado por [**Carlos Miguel**](https://www.linkedin.com/in/cmiguelwm/) —

---

### 🧩 Exemplo rápido para baixar outros arquivos

Basta substituir a lista `urls` no topo do script:

```python
urls = [
    "https://exemplo.com/arquivo1.zip",
    "https://exemplo.com/arquivo2.zip",
    ...
]
```

O script cuidará automaticamente do download paralelo, retomada e log.
