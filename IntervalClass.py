from PitchClass import get_pitch_class_array, pitch_class_array_to_string
import copy

def get_interval(pitch_class_1: int, pitch_class_2: int):
    return ((pitch_class_1 - pitch_class_2) + 12) % 12

def min_interval(pitch_class_1: int, pitch_class_2: int):
    ic = get_interval(pitch_class_1, pitch_class_2)
    return min(ic, 12 - ic)

def pcs_to_vector(pc_array: list[int]):
    interval_vector = [0] * 7
    for i in range(len(pc_array) - 1):
        for j in range(i + 1, len(pc_array)):
            interval_vector[min_interval(pc_array[i], pc_array[j])] += 1
    return f'<{interval_vector[1]}{interval_vector[2]}{interval_vector[3]}{interval_vector[4]}{interval_vector[5]}{interval_vector[6]}>'

def notes_to_vector(notes: str):
    return pcs_to_vector(get_pitch_class_array(notes))

def pcs_to_normal(pc_array: list[int]):
    pc_array.sort()
    best_array = []
    best_span = 13
    for i in range(len(pc_array)):
        current_span = get_interval(pc_array[len(pc_array) - 1], pc_array[0])
        print(f'Checked {pitch_class_array_to_string(pc_array)} - {current_span}')
        if current_span == best_span:
            current_secondary = get_interval(pc_array[len(pc_array) - 2], pc_array[0])
            best_secondary = get_interval(best_array[len(best_array) - 2], best_array[0])
            print(f'Tie breaking using secondary intervals - Current:{current_secondary} Previous:{best_secondary}')
            if current_secondary < best_secondary:
                print("Current form is now the best form")
                best_span = current_span
                best_array = copy.copy(pc_array)
        elif current_span < best_span:
            best_span = current_span
            best_array = copy.copy(pc_array)

        pc_array.append(pc_array.pop(0))

    result = pitch_class_array_to_string(best_array)
    print(f'Final best form: {result} - {best_span}')
    return result


def notes_to_normal(notes: str):
    return pcs_to_normal(get_pitch_class_array(notes))


# print(notes_to_normal('c,g#,b,e,a'))

problem_1 = 'Cb,G,Bb,E,Gb,F,Db,C,D,Bb'
problem_1_pcs = get_pitch_class_array(problem_1)
print(problem_1_pcs)
print("ics in order:")
for i in range(len(problem_1_pcs) - 1):
    print(min_interval(problem_1_pcs[i], problem_1_pcs[i + 1]))

problem_2a = [1,5,8,9]
problem_2b = [0,3,4,7,8]
print(pcs_to_vector(problem_2a))
print(pcs_to_vector(problem_2b))

problem_3a = [4,7,2,11]
problem_3b = 'Eb,C,B,Bb,E,G'

pcs_to_normal(problem_3a)
notes_to_normal(problem_3b)
