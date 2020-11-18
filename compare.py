from pydub import AudioSegment
import numpy as np
from matplotlib import pyplot as plt


original = AudioSegment.from_file("sources/sax_waves.wav")
created = AudioSegment.from_file("OUTPUT.wav")


original_samples = original.get_array_of_samples()
created_samples = created.get_array_of_samples()


print(len(original_samples), len(created_samples), len(original_samples) == len(created_samples))

graph_size = len(original_samples) // 7
start = graph_size // 2
plt.plot(original_samples[start:graph_size], color='black', label='original')
plt.plot(created_samples[start:graph_size], color='red', label='created')
plt.legend()
plt.show()