import random2

movies_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']

# pick a random choice from a list of strings.
movie = random2.choice(movies_list)
print(movie)
# Output 'The Shawshank Redemption'

for i in range(2):
    movie = random2.choice(movies_list)
    print(movie)