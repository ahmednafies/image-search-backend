import base64

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.fyndiq_bff import search
from vision.detect import detect_product

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UploadImage(BaseModel):
    image: str


@app.post("/image-search/")
async def upload_image(body: UploadImage):
    decoded_image = base64.b64decode(body.image)
    labels = detect_product(decoded_image)
    res = search(labels[0])
    return {"products": res, "label": labels[0]}


@app.get("/health/")
async def check_health():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
