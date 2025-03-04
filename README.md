# 🎙️ Audio Transcription with Google Gemini

This project provides a Python script that transcribes audio files using **Google Gemini API**. It takes an audio file (e.g., `.mp3`) as input and outputs a complete transcription, including optional timestamps and speaker identification.

---

## ✅ Features

- Transcribes audio files using the **Google Gemini** model.
- Supports adding timestamps every 30 seconds.
- Identifies multiple speakers (if present).
- Saves the transcription to a `.txt` file.

---

## 📦 Requirements

- Python 3.7 or higher
- Google Generative AI Python SDK (`google-generativeai`)
- `python-dotenv` to load environment variables

---

## 🔧 Installation

1. **Clone the repository and access the folder:
    ```bash
    
    git clone --branch main https://github.com/profmoisesomena/simple_audio_transcription_gemini.git --single-branch
    cd simple_audio_transcription_geminin/
    ```
3. **Create and activate a virtual environment**:
   ```bash
    sudo apt install python3.10-venv
    python3 -m venv .venv
    source .venv/bin/activate
    ```
4. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Create a `.env` file** in the project directory to store your API key:
    ```env
    GEMINI_API_KEY=your_google_gemini_api_key_here
    ```

---

## 🚀 Usage

To run the transcription script:

```bash
python3 simple_audio_transcriber_by_gemini path/to/your_audio_file.mp3
```

### Example:
```bash
python3 simple_audio_transcriber_by_gemini ./meeting_recording.mp3
```

After processing, the transcription will be saved as:
```
./meeting_recording_transcricao.txt
```

---

## ⚠️ Notes

- The script works with audio files (`mp3` recommended, but `mp4`, 'ogg' (by whatsapp), wav, etc. may work too).
- Large files may take a few minutes to process.
- Ensure your **Google Gemini API key** is valid and has the necessary permissions for content generation.
- Timestamps and speaker identification depend on the model's capabilities and may vary in accuracy.

---

## 🛠️ Configuration

You can modify the model used for transcription by changing this line in the script:
```python
transcribe_audio(args.audio_file, api_key, gemini_model='gemini-1.5-pro')
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Author

Created by Moisés Omena 
Feel free to contribute or suggest improvements!

