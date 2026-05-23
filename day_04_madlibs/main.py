# Mad Libs Game
print("Welcome to Mad Libs!")
print("Please provide the following words:\n")

# Collect user inputs
noun1 = input("Enter a noun (e.g., 'dog', 'spaceship'): ")
verb1 = input("Enter a verb (e.g., 'run', 'dance'): ")
adjective1 = input("Enter an adjective (e.g., 'silly', 'sparkly'): ")
noun2 = input("Another noun: ")
verb2 = input("Another verb: ")
adjective2 = input("Another adjective: ")
plural_noun = input("A plural noun (e.g., 'robots', 'tacos'): ")
celebrity = input("A famous person's name: ")

# The funny story template
story = f"""
--- Your Mad Libs Story ---

Last week, my {adjective1} {noun1} decided to {verb1} through the kitchen.
Suddenly, a giant {noun2} appeared and started to {verb2} uncontrollably!
I called {celebrity} for help, but they were busy eating {plural_noun}.

“Don’t worry,” I said, “I’ll just use my {adjective2} imagination.”
So I grabbed a spoon, put it on my head, and turned into a superhero.
Moral of the story: Never underestimate a {adjective1} {noun1} with a spoon.

THE END
"""

# Display the result
print(story)