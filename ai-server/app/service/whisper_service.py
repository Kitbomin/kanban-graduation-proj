import whisper

print("Whisper 로딩중")

model = whisper.load_model("base")

print("Whisper 호출 완료")

def transcribe_audio(audio_path):

    result = model.transcribe(
        audio_path,
        language="ko",
        fp16=False
    )

    return result["text"]