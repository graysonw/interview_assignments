import unittest
import datetime


class TestMatching(unittest.TestCase):

    # First unit test. There are of course a lot more we could/should do, but 
    # this is enough to get started/show the general idea.
    def test_matching(self):
        from transform import match_data
        friendly_data = [
            {
                "firstname": "Roger",
                "id": 111941,
                "last_active_date": "2017-01-04",
                "lastname": "Aaberg",
                "practice_location": "belk",
                "specialty": "Orthopedics",
                "user_type_classification": "Contributor"
            },
            {
                "firstname": "Joseph",
                "id": 15921,
                "last_active_date": "2017-01-08",
                "lastname": "Aadland",
                "practice_location": "concord",
                "specialty": "Orthopedics",
                "user_type_classification": "Contributor"
            },
            {
                "firstname": "Kimberly",
                "id": 20597,
                "last_active_date": "2017-01-04",
                "lastname": "Aaron",
                "practice_location": "avon",
                "specialty": "Cardiology",
                "user_type_classification": "Leader"
            }]
        company2_data = [{"company2_user_id": 666015,
                          "practice_id": 28,
                          "firstname": "Kimberly",
                          "lastname": "Aaron",
                          "classification": "contributor",
                          "specialty": "Cardiology",
                          "platform_registered_on": "website",
                          "company2_last_active_date": datetime.date(2016, 12, 27),
                          "practice_name": "generic_clinic_27",
                          "location": "avon"},
                         {"company2_user_id": 251043,
                          "practice_id": 35,
                          "firstname": "Steven",
                          "lastname": "Michael",
                          "classification": "contributor",
                          "specialty": "Family Medicine",
                          "platform_registered_on": "website",
                          "company2_last_active_date": datetime.date(2016, 10, 15),
                          "practice_name": "generic_clinic_35",
                          "location": "bellingham"},
                         {"company2_user_id": 45015,
                          "practice_id": 63,
                          "firstname": "Emma",
                          "lastname": "Aaron",
                          "classification": "popular",
                          "specialty": "Dermatology",
                          "platform_registered_on": "mobile",
                          "company2_last_active_date": datetime.date(2017, 1, 5),
                          "practice_name": "generic_clinic_63",
                          "location": "chickasaw"}]
        num_matches, result = match_data(friendly_data, company2_data, [])
        self.assertEqual(num_matches, 1)


if __name__ == '__main__':
    unittest.main()
