"""Reformatting Code

This code is a mess. Let's reformat it!

Exercise: Find the "Reformat Code" command with the "Find Action" shortcut and clean up this file.
"""
people_on_meetup = [
'A tiny horse' ,
  'Mystic Mouse',
            'Steg O Saurus',
    'Tardi Grade'
]

class Meetup:
 def __init__ ( self, members):
        self.members =        members
    def count_members(self):
   return len(self.members)

if __name__ == '__main__':
  this_meetup = Meetup(people_on_meetup)

    print( 'Hello, Pythonistas!')
    print('We are a great group of {}.'.format(
            this_meetup.count_members()
                                             ))
