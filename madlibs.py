"""I'm not sure why but the input for everything after the first prompt requires quotes to run"""

print("Mad libs where libs get mad\nStart below:\n")
time = input("Enter a number from 1 to 12: ")
items = input("Enter a noun (plural): ")
name = input("Enter a name: ")
scream = input("Enter any sentence: ")
action = input("Enter a verb: ")

print("The story goes...\nIt was {0} when I heard a knock at the door.\nI opened the door and there was a box full of {1} with a note saying \"From {2}.\"\nJust as I closed the door I heard a scream: \"{3}.\"\n I froze in place and all I could do was {4}.".format(time, items, name.title(), scream.upper(), action))