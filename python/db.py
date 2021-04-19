# create a small program to generate the sqlite database
# this will get re-use by others therefore it must be READ ONLY
# We are going to create a very simple table stucture with 3 fields
# word (the original word)
# characters (take the word apart then sort the characters in desc order)
# len (the length of the word)
import sqlite3
con = sqlite3.connect('../../share/anagram.db')

cur = con.cursor()

# execute many query at once

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
cur.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

# end loop here then commit

cur.commit()
con.close()
