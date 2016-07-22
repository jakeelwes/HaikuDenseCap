import json
import pronouncing
from random import randint

#get the data from the json file
haiku_base = open('/Users/rollasoul/densecap/vis/data/results.json')
wjson = haiku_base.read()
wjdata = json.loads(wjson)
wjdata_list = wjdata['results'][0]['captions']

# create empty storage for selected captiosn with fitting syllables (with either 5 or 7 syllables)
syllables5 = []
syllables7 = []
syllables23 = []

# check all captions for fitting syllables (using pronouncingpy + CMU pronouncing dictionary)
# add them to the empty storage
for i in range (1, 83):

	try:
		text = wjdata['results'][0]['captions'][i - 1]

		phones = [pronouncing.phones_for_word(p)[0] for p in text.split()]
		count = sum([pronouncing.syllable_count(p) for p in phones])
		for y in range (1, 2):
			if int(count) == 5:
				syllables5.append(wjdata['results'][0]['captions'][i - 1])
		for x in range (0, 1):
			if int(count) == 7:
				syllables7.append(wjdata['results'][0]['captions'][i - 1])
		for z in range (0, 1):
			if int(count) == 3 or int(count) == 2:
				syllables23.append(wjdata['results'][0]['captions'][i - 1])

# skip over errors caused by non-indexed word <UNK> in captions
	except IndexError:
    		pass
	continue

# create arrays for pre-selections of fitting syllables
selection_line1 = ['fill']
selection_line2 = ['fill']
selection_line3 = []

# randomise selection per syllable selection
while selection_line1[0] == selection_line2[0]:
	selection_line1 = syllables5 [randint(0,(len(syllables5) -1) /2)]
	selection_line2 = syllables7 [randint(0,(len(syllables7)-1))]
	selection_line3 = syllables5 [randint(len(syllables5)/2,(len(syllables5)-1))]

# add a bit of random weirdness to it (cut one caption after first two words and replace one of the 3 verses of the Haiku)
i = randint(0,2)
x = randint(0,2)
if randint(0,1) == 0:
	if x == 0:
		selection_line1 = selection_line1.split()
		selection_line1 = selection_line1 [0] + " " + selection_line1 [1]
	if x == 1:
		selection_line2 = selection_line2.split()
		selection_line2 = selection_line2 [0] + " " + selection_line2 [1]
	if x == 2:
		selection_line3 = selection_line3.split()
		selection_line3 = selection_line3 [0] + " " + selection_line3 [1]

# have a look at the result
print selection_line1 
print selection_line2 
print selection_line3

for i in range (0, len(syllables23)): 
	print syllables23




