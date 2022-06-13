SIZE = 3


def create_field(field_size):
    field = []

    for x_coord in range(field_size):
        field.append([])

        for y_coord in range(field_size):
            field[-1].append(f' {y_coord + x_coord * field_size}')

    return field

def show_field(field):
    for line in field:
        print(' '.join(line))


def make_turn(turn_position, field):
    pass

game_field = create_field(field_size=SIZE)
make_turn('2', game_field)
show_field(game_field)


