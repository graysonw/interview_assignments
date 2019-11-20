create_table_query = f"create table if not exists usermatching ( \
`id` int(11) NOT NULL AUTO_INCREMENT, \
`company2_user_id` int(11) DEFAULT NULL, \
`friendly_id` int(11) DEFAULT NULL, \
`practice_id` int(11) DEFAULT NULL, \
`firstname` varchar(50) DEFAULT NULL, \
`lastname` varchar(50) DEFAULT NULL, \
`company2_classification` varchar(50) DEFAULT NULL, \
`friendly_classification` varchar(50) DEFAULT NULL, \
`specialty` varchar(50) DEFAULT NULL, \
`platform_registered_on` varchar(25) DEFAULT NULL, \
`company2_last_active_date` date DEFAULT NULL, \
`friendly_last_active_date` date DEFAULT NULL, \
`location` varchar(50) DEFAULT NULL, \
`is_active_company2` tinyint(1) DEFAULT NULL, \
`is_active_friendly` tinyint(1) DEFAULT NULL, \
PRIMARY KEY (`id`))"

insert_table_query = f"INSERT IGNORE INTO usermatching (\
company2_user_id, \
friendly_id, \
practice_id, \
firstname, \
lastname, \
company2_classification, \
friendly_classification, \
specialty, \
platform_registered_on, \
company2_last_active_date, \
friendly_last_active_date, \
location, \
is_active_company2, \
is_active_friendly) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# We have different queries based on whether or not we're going from the 
# first page, last page, or an intermediate page in the Friendly API. For the 
# first page, there might be records in our database that are before the first
# user in Friendly alphabetically. Likewise, for the last page, there might be
# users in our DB after the last user in Friendly. We need to make sure we don't 
# miss these.
get_first_page_query = f"select \
user.id AS company2_user_id, \
practice_id, \
firstname, \
lastname, \
classification, \
specialty, \
platform_registered_on, \
last_active_date AS company2_last_active_date, \
name AS practice_name, \
location \
from user join user_practice on user.`practice_id` = user_practice.id \
where lastname < %s or (lastname = %s and firstname <= %s) \
order by user.lastname, user.firstname"

get_middle_page_query = f"select \
user.id AS company2_user_id, \
practice_id, \
firstname, \
lastname, \
classification, \
specialty, \
platform_registered_on, \
last_active_date AS company2_last_active_date, \
name AS practice_name, \
location \
from user join user_practice on user.`practice_id` = user_practice.id \
where lastname > %s and lastname < %s or \
((lastname = %s and firstname >= %s) or \
(lastname = %s and firstname <= %s)) order by user.lastname, user.firstname"

get_last_page_query = f"select \
user.id AS company2_user_id, \
practice_id, \
firstname, \
lastname, \
classification, \
specialty, \
platform_registered_on, \
last_active_date AS company2_last_active_date, \
name AS practice_name, \
location \
from user join user_practice on user.`practice_id` = user_practice.id \
where lastname > %s or (lastname = %s and firstname >= %s) \
order by user.lastname, user.firstname"
