from fastapi import FastAPI, UploadFile, File, Depends, HTTPException, Form
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from transformers import AutoProcessor, AutoModel
from PIL import Image
import torch
import os

# Load the Chinese-CLIP model
model_path = "./chinese-clip-vit-base-patch16"  # 请提前下载到本地目录
model = AutoModel.from_pretrained(model_path)
processor = AutoProcessor.from_pretrained(model_path)
model.eval()

# Basic Auth setup
security = HTTPBasic()
USERNAME = os.getenv("BASIC_AUTH_USERNAME", "admin")
PASSWORD = os.getenv("BASIC_AUTH_PASSWORD", "password")

# FastAPI app
app = FastAPI()

# Auth dependency
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username

@app.post("/embed")
async def embed_image(file: UploadFile = File(...), username: str = Depends(get_current_username)):
    image = Image.open(file.file).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        image_features = model.get_image_features(**inputs)
        image_features = image_features / image_features.norm(p=2, dim=-1, keepdim=True)

    return {"vector": image_features.squeeze(0).tolist()}

@app.post("/search")
async def search_text(text: str = Form(...), username: str = Depends(get_current_username)):
    inputs = processor(text=[text], return_tensors="pt")
    with torch.no_grad():
        vec = model.get_text_features(**inputs)
        vec = vec / vec.norm(p=2, dim=-1, keepdim=True)

    return {"vector": vec.squeeze(0).tolist()}
