from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from utils.whisper_transcript import whisper_transcript


def extract_video_id(url):

    parsed_url = urlparse(url)

    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    if parsed_url.hostname in ["www.youtube.com", "youtube.com", "m.youtube.com", "youtu.be"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]

    return None



def get_transcript(youtube_url):

    video_id = extract_video_id(youtube_url)

    api = YouTubeTranscriptApi()

    try:

        print("\nTrying YouTube captions...\n")

        transcript_list = api.fetch(
            video_id,
            languages=['en', 'hi']
        )

        full_transcript = ""

        for item in transcript_list:
            full_transcript += item.text + " "

        print("Captions transcript success.\n")

        return full_transcript

    except Exception as e:

        print("Captions not available.")
        print("Using Whisper...\n")

        whisper_text = whisper_transcript(youtube_url)

        return whisper_text

