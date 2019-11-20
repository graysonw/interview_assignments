import datetime
from dateutil import parser
import random
import logging


# We rename the fields to match our DW schema
def add_friendly_fields(friendly_user: dict):
    friendly_user["friendly_id"] = friendly_user.pop("id")
    friendly_user["friendly_last_active_date"] = parser.parse(friendly_user.pop("last_active_date")).date()
    friendly_user["friendly_classification"] = friendly_user.pop("user_type_classification")
    friendly_user["location"] = friendly_user.pop("practice_location")
    return friendly_user


# Create a record that only contains the fields we're matching on. This is necessary because of
# the possibility that there might be two users with the same first and last name, but different
# locations and/or specialties, especially at the page break from the Friendly API. We keep track
# of the previous matches so that we're not double counting.
def create_matching_dict(new_record: dict):
    return {"firstname": new_record["firstname"],
            "lastname": new_record["lastname"],
            "specialty": new_record["specialty"],
            "location": new_record["location"]}


# This needs to be in tuple form for executemany()
def create_tuple(new_record: dict):
    return (new_record.get("company2_user_id", None),
            new_record.get("friendly_id", None),
            new_record.get("practice_id", None),
            new_record.get("firstname", None),
            new_record.get("lastname", None),
            new_record.get("company2_classification", None),
            new_record.get("friendly_classification", None),
            new_record.get("specialty", None),
            new_record.get("platform_registered_on", None),
            new_record.get("company2_last_active_date", None),
            new_record.get("friendly_last_active_date", None),
            new_record.get("location", None),
            new_record.get("is_active_company2", None),
            new_record.get("is_active_friendly", None))


def match_data(friendly_users: list, company2_users: list, prev_rows: list, print_rows=False):
    num_matches, rows_to_insert, rows_to_print = 0, [], []
    for friendly_user in friendly_users:
        matched = False

        # Loop over all the users in our database.
        for company2_user in company2_users:
            # Match on lastname, firstname, specialty and practice_location
            if friendly_user["lastname"] == company2_user["lastname"] and \
                    friendly_user["firstname"] == company2_user["firstname"] and \
                    friendly_user["specialty"] == company2_user["specialty"] and \
                    friendly_user["practice_location"] == company2_user["location"]:  # we have a match
                matched = True
                new_record = dict(company2_user)
                new_record.update(add_friendly_fields(friendly_user))
                new_record["is_active_company2"] = True if (datetime.date(2017, 2, 2) -
                                                            new_record[
                                                                "company2_last_active_date"]).days <= 30 else False
                new_record["is_active_friendly"] = True \
                    if (datetime.date(2017, 2, 2) -
                        new_record["friendly_last_active_date"]).days <= 30 else False

                if rows_to_print:
                    rows_to_print.append(new_record)
                if create_matching_dict(new_record) not in prev_rows:
                    rows_to_insert.append(create_tuple(new_record))
                num_matches += 1

                # Remove the matched user from the Company2 rows. Then after we're done with the Friendly rows, insert
                # the remaining Company2 users into the database.
                company2_users.remove(company2_user)

                # We found a match, no need to continue
                break
        # Go through the Friendly users who don't exist in our database.
        if not matched:
            new_record = add_friendly_fields(dict(friendly_user))
            new_record["is_active_friendly"] = True if (datetime.date(2017, 2, 2) -
                        new_record["friendly_last_active_date"]).days <= 30 else False
            if create_matching_dict(new_record) not in prev_rows:
                if print_rows:
                    rows_to_print.append(new_record)
                rows_to_insert.append(create_tuple(new_record))

    # Go through our users who don't exist in the Friendly database.
    for company2_user in company2_users:
        if create_matching_dict(company2_user) not in prev_rows:
            company2_user["is_active_company2"] = True if (datetime.date(2017, 2, 2) - company2_user[
                "company2_last_active_date"]).days <= 30 else False
            if print_rows:
                rows_to_print.append(company2_user)
            rows_to_insert.append(create_tuple(company2_user))

    # This is just for the assignment--print 10 random rows that we're inserting.
    if print_rows:
        if len(rows_to_print) > 10:
            for i in range(10):
                logging.info(random.choice(rows_to_print))
            # print(rows_to_print)

    return num_matches, rows_to_insert
