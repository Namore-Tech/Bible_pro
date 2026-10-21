import sys
import pyaudio
import numpy as np
from faster_whisper import WhisperModel

print(f"Python Executable: {sys.executable}")


print("Loading Faster-Whisper model...")
model = WhisperModel("small", device="cpu", compute_type="int8")

INPUT_DEVICE_INDEX = 1
SAMPLE_RATE = 16000 
CHUNK_SIZE = 1024
LISTEN_SECONDS = 5   

p = pyaudio.PyAudio()

def init_stream():
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK_SIZE,
        input_device_index=INPUT_DEVICE_INDEX
    )
    return stream

def transcribe_chunk(audio_np: np.ndarray, sample_rate: int = 16000) -> str:
    segments, _ = model.transcribe(audio_np, beam_size=5, language="en")
    return " ".join(seg.text.strip() for seg in segments)

print("Initializing STT. Listening... (Press Ctrl + C to stop)")
stream = init_stream()
stream.start_stream()

stream = init_stream()
stream.start_stream()

def listen_and_transcribe():
    frames = []
    for _ in range(0, int(SAMPLE_RATE / CHUNK_SIZE * LISTEN_SECONDS)):
        data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
        frames.append(data)

    audio_bytes = b"".join(frames)
    audio_int16 = np.frombuffer(audio_bytes, dtype=np.int16)
    audio_float32 = audio_int16.astype(np.float32) / 32768.0

    print("Transcribing...")
    text = transcribe_chunk(audio_float32, sample_rate=SAMPLE_RATE)

    if text:
        print(f"You said: {text}")

    return text