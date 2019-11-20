import unittest
import datetime


class TestMatching(unittest.TestCase):

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
        doximity_data = [{"doximity_user_id": 666015,
                          "practice_id": 28,
                          "firstname": "Kimberly",
                          "lastname": "Aaron",
                          "classification": "contributor",
                          "specialty": "Cardiology",
                          "platform_registered_on": "website",
                          "doximity_last_active_date": datetime.date(2016, 12, 27),
                          "practice_name": "generic_clinic_27",
                          "location": "avon"},
                         {"doximity_user_id": 251043,
                          "practice_id": 35,
                          "firstname": "Steven",
                          "lastname": "Michael",
                          "classification": "contributor",
                          "specialty": "Family Medicine",
                          "platform_registered_on": "website",
                          "doximity_last_active_date": datetime.date(2016, 10, 15),
                          "practice_name": "generic_clinic_35",
                          "location": "bellingham"},
                         {"doximity_user_id": 45015,
                          "practice_id": 63,
                          "firstname": "Emma",
                          "lastname": "Aaron",
                          "classification": "popular",
                          "specialty": "Dermatology",
                          "platform_registered_on": "mobile",
                          "doximity_last_active_date": datetime.date(2017, 1, 5),
                          "practice_name": "generic_clinic_63",
                          "location": "chickasaw"}]
        num_matches, result = match_data(friendly_data, doximity_data, [])
        self.assertEqual(num_matches, 1)


if __name__ == '__main__':
    unittest.main()
