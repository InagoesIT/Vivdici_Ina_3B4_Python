# Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer). The function will return
# the song composed by going through the musical notes beginning with the start position
# and following the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]


def get_composed_song(musical_notes, moves, start_position):
    current_index = start_position
    song = [musical_notes[current_index]]
    size_musical_notes = len(musical_notes)

    for move in moves:
        current_index += move
        if current_index >= size_musical_notes:
            current_index = current_index % size_musical_notes
        song.append(musical_notes[current_index])

    return song


if __name__ == '__main__':
    print(get_composed_song(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
