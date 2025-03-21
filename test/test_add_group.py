# -*- coding: utf-8 -*-
from model.group import Group



def test_add_group(app):
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name="jgff", header="jhfd", footer="nhvcvx")
    app.group.create(group)
    app.group.open_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_empty_group(app):
#     app.group.open_groups_page()
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#     app.return_to_home_page()

