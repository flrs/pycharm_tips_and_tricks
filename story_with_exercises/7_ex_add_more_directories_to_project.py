"""Add More Directories to a Project

Exercise:
We want to add another directory to the project.

Clone the GitHub repository https://github.com/flrs/animal_name_generator into a directory on your computer and then
add it to the project like this:

    1. Find the "Project Structure" action with the "Find Action" shortcut
    2. Click on "Add Content Root" on the right side of the preference pane
    3. Navigate to the directory you cloned the repository above in and add it
    4. Click "Apply" or "OK" and the cloned repository should be visible in PyCharm's project tree

Now, let's import the generate_name function from animal_name_generator. Interact with the red light bulb that appears
when you click on generate_name below to import the function from the directory we just added to the project.
"""
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