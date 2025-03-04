#!/usr/bin/env python3
import os
import sys
import argparse
import google.generativeai as genai
from dotenv import load_dotenv

def transcribe_audio(audio_file_path, api_key, gemini_model):
    print(f"Transcrevendo arquivo de áudio: {audio_file_path}")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(gemini_model)
    # Verificar se o arquivo existe
    if not os.path.exists(audio_file_path):
        print(f"Erro: Arquivo de áudio não encontrado: {audio_file_path}")
        sys.exit(1)
        
    try:
        # Ler o arquivo de áudio
        with open(audio_file_path, 'rb') as f:
            audio_data = f.read()
        
        print(f"Arquivo de áudio carregado contém({len(audio_data)/1024/1024:.2f} MB)")
        print("Enviando para o Gemini para transcrição. Isso pode levar alguns minutos...")
        
        
        prompt = """
        Por favor, forneça uma transcrição completa e precisa deste áudio.
        Inclua marcações de tempo a cada 30 segundos, se possível.
        Identifique diferentes falantes se houver múltiplas pessoas falando.
        """
        
        # Gerar conteúdo com o arquivo de áudio
        response = model.generate_content(
            [
                {"mime_type": "audio/mp3", "data": audio_data},
                prompt
            ]
        )
        
        # Salvar a transcrição em um arquivo
        output_file = f"{os.path.splitext(audio_file_path)[0]}_transcricao.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"Transcrição salva em: {output_file}")
        return response.text
    
    except Exception as e:
        print(f"Erro ao transcrever áudio: {str(e)}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Transcrever arquivo de áudio usando Google Gemini')
    parser.add_argument('audio_file', help='Caminho para o arquivo de áudio a ser transcrito')
    
    args = parser.parse_args()
    load_dotenv()  # Carregar variáveis de ambiente do arquivo .env
    
    # Obter a chave da API dos argumentos ou variável de ambiente
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Erro: A chave da API do Google Gemini é necessária. Forneça-a com --api-key ou defina a variável de ambiente GEMINI_API_KEY.")
        sys.exit(1)
    
    # Transcrever o áudio
    transcribe_audio(args.audio_file, api_key, gemini_model='gemini-1.5-pro')

if __name__ == "__main__":
    main()
