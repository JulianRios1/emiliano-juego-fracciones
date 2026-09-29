"""Servidor de "Carrera de Fracciones"."""

import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

PAGE = Path(__file__).parent / "static" / "index.html"
HTML = (
    '<!doctype html><html lang="es"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1">'
    f'</head><body>{PAGE.read_text(encoding="utf-8")}</body></html>'
)

app = FastAPI(title="Carrera de Fracciones", docs_url=None, redoc_url=None)


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    """Sirve el juego."""
    return HTML


@app.get("/health")
def health() -> dict:
    """Chequeo de salud para Docker."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
