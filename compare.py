from pydub import AudioSegment
import numpy as np
from matplotlib import pyplot as plt
import sys

def abreviate(data, rate=100):
    new = []
    for ind, point in enumerate(data):
        if ind % rate == 0:
            new.append(point)

    return new



acceptable_filetypes = ["mp3", "wav"]

file_a = None
file_b = None
for entry in sys.argv:
    if entry.split('.')[-1] in acceptable_filetypes:
        if not file_a and not file_b:
            file_a = entry
        elif file_a and not file_b:
            file_b = entry

original = AudioSegment.from_file(file_a)
created = AudioSegment.from_file(file_b)

original_samples = abreviate(original.get_array_of_samples())
created_samples = abreviate(created.get_array_of_samples())

len_a = len(original_samples)
len_b = len(created_samples)
print(len_a, len_b, f"lengths match: {len_a == len_b}")

end = len(original_samples) // 3
start = 0
total_points = len(original_samples[start:end])
print(f"{total_points = }")

plt.plot(original_samples[start:end], color='black', label='original')
plt.plot(created_samples[start:end], color='red', label='created')
plt.legend()
plt.show()