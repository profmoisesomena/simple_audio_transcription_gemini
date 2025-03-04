# YouTube Transcription com Google Gemini

Este script permite baixar vídeos do YouTube, extrair o áudio e gerar transcrições usando a API do Google Gemini, em vez do OpenAI Whisper.

## Requisitos

- Python 3.6+
- Bibliotecas Python:
  - yt-dlp
  - google-generativeai
  - python-dotenv
- FFmpeg (dependência do sistema)
- Chave de API do Google Gemini

## Instalação

1. Clone este repositório ou baixe os arquivos

2. Instale as dependências Python:
   ```
   pip install -r requirements.txt
   ```

3. Instale o FFmpeg:
   - **Ubuntu/Debian**: `sudo apt update && sudo apt install ffmpeg`
   - **Windows**: Baixe do [site oficial](https://ffmpeg.org/download.html) ou use o Chocolatey: `choco install ffmpeg`
   - **macOS**: `brew install ffmpeg`

4. Obtenha uma chave de API do Google Gemini:
   - Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Crie uma chave de API
   - Guarde a chave para usar com o script

## Uso

### Método 1: Definir a chave de API em um arquivo .env

Crie um arquivo `.env` com o seguinte conteúdo:
```
GEMINI_API_KEY=sua_chave_api_aqui
```

Depois execute o script:
```
python youtube_transcription_gemini.py https://www.youtube.com/watch?v=ID_DO_VIDEO
```

### Método 2: Definir a chave de API como variável de ambiente

```bash
# Linux/macOS
export GEMINI_API_KEY="sua_chave_api_aqui"

# Windows (PowerShell)
$env:GEMINI_API_KEY="sua_chave_api_aqui"
```

Depois execute o script:
```
python youtube_transcription_gemini.py https://www.youtube.com/watch?v=ID_DO_VIDEO
```

### Método 3: Passar a chave de API como argumento

```
python youtube_transcription_gemini.py https://www.youtube.com/watch?v=ID_DO_VIDEO --api-key "sua_chave_api_aqui"
```

### Opções adicionais

- `--output ARQUIVO`: Especifica o arquivo de saída para a transcrição
- `--keep-audio`: Mantém o arquivo de áudio após a transcrição (por padrão, o áudio é removido)

Exemplo:
```
python youtube_transcription_gemini.py https://www.youtube.com/watch?v=ID_DO_VIDEO --output minha_transcricao.txt --keep-audio
```

## Como funciona

1. O script baixa o vídeo do YouTube usando a biblioteca yt-dlp (mais robusta que pytube)
2. Extrai o áudio do vídeo e converte para MP3
3. Envia o áudio para a API do Google Gemini para transcrição
4. Salva a transcrição em um arquivo de texto

## Diferenças em relação ao OpenAI Whisper

- Usa a API do Google Gemini em vez do modelo Whisper da OpenAI
- Não requer instalação de modelos grandes localmente
- Requer uma chave de API do Google
- Pode incluir marcações de tempo e identificação de falantes automaticamente
# simple_audio_transcription_gemini
