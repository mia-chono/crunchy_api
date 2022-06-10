import unittest

from crunchy_api.crunchy_obj.cms import CMS

json = {
    "bucket": "/FR/M3/crunchyroll",
    "policy": "fake_policy",
    "signature": "fake_signature",
    "key_pair_id": "fake_key_pair_id",
    "expires": "2022-6-10T17:58:59Z"
}


class TestCMSCrunchyObj(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cms = CMS(json)

    @classmethod
    def tearDownClass(cls):
        cls.cms = None

    def test_bucket(self):
        self.assertEqual(self.cms.bucket, json["bucket"])

    def test_policy(self):
        self.assertEqual(self.cms.policy, json["policy"])

    def test_signature(self):
        self.assertEqual(self.cms.signature, json["signature"])

    def test_key_pair_id(self):
        self.assertEqual(self.cms.key_pair_id, json["key_pair_id"])

    def test_expires(self):
        self.assertEqual(self.cms.expires, json["expires"])
