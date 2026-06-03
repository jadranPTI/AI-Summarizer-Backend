from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.get_transcript import get_transcript
from utils.summarize import summarize_text

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SummarizeRequest(BaseModel):
    youtube_url: str
    language: str


@app.post("/summarize")
def summarize(request: SummarizeRequest):

    transcript = get_transcript(request.youtube_url)

    return StreamingResponse(
        summarize_text(transcript, request.language),
        media_type="text/plain"
    )









# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# from pydantic import BaseModel
# from utils.get_transcript import get_transcript
# from utils.summarize import summarize_text

# app = FastAPI()


# # Request body model
# class SummarizeRequest(BaseModel):
#     youtube_url: str
#     language: str


# # Normal response endpoint  
# @app.post("/summarize")
# def summarize(request: SummarizeRequest):

#     transcript = get_transcript(request.youtube_url)
#     summary = summarize_text(transcript, request.language)

#     return {
#         "youtube_url": request.youtube_url,
#         "language": request.language,
#         "summary": summary
#     }


# # Streaming response endpoint
# @app.post("/summarize/stream")
# def summarize_stream(request: SummarizeRequest):

#     transcript = get_transcript(request.youtube_url)

#     def stream_summary():
#         from langchain_google_genai import ChatGoogleGenerativeAI
#         from prompts.summary_prompt import SUMMARY_PROMPT
#         import os
#         from dotenv import load_dotenv
#         load_dotenv()

#         llm = ChatGoogleGenerativeAI(
#             model="gemini-2.5-flash-lite",
#             google_api_key=os.getenv("GEMINI_API_KEY")
#         )

#         prompt = SUMMARY_PROMPT.format(
#             transcript=transcript,
#             language=request.language
#         )

#         for chunk in llm.stream(prompt):
#             yield chunk.content

#     return StreamingResponse(stream_summary(), media_type="text/plain")


# # Health check endpoint
# @app.get("/")
# def health_check():
#     return {"status": "AI Summarizer API is running"}







# from fastapi import FastAPI
# from pydantic import BaseModel
# from utils.get_transcript import get_transcript
# from utils.summarize import summarize_text

# app = FastAPI()


# class SummarizeRequest(BaseModel):
#     youtube_url: str
#     language: str


# @app.post("/summarize")
# def summarize(request: SummarizeRequest):

#     transcript = get_transcript(request.youtube_url)
#     summary = summarize_text(transcript, request.language)

#     return {"summary": summary}