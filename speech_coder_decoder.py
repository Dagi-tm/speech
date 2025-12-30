# Lab 1: Speech Coder and Decoder
# Multimedia Technologies

import numpy as np
import librosa
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt

# 1. Load speech signal
speech, fs = librosa.load("ahem_x.wav", sr=None, mono=True)

# 2. Play original speech
sd.play(speech, fs)
sd.wait()

# 3. Compress (downsampling)
downsample_factor = 2
compressed_speech = speech[::downsample_factor]
compressed_fs = fs // downsample_factor

# 4. Reconstruct (interpolation)
reconstructed_speech = np.interp(
    np.arange(0, len(compressed_speech) * downsample_factor),
    np.arange(0, len(compressed_speech) * downsample_factor, downsample_factor),
    compressed_speech
)

# 5. Play reconstructed speech
sd.play(reconstructed_speech, fs)
sd.wait()

# 6. Plot signals
t1 = np.arange(len(speech)) / fs
t2 = np.arange(len(reconstructed_speech)) / fs

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t1, speech)
plt.title("Original Speech Signal")

plt.subplot(2, 1, 2)
plt.plot(t2, reconstructed_speech)
plt.title("Reconstructed Speech Signal")

plt.tight_layout()
plt.show()

# 7. Save output
sf.write("reconstructed_speech.wav", reconstructed_speech, fs)
