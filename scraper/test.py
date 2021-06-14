# SOURCE unit testing scraper https://dev.to/albertulysses/unit-testing-your-web-scraper-1aha
# FILENAME test.py

import os
import sys
import clean as cl

user_name = 'Vanessa'
project_name = 'test_scrape'

clean_file = "clean.py"
prg = './clean.py'
DATA_PATH = ('/{}/Data/{}/').format(user_name, project_name)



# -------------------------------------------------
def test_exists():
    """checks if the file exist"""

    assert os.path.isfile(prg)


# -------------------------------------------------
def test_price():
    """£51.77 -> 51.77 type float"""

    res = cl.monetary('£51.77')
    assert res == float(51.77)


# -------------------------------------------------
def test_integer():
    """'in stock (22 available)' -> 22"""

    res = cl.wholenumber('in stock (22 available)')
    assert res == int(22)


def write_source(clean_file):
	f = open(clean_file, "a")
	f.write("#SOURCE\n")
	f.write("#FILENAME \n")
	f.close()


def test_clean(clean_file):
	f = open(clean_file, "a")
	file = open(clean_file)
	print(file.read())
	search_word = input("#SOURCE\n")
	if (search_word in file.read()):
		print("word found")
	else:
		f = open(clean_file, "a")
		f.write("#SOURCE\n") # FIXME need to fix so the loop creates single
		f.write("#FILENAME \n") # FIXME each file needs to have one, remove loop that always adds one more
		print("word not found, I've added it")
		f.close()


