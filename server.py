from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from deep_translator import GoogleTranslator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this for security in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.post("/translate")
async def translate(
    text: str = Form(...),
    source_lang: str = Form(...),
    target_lang: str = Form(...)
):
    """Translates text using Google Translator."""
    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translated_text = translator.translate(text)
        return {"translated_text": translated_text}
    except Exception as e:
        return {"error": f"Translation failed: {e}"}

# Start the server with:
# uvicorn filename:app --reload
