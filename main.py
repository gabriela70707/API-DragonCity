from fastapi import FastAPI
from core.configs import settings
from fastapi.middleware.cors import CORSMiddleware
from api.v1.api import api_router

#Importações para permitir que o navegador consiga puxar as imagens estaticas(as que vieram dos uploads)
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="API do Dragon City")

origin = ["http://localhost", "http://localhost:8080", "http://127.0.0.1:5500"]

app.add_middleware(CORSMiddleware, allow_origins=origin, allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)

app.include_router(api_router, prefix=settings.API_V1_STR)

# Monta a pasta "media" como arquivos estáticos
app.mount("/media", StaticFiles(directory="media"), name="media")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)