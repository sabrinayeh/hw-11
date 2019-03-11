# Add your own! :)
tv_characters = ["Will Byers", "Tyrion Lannister", "Oliver Queen", "Jean Luc Picard", "Malcom Reynolds", "The Doctor", "Sam Winchester", "Sherlock Holmes"]

# Write out my character list to a file called "text"
f = open("text.txt", "w")

for index, character in enumerate(tv_characters):

  f.write("{0}: {1}\n".format(index+1, character))

f.close()


'''
1: Will Byers
2: Tyrion Lannister
3: Oliver Queen
4: Jean-Luc Picard
5: Malcolm Reynolds
6: The Doctor
7: Sam Winchester
8: Sherlock Holmes

'''