from PitchClass import get_pitch_class_array, pitch_class_array_to_string
import copy

def get_interval(pitch_class_1: int, pitch_class_2: int):
    return ((pitch_class_1 - pitch_class_2) + 12) % 12

def get_vector(notes: str):
    pc_array = get_pitch_class_array(notes)
    interval_vector = [0] * 7
    for i in range(len(pc_array) - 1):
        for j in range(i + 1, len(pc_array)):
            candidate_1 = get_interval(pc_array[i], pc_array[j])
            candidate_2 = get_interval(pc_array[j], pc_array[i])
            interval_vector[min(candidate_1, candidate_2)] += 1

    return f'<{interval_vector[1]}{interval_vector[2]}{interval_vector[3]}{interval_vector[4]}{interval_vector[5]}{interval_vector[6]}>'

def get_normal_form(notes: str):
    sorted_pc_array = get_pitch_class_array(notes)
    sorted_pc_array.sort()
    best_array = []
    best_span = 13
    for i in range(len(sorted_pc_array)):
        current_span = get_interval(sorted_pc_array[len(sorted_pc_array)-1], sorted_pc_array[0])
        print(f'Checked {pitch_class_array_to_string(sorted_pc_array)} - {current_span}')
        if current_span == best_span:
            current_secondary = get_interval(sorted_pc_array[len(sorted_pc_array)-2], sorted_pc_array[0])
            best_secondary = get_interval(best_array[len(best_array)-2], best_array[0])
            print(f'Tie breaking using secondary intervals - Current:{current_secondary} Previous:{best_secondary}')
            if current_secondary < best_secondary:
                print("Current form is now the best form")
                best_span = current_span
                best_array = copy.copy(sorted_pc_array)
        elif current_span < best_span:
            best_span = current_span
            best_array = copy.copy(sorted_pc_array)

        sorted_pc_array.append(sorted_pc_array.pop(0))

    result = pitch_class_array_to_string(best_array)
    print(f'Final best form: {result} - {best_span}')
    return result



print(get_normal_form('c,g#,b,e,a'))