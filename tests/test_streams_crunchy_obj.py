import unittest

from crunchy_api.crunchy_obj.streams import Streams

json = dict({
    "adaptive_dash": {
        "": {
            "hardsub_locale": "",
            "url": "dash_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "dash_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "dash_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "dash_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "dash_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "dash_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "dash_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "dash_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "dash_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "dash_fr_link",
            "vcodec": "h264"
        }
    },
    "adaptive_hls": {
        "": {
            "hardsub_locale": "",
            "url": "hls_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "hls_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "hls_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "hls_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "hls_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "hls_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "hls_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "hls_fr_link",
            "vcodec": "h264"
        }
    },
    "download_hls": {
        "": {
            "hardsub_locale": "",
            "url": "hls_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "hls_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "hls_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "hls_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "hls_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "hls_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "hls_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "hls_fr_link",
            "vcodec": "h264"
        }
    },
    "drm_adaptive_dash": {
        "": {
            "hardsub_locale": "",
            "url": "dash_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "dash_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "dash_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "dash_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "dash_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "dash_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "dash_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "dash_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "dash_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "dash_fr_link",
            "vcodec": "h264"
        }
    },
    "drm_adaptive_hls": {
        "": {
            "hardsub_locale": "",
            "url": "hls_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "hls_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "hls_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "hls_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "hls_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "hls_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "hls_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "hls_fr_link",
            "vcodec": "h264"
        }
    },
    "drm_download_hls": {
        "": {
            "hardsub_locale": "",
            "url": "hls_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "hls_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "hls_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "hls_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "hls_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "hls_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "hls_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "hls_fr_link",
            "vcodec": "h264"
        }
    },
    "trailer_dash": {
        "": {
            "hardsub_locale": "",
            "url": "dash_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "dash_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "dash_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "dash_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "dash_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "dash_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "dash_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "dash_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "dash_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "dash_fr_link",
            "vcodec": "h264"
        }
    },
    "trailer_hls": {
        "": {
            "hardsub_locale": "",
            "url": "hls_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "hls_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "hls_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "hls_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "hls_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "hls_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "hls_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "hls_fr_link",
            "vcodec": "h264"
        }
    },
    "vo_adaptive_dash": {
        "": {
            "hardsub_locale": "",
            "url": "dash_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "dash_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "dash_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "dash_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "dash_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "dash_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "dash_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "dash_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "dash_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "dash_fr_link",
            "vcodec": "h264"
        }
    },
    "vo_adaptive_hls": {
        "": {
            "hardsub_locale": "",
            "url": "hls_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "hls_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "hls_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "hls_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "hls_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "hls_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "hls_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "hls_fr_link",
            "vcodec": "h264"
        }
    },
    "vo_drm_adaptive_dash": {
        "": {
            "hardsub_locale": "",
            "url": "dash_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "dash_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "dash_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "dash_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "dash_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "dash_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "dash_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "dash_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "dash_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "dash_fr_link",
            "vcodec": "h264"
        }
    },
    "vo_drm_adaptive_hls": {
        "": {
            "hardsub_locale": "",
            "url": "hls_link",
            "vcodec": "h264"
        },
        "en-US": {
            "hardsub_locale": "en-US",
            "url": "hls_en_link",
            "vcodec": "h264"
        },
        "es-LA": {
            "hardsub_locale": "es-LA",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "es-ES": {
            "hardsub_locale": "es-ES",
            "url": "hls_es_link",
            "vcodec": "h264"
        },
        "pt-BR": {
            "hardsub_locale": "pt-BR",
            "url": "hls_pt_link",
            "vcodec": "h264"
        },
        "ar-ME": {
            "hardsub_locale": "ar-ME",
            "url": "hls_ar_link",
            "vcodec": "h264"
        },
        "it-IT": {
            "hardsub_locale": "it-IT",
            "url": "hls_it_link",
            "vcodec": "h264"
        },
        "de-DE": {
            "hardsub_locale": "de-DE",
            "url": "hls_de_link",
            "vcodec": "h264"
        },
        "ru-RU": {
            "hardsub_locale": "ru-RU",
            "url": "hls_ru_link",
            "vcodec": "h264"
        },
        "fr-FR": {
            "hardsub_locale": "fr-FR",
            "url": "hls_fr_link",
            "vcodec": "h264"
        }
    }
})


class TestStreamsCrunchyObj(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.streams = Streams(json)

    @classmethod
    def tearDownClass(cls):
        cls.streams = None

    def test_number_of_adaptive_dash(self):
        self.assertEqual(len(self.streams.adaptive_dash), len(json["adaptive_dash"]))

    def test_number_of_adaptive_hls(self):
        self.assertEqual(len(self.streams.adaptive_hls), len(json["adaptive_hls"]))

    def test_number_of_download_hls(self):
        self.assertEqual(len(self.streams.download_hls), len(json["download_hls"]))

    def test_number_of_drm_adaptive_dash(self):
        self.assertEqual(len(self.streams.drm_adaptive_dash), len(json["drm_adaptive_dash"]))

    def test_number_of_drm_adaptive_hls(self):
        self.assertEqual(len(self.streams.drm_adaptive_hls), len(json["drm_adaptive_hls"]))

    def test_number_of_drm_download_hls(self):
        self.assertEqual(len(self.streams.drm_download_hls), len(json["drm_download_hls"]))

    def test_number_of_trailer_dash(self):
        self.assertEqual(len(self.streams.trailer_dash), len(json["trailer_dash"]))

    def test_number_of_trailer_hls(self):
        self.assertEqual(len(self.streams.trailer_hls), len(json["trailer_hls"]))

    def test_number_of_vo_adaptive_dash(self):
        self.assertEqual(len(self.streams.vo_adaptive_dash), len(json["vo_adaptive_dash"]))

    def test_number_of_vo_adaptive_hls(self):
        self.assertEqual(len(self.streams.vo_adaptive_hls), len(json["vo_adaptive_hls"]))

    def test_number_of_vo_drm_adaptive_dash(self):
        self.assertEqual(len(self.streams.vo_drm_adaptive_dash), len(json["vo_drm_adaptive_dash"]))

    def test_number_of_vo_drm_adaptive_hls(self):
        self.assertEqual(len(self.streams.vo_drm_adaptive_hls), len(json["vo_drm_adaptive_hls"]))

    def test_adaptive_dash_stream_content(self):
        self.assertEqual(self.streams.adaptive_dash[""].url, json["adaptive_dash"][""]["url"])
        self.assertEqual(self.streams.adaptive_dash[""].vcodec, json["adaptive_dash"][""]["vcodec"])
        self.assertEqual(self.streams.adaptive_dash[""].hardsub_locale, json["adaptive_dash"][""]["hardsub_locale"])
