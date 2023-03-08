from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples

plt.figure(figsize=(5,1))
plt.axis("off")

for x in range(500, 1000):
    input_data = read("test.wav")
    audio = input_data[1]
    plt.plot(audio[x:x+44100*x])
    plt.savefig(str(x) + ".png")
    print(x)
    if x > (10**4):
        break
