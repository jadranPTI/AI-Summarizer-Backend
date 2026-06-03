import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.summary_prompt import SUMMARY_PROMPT

load_dotenv()


def summarize_text(transcript, language):

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt = SUMMARY_PROMPT.format(
        transcript=transcript,
        language=language
    )

    full_summary = ""

    # for chunk in llm.stream(prompt):
    #     text = chunk.content                   
    #     print(text, end="", flush=True)       
    #     full_summary += text                   

    # print()                                   

    # return full_summary 

    for chunk in llm.stream(prompt):
        yield chunk.content
        print(chunk.content, end="", flush=True)

    # for chunk in response:
    #     print(chunk, end="", flush=True)

    # return chunk.content