"""
Today I Learned


This script updates the Readme.md as new entries accumulate.
"""

import os
from collections import defaultdict

listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk("."):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

# kick out .git/
# kick out .html
# kick out this file
# kick out README.md

categories = defaultdict(list)

for f in listOfFiles:
    fs = f.split("/")
    ft = fs[-1].split(".")[-1]
    cat = fs[1]
    if fs[1] == ".git" or cat == 'README.md':
        continue
    if cat == 'til.py' or cat == 'README.html':
        continue
    if ft == 'html':
        continue
    print(cat, fs, ft)
    categories[cat].append(fs[-1])

cats = list(categories.keys())
cats.sort()


cathead = ["## Categories"]
lines = [f'\n - [{cat}](#{cat})' for cat in cats]
cathead.extend(lines)
cathead.append("\n---\n")

n = 0
for cat in cats:
    cathead.append(f'\n### {cat}')
    tils = categories[cat]
    for til in tils:
        pth = f'{cat}/{til}'
        with open(pth, 'r', encoding='utf-8', errors='ignore') as f:
            contents = f.readlines()
            title = contents[0]
            title = title.replace("# ", "")
            print(title)
            line = f'\n- [{title.strip()}]({pth})'
            cathead.append(line)
        n += 1


content = "\n".join(cathead)

head = """
# Today I Learned

A place to capture the nuggets so that I don't repeat the same search again.

Inspired by [jbranchaud](https://github.com/jbranchaud/til).

"""

head = f'{head}\n{n} TILs at last count.\n'

content = head + "\n" + content
with open('README.md', 'w') as of:
    of.write(content)
