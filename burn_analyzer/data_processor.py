EXERCISE_NAMES_ROW = 0
MAX_VALUE_ROW = 1


def get_normalised_exercises(exercise_data):
    for position, data in enumerate(exercise_data):
        if position == EXERCISE_NAMES_ROW:
            exercises = data
        if position > MAX_VALUE_ROW:
            zip_list = [blah for blah in (zip(exercises[1:], data[1:]))]
            normalised_exercises = [(data[0], exentry[0], exentry[1]) for exentry in zip_list]
            clean_normalised_exercises = [exercise for exercise in normalised_exercises if exercise[2] != '']
            print(clean_normalised_exercises)