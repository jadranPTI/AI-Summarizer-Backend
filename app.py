from utils.get_transcript import get_transcript
from utils.summarize import summarize_text


youtube_url = input("Enter YouTube URL: ")
language = input("Enter language for summary: ")

print("\nGetting transcript...\n")

transcript = get_transcript(youtube_url)

print("\nGenerating summary...\n")

summarize_text(transcript, language)

# print("\nSUMMARY:\n")

# print(summary.content)

