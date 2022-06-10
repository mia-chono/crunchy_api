import unittest
from datetime import datetime, timedelta

from crunchy_api.crunchy_obj.account import Account
from crunchy_api.crunchy_obj.cms import CMS

json = dict({
    "access_token": "test_access_token",
    "refresh_token": "test_refresh_token",
    "expires_in": 300,
    "token_type": "Bearer",
    "scope": "account content offline_access",
    "country": "FR",
    "account_id": "fake_account_id",
    "cms": {
        "bucket": "/FR/M3/crunchyroll",
        "policy": "fake_policy",
        "signature": "fake_signature",
        "key_pair_id": "fake_key_pair_id",
        "expires": "2022-6-10T17:58:59Z"
    },
    "service_available": True,
    "default_marketing_opt_in": True,
    "avatar": "yuzu-3.png",
    "cr_beta_opt_in": True,
    "crleg_email_verified": False,
    "email": "fake@email.com",
    "mature_content_flag_manga": "1",
    "maturity_rating": "M3",
    "opt_out_android_in_app_marketing": False,
    "opt_out_free_trials": True,
    "opt_out_new_media_queue_updates": False,
    "opt_out_newsletters": True,
    "opt_out_pm_updates": False,
    "opt_out_promotional_updates": True,
    "opt_out_queue_updates": True,
    "opt_out_store_deals": True,
    "preferred_communication_language": "en-US",
    "preferred_content_subtitle_language": "fr-FR",
    "qa_user": False,
    "username": "fake_username",
    "wallpaper": "one_picture.png"
})


class TestAccountCrunchyObj(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expires_in = datetime.utcnow() + timedelta(seconds=json["expires_in"])
        cls.account = Account(json)

    @classmethod
    def tearDownClass(cls):
        cls.account = None

    def test_access_token(self):
        self.assertEqual(self.account.access_token, json["access_token"])

    def test_refresh_token(self):
        self.assertEqual(self.account.refresh_token, json["refresh_token"])

    def test_expires_in(self):
        self.assertEqual(self.account.expires_in, self.expires_in)

    def test_token_type(self):
        self.assertEqual(self.account.token_type, json["token_type"])

    def test_scope(self):
        self.assertEqual(self.account.scope, json["scope"])

    def test_country(self):
        self.assertEqual(self.account.country, json["country"])

    def test_account_id(self):
        self.assertEqual(self.account.account_id, json["account_id"])

    def test_cms(self):
        self.assertIsInstance(self.account.cms, CMS)
        self.assertEqual(self.account.cms.bucket, json["cms"]["bucket"])
        self.assertEqual(self.account.cms.policy, json["cms"]["policy"])
        self.assertEqual(self.account.cms.signature, json["cms"]["signature"])
        self.assertEqual(self.account.cms.key_pair_id, json["cms"]["key_pair_id"])
        self.assertEqual(self.account.cms.expires, json["cms"]["expires"])

    def test_avatar(self):
        self.assertEqual(self.account.avatar, json["avatar"])

    def test_cr_beta_opt_in(self):
        self.assertTrue(self.account.has_beta)

    def test_crleg_email_verified(self):
        self.assertFalse(self.account.email_verified)

    def test_email(self):
        self.assertEqual(self.account.email, json["email"])

    def test_maturity_rating(self):
        self.assertEqual(self.account.maturity_rating, json["maturity_rating"])

    def test_account_language(self):
        self.assertEqual(self.account.account_language, json["preferred_communication_language"])

    def test_subtitles_language(self):
        self.assertEqual(self.account.subtitles_language, json["preferred_content_subtitle_language"])

    def test_username(self):
        self.assertEqual(self.account.username, json["username"])
