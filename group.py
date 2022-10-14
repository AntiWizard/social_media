import datetime

import file_manager
import utils


class Group:
    def __init__(self):
        self.__admin = None
        self.__group_name = None
        self.__creation_date = str(datetime.datetime.now())
        self.__members = "None"

    @property
    def admin(self):
        return self.__admin

    @admin.setter
    def admin(self, value):
        record = utils.search_record("person", utils.check_valid_email(value))
        if not record:
            raise TypeError("admin not exist as person")
        self.__admin = record[2]

    @property
    def group_name(self):
        return self.__group_name

    @group_name.setter
    def group_name(self, value):
        self.__group_name = utils.check_valid_name(value)

    @property
    def creation_date(self):
        return self.__creation_date

    def add_member(self, admin, member_email):
        record = utils.search_record(self.__class__.__name__, utils.check_valid_email(admin))
        if record:
            self.__members = record[3]
        else:
            raise TypeError("admin not found")
        if member_email != admin and utils.search_record("person", member_email):
            members = self.__members
            self.__members = member_email if members == "None" else self.__members + "|" + member_email
            record[3] = self.__members
            return record
        else:
            raise TypeError("person not exist")

    def remove_member(self, admin, member_email):
        record = utils.search_record(self.__class__.__name__, utils.check_valid_email(admin))
        if record:
            self.__members = record[3]
        else:
            raise TypeError("Not found this admin")
        self.__members = record[3]
        if member_email in self.__members and member_email != admin:
            self.__members = "None" if "|" not in self.__members else self.__members.replace(member_email, "")
            if "||" in self.__members:
                self.__members.replace("||", "|")
            record[3] = self.__members
            return record
        else:
            raise TypeError("member not existed in this group")

    def add(self):
        record = utils.search_record(self.__class__.__name__, self.__admin)
        if not record and self.__admin and self.__group_name:
            record = [self.__admin, self.__group_name, self.__creation_date, self.__members]
            file_manager.add_item(self.__class__.__name__, self.__admin, record)
        else:
            raise TypeError("group exist or invalid")

    def update_by_admin(self, old_admin, new_admin):
        if not utils.search_record("person", utils.check_valid_email(old_admin)) or \
                not utils.search_record("person", utils.check_valid_email(new_admin)):
            raise TypeError("admin not exist as person")
        record = utils.search_record(self.__class__.__name__, old_admin)
        if record:
            record[0] = new_admin
            file_manager.update_item(self.__class__.__name__, old_admin, record)
        else:
            raise TypeError("group not exist")

    def update_by_group_name(self, old_group_name, new_group_name):
        record = utils.search_record(self.__class__.__name__, utils.check_valid_name(old_group_name))
        if not record or utils.search_record(self.__class__.__name__, new_group_name):
            raise TypeError("group not found or exist")
        record[1] = new_group_name
        file_manager.update_item(self.__class__.__name__, old_group_name, record)

    def update_by_members(self, admin, member_email, member_func):
        try:
            record = member_func(utils.check_valid_email(admin), member_email)  # func -> add_member | remove_member
            if admin:
                file_manager.update_item(self.__class__.__name__, admin, record)
            else:
                raise TypeError("group not exist")
        except Exception as e:
            raise e

    def delete_by_admin(self, admin):
        record = utils.search_record(self.__class__.__name__, utils.check_valid_email(admin))
        if record:
            file_manager.delete_item(self.__class__.__name__, admin)
        else:
            raise TypeError("admin not found")

    def delete_by_group_name(self, group_name):
        record = utils.search_record(self.__class__.__name__, group_name)
        if record:
            file_manager.delete_item(self.__class__.__name__, group_name)
        else:
            raise TypeError("group not found")
