import requests
import json
url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'
data = json.loads(requests.get(url).text)
books = data['results']['books']

########
# Task A
numpub = len([b for b in books if b['publisher'] == 'Scribner'])
print("A.", numpub)

########
# Task B
s = "Detective"
desc = len([b for b in books if b['description'].find(s.lower()) != -1])
print("B.", desc)

########
# Task C
def onlist(books):
	return books['weeks_on_list']

q = max(books, key = onlist)
title = q['title']
weeks = q['weeks_on_list']
print("C.", title, '|', weeks)

########
# Task D
def ranking_lastwk(books):
	return books['rank_last_week']

q = max(books, key = ranking_lastwk)
qtitle = q['title']
qrank = q['rank']
print("D.", "|".join([str(q['title']), str(q['rank']), str(q['rank_last_week'])]))

########
# Task E

print("E.", len([b for b in books if b['rank_last_week'] == 0]))

########
# Task F

from operator import itemgetter
newbooks = []
for b in books:
	if b['rank_last_week'] == 0:
		newbooks.append(b)

q = sorted(newbooks, key = itemgetter('rank'))[0]
print("F.", "|".join([q['title'], str(q['rank'])]))


########
# Task G

def calc_rank_change(books):
	return books['rank_last_week'] - books['rank']

books_ranked_last_week = [b for b in books if b['rank_last_week'] > 0]
x = max(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("G.", s)

########
# Task H

def rank_change_drop(books):
	return books['rank'] - books['rank_last_week']

x = min(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(rank_change_drop(x))])
print("H.", s)

########
# Task I

changes = [calc_rank_change(b) for b in books_ranked_last_week]
x = [v for v in changes if v > 0]
s = sum(x)
print("I.", s)

########
# Task J

x = [v for v in changes if v < 0]
s = sum(x)
print("J.", "|".join([str(len(x)), str(s)]))

########
# Task K

print('K.', max([len(b['title']) for b in books]))

########
# Task L
total = 0
for b in books:
	total += len(b['title'])

print('L.', str(int(total / len(books))))