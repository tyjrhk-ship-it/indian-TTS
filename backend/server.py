from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Indian TTS Backend is Running!"
    }
