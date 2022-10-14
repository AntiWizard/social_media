import file_manager, post, group, relation, person


def start_app():
    # for item in file_manager.category_option:
    #     file_manager.create_management_file(item)
    return


def create_file(file_name):
    file_manager.create_management_file(file_name)


def add_person(*args):
    persons = person.Person()
    persons.first_name = args[0]
    persons.last_name = args[1]
    persons.email = args[2]
    persons.add()


def follow(*args):
    persons = person.Person()
    persons.follower = args[0]
    persons.following = args[1]
    persons.follow()


def unfollow(*args):
    persons = person.Person()
    persons.follower = args[0]
    persons.following = args[1]
    persons.unfollow()


def add_group(*args):
    groups = group.Group()
    groups.admin = args[0]
    groups.group_name = args[1]
    groups.add()


def add_member_to_group(*args):
    groups = group.Group()
    groups.admin = args[0]
    groups.group_name = args[1]
    groups.update_by_members(args[0], args[1], groups.add_member)


def remove_member_to_group(*args):
    groups = group.Group()
    groups.admin = args[0]
    groups.group_name = args[1]
    groups.update_by_members(args[0], args[1], groups.remove_member)


def add_post(*args):
    posts = post.Post()
    posts.author = args[0]
    posts.title = args[1]
    posts.content = args[2]
    posts.add()


def see_posts(user, friend):
    rel = relation.Relation()
    rel.user = user
    rel.friend = friend
    rel.get_all_post_friend()


def see_follower(user, friend):
    rel = relation.Relation()
    rel.user = user
    rel.friend = friend
    rel.get_all_follower_friend()


def see_following(user, friend):
    rel = relation.Relation()
    rel.user = user
    rel.friend = friend
    rel.get_all_following_friend()


if __name__ == '__main__':
    start_app()
