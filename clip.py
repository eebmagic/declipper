from pydub import AudioSegment
import numpy as np
import array
import os
import time


###########################
### SETTINGS ###
AMP_FACTOR = 1.1
CUTOFF_REDUCTION = 0.6
###########################

source_dir = 'sources/'
files = os.listdir(source_dir)

for input_file in os.listdir(source_dir):
    start = time.time()

    # Load file
    # input_file = "sources/greater_than_four_chords.mp3"
    input_file = "sources/" + input_file
    print(f"### STARTING FILE: {input_file}")
    sound = AudioSegment.from_file(input_file)
    print(f"{time.time() - start}\t: load sound")

    # Load samples
    both = sound.get_array_of_samples()
    both = np.array(both)
    print(f"{time.time() - start}\t: load samples")

    # Amplify samples
    amped = both * AMP_FACTOR
    print(f"{time.time() - start}\t: amplify samples")

    # Cutoff samples
    cutoff = int(max(both) * CUTOFF_REDUCTION)
    cut = np.clip(amped, -cutoff, cutoff)
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
    output_file = "outputs/OUTPUT_" + input_file.split('/')[-1].split('.')[0] + ".wav"
    new.export(output_file, format="wav")
    print(f"{time.time() - start}\t: export file")

    print(f"\n ### FINISHED EXPORT: {output_file}\n")