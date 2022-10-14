import utils


class Relation:
    def __init__(self):
        self.__user = None
        self.__friend = None

    @property
    def user(self):
        return self.__user.lower()

    @user.setter
    def user(self, value):
        self.__user = utils.check_valid_email(value)

    @property
    def friend(self):
        return self.__friend

    @friend.setter
    def friend(self, value):
        self.__friend = utils.check_valid_email(value)

    def check_relation(self, user, friend):
        r_user = utils.search_record("person", utils.check_valid_email(user))
        r_friend = utils.search_record("person", utils.check_valid_email(friend))
        if r_user and r_friend:
            if r_user[2] in r_friend[3] and r_friend[2] in r_user[4]:
                return True
            else:
                raise TypeError("wrong relation")
        else:
            raise TypeError("users not exist as person")

    def get_all_post_friend(self):
        if self.check_relation(self.__user, self.__friend):
            return utils.search_all_record("post", self.__friend)

    def get_all_follower_friend(self):
        if self.check_relation(self.__user, self.__friend):
            result = utils.search_record("person", self.__friend)[3]
            return result.split("|")

    def get_all_following_friend(self):
        if self.check_relation(self.__user, self.__friend):
            result = utils.search_record("person", self.__friend)[4]
            return result.split("|")
