from model.group import Group
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n: f:", ["number of groups", "file"])
except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)

n = 5
f = 'data/groups.jason'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    # string will be chosen from letters, digits and 10 spaces -- ' '*10
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*5
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header=" header", footer="")] + [
    # will generate random string that starts with word 'Name' or 'Header etc and + some more random symbols
    Group(name=random_string('Name', (10)), header=random_string('Header', (5)), footer=random_string('Footer', (7)))
          for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    out.write(json.dumps(testdata, default= lambda x: x.__dict__, indent=2))
