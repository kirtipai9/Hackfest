## FOR VIDEO TO MP3 WITHOUT STORING THE VIDEO

from yt_dlp import YoutubeDL
audio_path = "extracted_audio.wav"
ydl_opts={
    'format': 'bestaudio/best',      # best available audio
    'outtmpl': 'temp_audio.%(ext)s', # temporary download file
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',     # convert to WAV
        'preferredquality': '192',
    }],
}
with YoutubeDL(ydl_opts) as ydl:
    video_url="https://www.youtube.com/watch?v=P_Q-zvU96FE"
    ydl.download([video_url])
print(f"Audio extracted successfully: {audio_path}")



##AUDIO TO TEXT

import whisper
mdoel=whisper.load_model("small")
result=mdoel.transcribe("temp_audio.wav")
text=result["text"]
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(text)