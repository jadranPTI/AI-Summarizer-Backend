

SUMMARY_PROMPT = """
Summarize the following YouTube transcript in simple and easy language and in detail and return summary in {language} language. And give me the summary in maximum 400 to 500 words and every part of transcript should be defined and perfectly but should be concise.

and one more thing that is only give me the response not this type of text of formalities before summary or response "Here's a summary of the YouTube transcript in simple Roman Urdu, keeping it detailed yet concise, within the 400-500 word limit:

**Transcript Ka Khulasa (Roman Urdu Mein)**" 

Transcript:
{transcript}
"""



# a like if any other language is present then return summary in english.
# and also give me every step with its meaning and also give me the main topic of the video and also give me the title of the video if you can find it in the transcript