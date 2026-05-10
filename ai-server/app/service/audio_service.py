# import ffmpeg
# import os

# PROCESSED_DIR = "app/storage/processed"

# def preprocess_audio(input_path):

#     #파일명 추출
#     filename = os.path.basename(input_path)

#     name, ext = os.path.splitext(filename)

#     #출력파일 경로 지정

#     output_path = os.path.join(
#         PROCESSED_DIR,
#         f"{name}_preprocessed.wav"
#     )

#     # ffmpeg 변환
#     (
#         ffmpeg
#         .input(input_path)
#         .output(
#             output_path,

#             ac = 1,

#             ar = 16000,

#             format='wav'
#         )
#         .overwrite_output()
#         .run(quiet=True)
#     )

#     return output_path