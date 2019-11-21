from animal_name_generator import generate_name

animals_in_zoo = [
    'A tiny horse',
    'Mystic Mouse',
    'Steg O Saurus',
    'Tardi Grade'
]


class Zoo:
    def __init__(self, members):
        self.members = members

    def count_members(self):
        return len(self.members)


if __name__ == '__main__':
    this_meetup = Zoo(animals_in_zoo)

    print('Hello, Pythonistas!')
    print('We are a great group of {}.'.format(
        this_meetup.count_members()
    ))

    surprise_guest_name = generate_name()
    print('Our surprise guest today: {}!'.format(surprise_guest_name))