"""Rename Like a Pro

Exercise:
The contents of the people_on_meetup variable look more like a zoo. Let's rename the following items:

    - variable "people_on_meetup" -> "animals_in_zoo"
    - class "Meetup" -> "Zoo"

To rename an item, put the cursor on the item you want to rename and then press Shift+F6 on Windows/Linux
or ⇧+F6 on Mac OS.
"""
people_on_meetup = [
    'A tiny horse',
    'Mystic Mouse',
    'Steg O Saurus',
    'Tardi Grade'
]


class Meetup:
    def __init__(self, members):
        self.members = members

    def count_members(self):
        return len(self.members)


if __name__ == '__main__':
    this_meetup = Meetup(people_on_meetup)

    print('Hello, Pythonistas!')
    print('We are a great group of {}.'.format(
        this_meetup.count_members()
    ))
