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
    new = [int(point * increase) for point in data]
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
both = sound.get_array_of_samples()

print(f"\n{len(left) = }")
print(f"{len(right) = }")
print(type(left))

print(left[:100])
print(max(left))
print(max(right))
print(min(left))
print(min(right))

amped = amp(both, 1.1)
cut = cutoff_max(amped, int(max(both) * 0.6))


## This Works!!
# new = AudioSegment(
#     data=sound.get_array_of_samples(),
#     frame_rate = sound.frame_rate,
#     sample_width=2,
#     channels=2
# )

import array
print(type(sound.get_array_of_samples()[0]), type(cut[0]))
cut = array.array(sound.array_type, cut)
print(type(sound.get_array_of_samples()), type(cut))
new = AudioSegment(
    data=cut,
    frame_rate = sound.frame_rate,
    sample_width=2,
    channels=2
)

# new.export("OUTPUT.mp3", format="mp3", bitrate='8k')
new.export("OUTPUT.wav", format="wav")
print("FINISHED EXPORT: OUTPUT.wav")