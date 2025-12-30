# Lab 3: Database Filter for Audio and Video
# Multimedia Technologies

import numpy as np
import cv2
import soundfile as sf
from scipy.signal import butter, lfilter
from moviepy.video.io.VideoFileClip import VideoFileClip


# ---------------- AUDIO FILTERING ---------------- #

# Extract audio from video
video = VideoFileClip("What is Multimedia_.mp4")
audio = video.audio.to_soundarray(fps=44100)

# Convert stereo to mono
audio = audio.mean(axis=1)
sr = 44100

# Low-pass filter
def lowpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, data)

filtered_audio = lowpass_filter(audio, cutoff=3000, fs=sr)

# Save filtered audio
sf.write("filtered_audio.wav", filtered_audio, sr)
print("Filtered audio saved as filtered_audio.wav")

# VIDEO FILTERING  #

cap = cv2.VideoCapture("What is Multimedia_.mp4")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("filtered_video.mp4", fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    out.write(blurred)

cap.release()
out.release()

print("Filtered video saved as filtered_video.mp4")
