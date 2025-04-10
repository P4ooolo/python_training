import pymysql.connections
from model.contact import Contact
from model.group import Group

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
                cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
                for row in cursor:
                    (id, name, header, footer) = row
                    list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            sql = """select
                   id,
                   firstname,
                   middlename,
                   lastname,
                   nickname,
                   title,
                   company,
                   address,
                   home as homenumber,
                   mobile,
                   work,
                   fax,
                   email,
                   email2,
                   bday,
                   homepage,
                   email3,
                   bmonth,
                   byear,
                   aday,
                   amonth,
                   ayear 
                   from addressbook"""
            cursor.execute(sql)
            for row in cursor:
                (id,
                   firstname,
                   middlename,
                   lastname,
                   nickname,
                   title,
                   company,
                   address,
                   homenumber,
                   mobile,
                   work,
                   fax,
                   email,
                   email2,
                   bday,
                   homepage,
                   email3,
                   bmonth,
                   byear,
                   aday,
                   amonth,
                   ayear ) = row

                list.append(Contact(id=str(id),
                                    firstname=firstname,
                                    lastname=lastname,
                                    middlename=middlename,
                                    homenumber=homenumber,
                                    nickname=nickname,
                                    title=title,
                                    company=company,
                                    fax=fax,
                                    work=work,
                                    mobile=mobile,
                                    bday=str(bday),
                                    homepage=homepage,
                                    bmonth=bmonth,
                                    byear=byear,
                                    aday=str(aday),
                                    amonth=amonth,
                                    ayear=ayear,
                                    email=email,
                                    email2=email2,
                                    email3=email3,
                                    address=address))
        finally:
            cursor.close()
        return list


    def get_contact_by_id(self, id):
        cursor = self.connection.cursor()
        try:
            sql = """select
                      id,
                      firstname,
                      lastname,
                      address,
                      home as homenumber,
                      mobile,
                      work,
                      email,
                      email2,
                      email3
                      from addressbook where id = %d""" % int(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            (id,
            firstname,
            lastname,
            address,
            homenumber,
            mobile,
            work,
            email,
            email2,
            email3) = row
            return Contact(id=str(id),
                                firstname=firstname,
                                lastname=lastname,
                                homenumber=homenumber,
                                work=work,
                                mobile=mobile,
                                email=email,
                                email2=email2,
                                email3=email3,
                                address=address)
        finally:
            cursor.close()


    def get_contact_count_by_group_id(self, group_id):
        cursor = self.connection.cursor()
        try:
            sql = "select count(id) from address_in_groups where group_id = %d" % int(group_id)
            cursor.execute(sql)
            return cursor.fetchone()[0]
        finally:
            cursor.close()


    def is_contact_in_group(self, contact_id, group_id):
        cursor = self.connection.cursor()
        try:
            sql = "select count(id) from address_in_groups where id = %d and group_id = %d" % (int(contact_id), int(group_id))
            cursor.execute(sql)
            return cursor.fetchone()[0] > 0
        finally:
            cursor.close()


    def destroy(self):
        self.connection.close()