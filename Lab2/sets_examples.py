# Sets

cats = set()  # creates empty set
cats.add('Lion')
cats.add('Tiger')
print(cats)
cats.add('Cheetah')
print(cats)

birds = {'owl', 'robin', 'swan'}
print(birds)
birds.add('robin')  # can't add duplicates
print(birds)
birds.remove('owl')
birds.add('cardinal')
print(birds)

for bird in birds:
    print(bird)


# trick to remove duplicates from list
bird_list = ['robin', 'swan', 'swan', 'eagle', 'cardinal', 'swan', 'robin']
bird_list_no_duplicates = list(set(bird_list))
print(bird_list_no_duplicates)