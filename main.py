import base64

import uvicorn
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from services.fyndiq_bff import search
from vision.detect import detect_product

app = FastAPI()


@app.post("/image-search-test/")
async def upload_image_file(file: UploadFile = File(...)):
    hotdog_data = await file.read()
    labels = detect_product(hotdog_data)
    res = search(labels[0])
    return {"products": res}


class UploadImage(BaseModel):
    hotdog: str


@app.post("/image-search/")
async def upload_image(body: UploadImage):
    decoded_hotdog = base64.b64decode(body.hotdog)
    labels = detect_product(decoded_hotdog)
    res = search(labels[0])
    return {"products": res}


@app.get("/health/")
async def check_health():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
