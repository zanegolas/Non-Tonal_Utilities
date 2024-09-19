pitchClasses = {
    'C': 0,
    'C#': 1,
    'Db': 1,
    'D': 2,
    'D#': 3,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'Gb': 6,
    'G': 7,
    'G#': 8,
    'Ab': 8,
    'A': 9,
    'A#': 10,
    'Bb': 10,
    'B': 11,
}

def get_pitch_class_array(note_string: str):
    note_string = note_string.upper()
    note_list = note_string.split(',')
    pitch_class_array = []
    for note in note_list:
        pitch_class_array.append(pitchClasses[note])

    return pitch_class_array

def pitch_class_array_to_string(pitch_class_array):
    pc_string = ''
    for pitch_class in pitch_class_array:
        if pitch_class == 10:
            pc_string += 'A'
        elif pitch_class == 11:
            pc_string += 'B'
        else:
            pc_string += str(pitch_class)
    return pc_string