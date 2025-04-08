from fixture.orm import ORMFixture
from datetime import datetime
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     l = db.get_group_list()
#     for item in l:
#         print(item)
#     print(len(l))

try:
    l = db.get_contacts_in_group(Group(id=122))
    for item in l:
        print(item)
    print(len(l))

finally:
    pass #db.destroy()