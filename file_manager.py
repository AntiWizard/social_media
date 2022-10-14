import csv
import datetime
import os.path
import shutil

import utils

category_option = {"person": ["first_name", "last_name", "email", "follower", "following"],
                   "post": ["author", "title", "creation_date", "content"],
                   "group": ["admin", "group_name", "creation_date", "members"]}


def create_management_file(file_name):
    if file_name in category_option:
        utils.file_not_exist(file_name)
        with open("{}.txt".format(file_name), 'w', newline='') as file:
            writer = csv.DictWriter(file, category_option[file_name])
            writer.writeheader()
    else:
        raise TypeError("file_name invalid")


def create_backup(file_name):
    if os.path.isfile("{}.txt".format(file_name)):
        try:
            shutil.copy("{}.txt".format(file_name),
                        "{}.txt".format(file_name + "_" +
                                        str(datetime.datetime.now())
                                        .strip()
                                        .replace(" ", "_")
                                        .replace(":", "-")
                                        .split(".")[0]))

        except Exception as e:
            print(e)


def add_item(category, check_record, item_field):
    utils.file_exist(category)
    with open("{}.txt".format(category), 'a', newline="") as file:
        writer = csv.writer(file)
        if not utils.search_record(category, check_record):
            return writer.writerow(item_field)


def update_item(category, check_record, item_field):
    utils.file_exist(category)
    delete_item(category, check_record)
    with open("{}.txt".format(category), 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(item_field)


def update_two_item(category, check_record, second_record, item_field, second_field):
    utils.file_exist(category)
    delete_two_item(category, check_record, second_record)
    with open("{}.txt".format(category), 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(item_field)
        writer.writerow(second_field)


def delete_item(category, check_record):
    utils.file_exist(category)
    with open('{}.txt'.format(category), 'r') as source_file, open('{}.txt'.format("temp_" + category), 'w',
                                                                   newline="") as result_file:
        writer = csv.writer(result_file)
        for row in csv.reader(source_file):
            if check_record not in row:
                writer.writerow(row)
    os.remove('{}.txt'.format(category))
    os.rename('{}.txt'.format("temp_" + category), '{}.txt'.format(category))


def delete_two_item(category, check_record, second_record):
    utils.file_exist(category)
    with open('{}.txt'.format(category), 'r') as source_file, open('{}.txt'.format("temp_" + category), 'w',
                                                                   newline="") as result_file:
        writer = csv.writer(result_file)
        for row in csv.reader(source_file):
            if check_record not in row and second_record not in row:
                writer.writerow(row)
    os.remove('{}.txt'.format(category))
    os.rename('{}.txt'.format("temp_" + category), '{}.txt'.format(category))


def follow(category, record_follower, record_following):
    utils.file_exist("person")
    delete_item(category, record_follower)
    delete_item(category, record_following)
    with open("person.txt", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(record_follower)
        writer.writerow(record_following)
