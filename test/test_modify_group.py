from model.group import Group

def test_modify_group_name(app):
    app.group.open_groups_page()
    app.group.modify_first_group(Group(name="New Group"))
    app.return_to_home_page()


def test_modify_group_header(app):
    app.group.open_groups_page()
    app.group.modify_first_group(Group(header="New Header"))
    app.return_to_home_page()
