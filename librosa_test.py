from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
input_data = read("test.wav")
audio = input_data[1]

plt.figure(figsize=(5,1))
plt.axis("off")
for x in range(0,100):
    plt.plot(audio[0+x:1024+x])
    plt.savefig("1"+".png")
