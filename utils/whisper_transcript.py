import whisper
import yt_dlp
import os

def download_audio(youtube_url):

    # Create temp folder if it doesn't exist
    os.makedirs("temp", exist_ok=True)

    output_path = "temp/audio.%(ext)s"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': False,
        'noplaylist': True, 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'extractor_args': {
            'youtube': {
                'js_runtimes': ['nodejs:C:\\Program Files\\nodejs\\node.exe']
            }
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    return "temp/audio.mp3"


def whisper_transcript(youtube_url):

    audio_path = download_audio(youtube_url)

    print("Loading Whisper model...\n")
    model = whisper.load_model("small")

    print("Transcribing audio...\n")
    result = model.transcribe(audio_path)

    # Cleanup audio file after transcription
    if os.path.exists(audio_path):
        os.remove(audio_path)

    return result["text"]





