# Lab 2: MIDI for Audio and Video Coding
# Multimedia Technologies

import pretty_midi
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load MIDI file
midi_data = pretty_midi.PrettyMIDI("AfterTheThrillIsGone.mid")

# Extract instruments
instruments = midi_data.instruments

# Step 2: Analyze notes
pitches = []
durations = []

for instrument in instruments:
    for note in instrument.notes:
        pitches.append(note.pitch)
        durations.append(note.end - note.start)

pitches = np.array(pitches)
durations = np.array(durations)

print("Total notes:", len(pitches))
print("Average note duration:", np.mean(durations))

# Step 3: Pitch-class distribution (similar to pcdist1)
pitch_classes = pitches % 12
pc_hist, pc_bins = np.histogram(pitch_classes, bins=12, range=(0, 12))

# Step 4: Visualization - Pitch Class Distribution
plt.figure(figsize=(8, 4))
plt.bar(range(12), pc_hist)
plt.xlabel("Pitch Class (0=C, 1=C#, ..., 11=B)")
plt.ylabel("Count")
plt.title("Pitch Class Distribution")
plt.show()

# Step 5: Piano Roll Visualization
plt.figure(figsize=(10, 5))

for instrument in instruments:
    for note in instrument.notes:
        plt.plot([note.start, note.end], [note.pitch, note.pitch])

plt.xlabel("Time (s)")
plt.ylabel("MIDI Pitch")
plt.title("Piano Roll Visualization")
plt.show()

# Step 6: MIDI Transformation (Transpose)
for instrument in instruments:
    for note in instrument.notes:
        note.pitch += 2  # Transpose up by 2 semitones

# Save transformed MIDI
midi_data.write("transposed_output.mid")

print("Transformed MIDI file saved as transposed_output.mid")
