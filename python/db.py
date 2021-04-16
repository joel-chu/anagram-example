# create a small program to generate the sqlite database
# this will get re-use by others therefore it must be READ ONLY
# We are going to create a very simple table stucture with 3 fields
# word (the original word)
# characters (take the word apart then sort the characters in desc order)
# len (the length of the word)

from mylib import WORDS_DIR, jsonData, getWords
# prepare the input data
max = jsonData['MAX_CHAR']
min = jsonData['MIN_CHAR']

print(f"min {min} max {max}")

allFiles = range(min, max + 1)

print(f"{allFiles}")

# place holder
# wordsArr = []
# @NOTE if we only use `range`  it throws a `TypeError: cannot unpack non-iterable int object`
"""

for idx, num in enumerate(allFiles):
    print(f"i {idx} - num {num}")
    words = getWords(WORDS_DIR, num)
"""


# print(wordsArr)


import sqlite3
con = sqlite3.connect('../share/anagram.db')
cur = con.cursor()
# only the minimum setup just use the rowid if required
create_table_sql = "CREATE TABLE IF NOT EXISTS anagram (word TEXT, charseq TEXT)"

cur.execute(create_table_sql)

con.commit()
con.close()


"""






# execute many query at once

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
cur.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

# end loop here then commit



"""
