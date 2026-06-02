from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import Response
import uvicorn
import os

app = FastAPI()

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS, GET",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Max-Age": "86400",
}

@app.get("/")
def health():
    return Response(content='{"status":"ok"}', media_type="application/json", headers=CORS_HEADERS)

@app.options("/remove-bg")
async def options_remove_bg(request: Request):
    return Response(status_code=200, headers=CORS_HEADERS)

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    from rembg import remove
    input_bytes = await file.read()
    output_bytes = remove(input_bytes)
    return Response(
        content=output_bytes,
        media_type="image/png",
        headers=CORS_HEADERS
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
