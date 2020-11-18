from pydub import AudioSegment
import time
import numpy as np

def split_channels(s):
    arr = s.get_array_of_samples()
    if s.channels <= 1:
        return arr
    elif s.channels == 2:
        left = []
        right = []
        for ind in range(len(arr)):
            if ind % 2 == 0:
                left.append(arr[ind])
            else:
                right.append(arr[ind])

        return (left, right)


def amp(data, increase):
    new = [point* increase for point in data]
    return new


def cutoff_max(data, cutoff):
    cutoff = abs(cutoff)
    new = []
    for point in data:
        if abs(point) > cutoff:
            if point > 0:
                new.append(cutoff)
            else:
                new.append(-cutoff)
        else:
            new.append(point)

    return new


def abreviate(data, rate):
    new = []
    for ind, point in enumerate(data):
        if ind % rate == 0:
            new.append(point)

    return new


sound = AudioSegment.from_file("sources/sax_waves.wav")
samples = sound.get_array_of_samples()

print(f"{len(samples) = }")

rate = 44_100 # MHz
length = 72 # seconds
full_sample_size = rate * length * sound.channels
channel_sample_size = rate * length

print(f"{full_sample_size = }")
print(f"{channel_sample_size = }")


left, right = split_channels(sound)

print(f"\n{len(left) = }")
print(f"{len(right) = }")
print(type(left))

print(left[:100])
print(max(left))
print(max(right))
print(min(left))
print(min(right))

amped = amp(left, 0.1)
cut = cutoff_max(amped, max(left) * 0.8)


## Optionally graph the change
# from matplotlib import pyplot as plt
# abrev_rate = 100
# abrev_size = len(left) // 5
# abrev_left = abreviate(left[:abrev_size], abrev_rate)
# abrev_cut = abreviate(cut[:abrev_size], abrev_rate)

# plt.plot(abrev_cut, color='red')
# plt.plot(abrev_left, color='black')
# plt.show()


## This Works!!
new = AudioSegment(
    data=sound.get_array_of_samples(),
    frame_rate = sound.frame_rate,
    sample_width=2,
    channels=2
)

# new.export("OUTPUT.mp3", format="mp3", bitrate='8k')
new.export("OUTPUT.wav", format="wav")
print("FINISHED EXPORT: OUTPUT.mp3")