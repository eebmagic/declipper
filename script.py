from pydub import AudioSegment
import numpy as np
import array
import time


def amp(data, increase):
    return data * increase


def cutoff_max(data, cutoff):
    return np.clip(data, -cutoff, cutoff)


def abreviate(data, rate):
    new = []
    for ind, point in enumerate(data):
        if ind % rate == 0:
            new.append(point)

    return new


start = time.time()

# Load file
input_file = "sources/greater_than_four_chords.mp3"
sound = AudioSegment.from_file(input_file)
print(f"{time.time() - start}\t: load sound")

# Load samples
both = sound.get_array_of_samples()
both = np.array(both)
print(f"{time.time() - start}\t: load samples")

# Amplify samples
amped = amp(both, 1.1)
print(f"{time.time() - start}\t: amplify samples")

# Cutoff samples
cut = cutoff_max(amped, int(max(both) * 0.6))
cut = cut.astype('int64')
print(f"{time.time() - start}\t: cutoff samples")

# Convert numpy.array to array.array
cut = array.array(sound.array_type, cut)
print(f"{time.time() - start}\t: put samples in array")

# Build new sound object
new = AudioSegment(
    data=cut,
    frame_rate = sound.frame_rate,
    sample_width=2,
    channels=2
)
print(f"{time.time() - start}\t: build new sound")

# Export OUTPUT_ file
output_file = "OUTPUT_" + input_file.split('/')[-1].split('.')[0] + ".wav"
new.export(output_file, format="wav")
print(f"{time.time() - start}\t: export file")

print(f"\nFINISHED EXPORT: {output_file}")