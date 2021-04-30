import uvicorn
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from typing import List

app = FastAPI()


class ProductList(BaseModel):
    products: List[str]


@app.post("/image-search/")
async def upload_image_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


@app.get("/health/")
async def check_health():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
