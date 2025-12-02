from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/fetch")
def fetch_url(url: str = Query(..., description="URL to fetch")):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        return JSONResponse(content={"url": url, "content": text[:10000]})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
