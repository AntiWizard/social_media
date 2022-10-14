import file_manager
import utils


class Person:
    def __init__(self):
        self.__first_name = None
        self.__last_name = None
        self.__email = None
        self.__follower = "None"
        self.__following = "None"

    @property
    def first_name(self):
        return self.__first_name.lower()

    @first_name.setter
    def first_name(self, value):
        self.__first_name = utils.check_valid_name(value)

    @property
    def last_name(self):
        return self.__last_name.lower()

    @last_name.setter
    def last_name(self, value):
        self.__last_name = utils.check_valid_name(value)

    @property
    def email(self):
        return self.__email.lower()

    @email.setter
    def email(self, value):
        self.__email = utils.check_valid_email(value)

    @property
    def follower(self):
        return self.__follower

    @follower.setter
    def follower(self, value):
        record = utils.search_record(self.__class__.__name__, value)
        self.__follower = record[2]

    @property
    def following(self):
        return self.__following

    @following.setter
    def following(self, value):
        record = utils.search_record(self.__class__.__name__, value)
        self.__following = record[2]

    def get_list_field(self):
        follower = ""
        following = ""
        if self.__follower != "None":
            if "|" in self.__follower:
                follower = "|".join(self.__follower.split("|"))
        if self.__following != "None":
            if "|" in self.__following:
                following = "|".join(self.__following.split("|"))
        return [self.__first_name, self.__last_name, self.__email, follower, following]

    def add(self):
        if self.__first_name and self.__last_name and self.__email:
            file_manager.add_item(self.__class__.__name__, self.__email, self.get_list_field())
        else:
            raise TypeError("person invalid")

    def update_by_email(self, old_email, new_email):
        record = utils.search_record(self.__class__.__name__, utils.check_valid_email(old_email))
        if not record and utils.search_record(self.__class__.__name__, utils.check_valid_email(new_email)):
            raise TypeError("email invalid or exist")
        record[2] = new_email
        file_manager.update_item(self.__class__.__name__, old_email, record)

    def update_by_first_name(self, old_first_name, new_first_name):
        record = utils.search_record(self.__class__.__name__, utils.check_valid_name(old_first_name))
        if not record:
            raise TypeError("person not exist")
        record[0] = new_first_name
        file_manager.update_item(self.__class__.__name__, old_first_name, record)

    def update_by_last_name(self, old_last_name, new_last_name):
        record = utils.search_record(self.__class__.__name__, utils.check_valid_name(old_last_name))
        if not record:
            raise TypeError("person not exist")
        record[1] = new_last_name
        file_manager.update_item(self.__class__.__name__, old_last_name, record)

    def __update_by_follow(self, p_follower, p_following):
        file_manager.update_two_item(self.__class__.__name__, p_follower[2], p_following[2], p_follower,
                                     p_following)  # -> follower record

    def follow(self):
        p_follower = utils.search_record(self.__class__.__name__, self.__follower)
        p_following = utils.search_record(self.__class__.__name__, self.__following)
        if (p_follower[3] == "None" and p_following[3] == "None") or p_follower[2] not in p_following[3]:
            p_following[3] = p_follower[2] if p_following[3] == "None" else p_following[3] + "|" + p_follower[2]
            if p_following[2] not in p_follower[4]:
                p_follower[4] = p_following[2] if p_follower[4] == "None" else p_follower[4] + "|" + \
                                                                               p_follower[2]
        else:
            raise FileExistsError("follower was followed that person")

        self.__update_by_follow(p_follower, p_following)

    def unfollow(self):
        p_follower = utils.search_record(self.__class__.__name__, self.__follower)
        p_following = utils.search_record(self.__class__.__name__, self.__following)
        if p_follower[2] in p_following[3]:
            p_following[3] = "None" if p_following[3] == p_follower[2] else p_following[3].replace(p_follower[2], "")
            if "||" in p_following:
                p_following.replace("||", "|")
            if p_following[2] in p_follower[4]:
                p_follower[4] = "None" if p_follower[4] == p_following[2] else p_follower[4].replace(p_following[2], "")
                if "||" in p_following:
                    p_following.replace("||", "|")
        else:
            raise FileExistsError("follower was not followed that person")

        self.__update_by_follow(p_follower, p_following)
