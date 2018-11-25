EXERCISE_NAMES_ROW = 0
MAX_VALUE_ROW = 1


def get_normalised_exercises(exercise_data):
    clean_normalised_exercises = []
    for position, data in enumerate(exercise_data):
        if position == EXERCISE_NAMES_ROW:
            exercises = data
        if position > MAX_VALUE_ROW:
            zipped_exercises_and_dates = [entry for entry in (zip(exercises[1:], data[1:]))]
            normalised_exercises = [(data[0], exentry[0], exentry[1]) for exentry in zipped_exercises_and_dates]
            clean_normalised_exercises += [exercise for exercise in normalised_exercises if exercise[2] != '']
    return clean_normalised_exercises