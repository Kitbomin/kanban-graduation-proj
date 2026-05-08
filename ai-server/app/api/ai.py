from fastapi import APIRouter, UploadFile, File
import tempfile
import os

from app.service.whisper_service import transcribe_audio

router = APIRouter(prefix="/ai")

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):

    # 임시파일 먼저 생성
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:

        # 파일 읽기
        content = await file.read()

        tmp.write(content)

        temp_path = tmp.name

    # 위스퍼로 전사
    text = transcribe_audio(temp_path)

    # 임시파일 만들어놓은거 삭제
    os.remove(temp_path)

    return {
        "script": text
    }