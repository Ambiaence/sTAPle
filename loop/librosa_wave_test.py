import librosa.display
import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load("test.wav", duration=10)

fig, ax = plt.subplots(nrows=3, sharex=True)

librosa.display.waveshow(y, sr=sr, ax=ax[0])

ax[0].set(title='Envelope view, mono')

ax[0].label_outer()
