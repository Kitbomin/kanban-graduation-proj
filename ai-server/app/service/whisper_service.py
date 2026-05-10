import whisper

print("Whisper 로딩중")

model = whisper.load_model("base")

print("Whisper 호출 완료")

def transcribe_audio(file_path: str):

    result = model.transcribe(
        file_path,
        language="ko"
    )

    return result["text"]