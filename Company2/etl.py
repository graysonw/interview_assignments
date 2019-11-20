import logging
import time

import friendly
import config
import mysql_databases

import transform


def main():
    company2_instance = mysql_databases.Doximity(config.company2_mysql)
    dw_instance = mysql_databases.DW(config.dw_mysql)

    num_matches = 0
    prev_rows = []
    last_user = None

    for page in friendly.get_pages():
        rows_to_insert = []
        friendly_users = page["users"]

        if page["current_page"] == 1:  # first page
            company2_users = company2_instance.get_first_page(friendly_users[-1])
            last_user = friendly_users[-1]
        elif page["current_page"] == page["total_pages"]:  # last page
            company2_users = company2_instance.get_last_page(last_user)
        else: # some page in the middle
            company2_users = company2_instance.get_middle_page(
                last_user, friendly_users[-1])
            last_user = friendly_users[-1]

        temp_num_matches, rows_to_insert = transform.match_data(
                friendly_users, company2_users, prev_rows,
                print_rows=True if page["current_page"] == 1 else 0)
        prev_rows = list()
        prev_rows += [{"firstname": row[3],
                       "lastname": row[4],
                       "specialty": row[7],
                       "location": row[11]} for row in rows_to_insert]
        num_matches += temp_num_matches
        dw_instance.insert(rows_to_insert)
    logging.info(f"Matches: {num_matches}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # there is a timeit Python package. However, we don't need repeated
    # runs, just a rough idea of how long this takes to run.
    t0 = time.time()
    main()
    t1 = time.time()
    logging.info(f"Elapsed_time: {(t1 - t0) // 60} minutes, {(t1 - t0) % 60} seconds.")
