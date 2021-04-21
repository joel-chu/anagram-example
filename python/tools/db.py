# create a small program to generate the sqlite database
# this will get re-use by others therefore it must be READ ONLY
# We are going to create a very simple table stucture with 3 fields
# word (the original word)
# characters (take the word apart then sort the characters in desc order)
# len (the length of the word)
from sys import argv
from mylib import WORDS_DIR, jsonData, getWords
import sqlite3

con = sqlite3.connect('../../share/anagrams.db')

def getCharSeq(word):
    """
    input the possible world and sort the character by A-Z
    """
    seq = [ch for ch in word]
    seq.sort()

    return ''.join(seq)

def initTable():
    """
    prepare the input data
    """
    cur = con.cursor()
    # only the minimum setup just use the rowid if required
    create_table_sql = "CREATE TABLE IF NOT EXISTS anagrams (word TEXT, charseq TEXT, desc TEXT)"
    cur.execute(create_table_sql)
    con.commit()

    max = jsonData['MAX_CHAR']
    min = jsonData['MIN_CHAR']
    allFiles = range(min, max + 1)
    # @NOTE if we only use `range`  it throws a `TypeError: cannot unpack non-iterable int object`
    data = []
    for idx, num in enumerate(allFiles):
        print(f"i {idx} - num {num}")
        words = getWords(WORDS_DIR, num)
        for word in words:
            data.append((word, getCharSeq(word)))
    # we build a huge array of data
    insert_sql = "INSERT INTO anagrams (word, charseq) VALUES (?,?)"
    cur.executemany(insert_sql, data)
    con.commit()

    return True

def getAnagramData(word):
    """
    Query the table for the anagram word
    """
    seq = getCharSeq(word)
    find_sql = "SELECT word from anagrams WHERE charseq=?"
    cur = con.cursor()
    # loop that later
    return cur.execute(find_sql, (seq))

def readTable(l = 2):
    cur = con.cursor()
    print(l)
    for row in cur.execute("SELECT * FROM anagrams WHERE length(word) = ?", (int(l),)):
        print(row[0])

# con.close() <-- just keep it open

if __name__ == '__main__':
    script, cmd = argv
    """
    Check the command
    """
    if (cmd == "init"):
        initTable()
    elif(cmd == "all"):
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM anagrams"):
            print(row)
    else:
        readTable(cmd)
