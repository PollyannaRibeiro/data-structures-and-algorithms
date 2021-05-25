class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


parent.add_user("Mother")
parent.add_user("Father")
child.add_user("Daughter")
child.add_user("Son")
sub_child.add_user("Dog")
sub_child.add_user("Cat")
sub_child.add_user("Guinea pig")


def is_user_in_group(user, group):

    if len(user) == 0:
        return False

    for username in group.users:
        if username == user:
            return True
    # recursion
    for inner_group in group.groups:
        if is_user_in_group(user, inner_group):
            return True
    return False

# test

print("Pass" if (is_user_in_group("Dog", parent)) else "Fail")
print("Pass" if (is_user_in_group("Cat", sub_child)) else "Fail")
print("Pass" if (not is_user_in_group("Mother", child)) else "Fail")
print("Pass" if (not is_user_in_group("Hamster", parent)) else "Fail") # not found in the group
print("Pass" if (not is_user_in_group("", parent)) else "Fail") # empty user


