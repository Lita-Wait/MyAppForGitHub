import collections

text = 'lorem ipsum dolor sit amet amet amet'
words = text.split()
count = collections.Counter(words)
common = count.most_common(1)

longest = max(words, key=len)

print(f'{common[0][0]} {longest}')
