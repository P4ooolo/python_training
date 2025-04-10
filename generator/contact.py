from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n,f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


testdata = [
    Contact(
        firstname=random_string("firstname", 10),
        middlename=random_string("middlename", 10),
        lastname=random_string("lastname", 10),
        nickname=random_string("nickname", 10),
        title=random_string("title", 10),
        company=random_string("company", 10),
        address=random_string("address", 10),
        homenumber=random_string("homenumber", 10),
        mobile=random_string("mobile", 10),
        work=random_string("work", 10),
        fax=random_string("fax", 10),
        email=random_string("email", 10),
        email2=random_string("email2", 10),
        email3=random_string("email3", 10),
        bday=str(random.randrange(31) + 1),
        homepage=random_string("homepage", 10),
        bmonth=months[random.randrange(len(months) - 1)],
        byear=random_string("", 4),
        aday=str(random.randrange(31) + 1),
        amonth=months[random.randrange(len(months) - 1)],
        ayear=random_string("", 4),
    )
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
