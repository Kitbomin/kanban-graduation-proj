import whisper

print("모델 로딩 중...")

model = whisper.load_model("small")

print("모델 로딩 완료")

result = model.transcribe(
    "test4.wav",
    language="ko",
    fp16=False
)

print(result["text"])