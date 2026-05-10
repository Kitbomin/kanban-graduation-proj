from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil
import uuid

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    allowed_extensios = [".wav", ".mp3", ".m4a"]

    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in allowed_extensios:
        raise HTTPException(
            status_code=400,
            detail="지원하지 않는 오디오 형식입니다."
        )
    
    # UUID 파일 생성
    unique_filename = f"{uuid.uuid4()}{file_extension}"

    file_path = UPLOAD_DIR / unique_filename

    # 저장
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "파일업로드 성공",
        "filename": unique_filename,
        "path": str(file_path)
    }