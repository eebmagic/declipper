from pydub import AudioSegment
import numpy as np
import array
import time

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


start = time.time()

input_file = "sources/greater_than_four_chords.mp3"
sound = AudioSegment.from_file(input_file)
print(f"{time.time() - start}\t: load sound")

both = sound.get_array_of_samples()
print(f"{time.time() - start}\t: load samples")
amped = amp(both, 1.1)
print(f"{time.time() - start}\t: amplify samples")
cut = cutoff_max(amped, int(max(both) * 0.6))
print(f"{time.time() - start}\t: cutoff samples")
cut = array.array(sound.array_type, cut)
print(f"{time.time() - start}\t: put samples in array")

new = AudioSegment(
    data=cut,
    frame_rate = sound.frame_rate,
    sample_width=2,
    channels=2
)
print(f"{time.time() - start}\t: build new sound")

# print("Original sample size: " + '{:,}'.format(len(both)))
# print("Output sample size: " + '{:,}'.format(len(new.get_array_of_samples())))

output_file = "OUTPUT_" + input_file.split('/')[-1].split('.')[0] + ".wav"

new.export(output_file, format="wav")
print(f"{time.time() - start}\t: export file")
print(f"FINISHED EXPORT: {output_file}")