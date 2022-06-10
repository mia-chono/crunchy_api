import unittest

from crunchy_api.crunchy_obj.episode_stream import EpisodeStream
from crunchy_api.crunchy_obj.streams import Streams
from crunchy_api.crunchy_obj.subtitles import Subtitle

json = dict({
    "audio_locale": "ja-JP",
    "subtitles": {
        "en-US": {
            "locale": "en-US",
            "url": "us_link",
            "format": "ass"
        },
        "es-419": {
            "locale": "es-419",
            "url": "es_link",
            "format": "ass"
        },
        "es-ES": {
            "locale": "es-ES",
            "url": "es_link",
            "format": "ass"
        },
        "pt-BR": {
            "locale": "pt-BR",
            "url": "pt_link",
            "format": "ass"
        },
        "ar-ME": {
            "locale": "ar-ME",
            "url": "ar_link",
            "format": "ass"
        },
        "it-IT": {
            "locale": "it-IT",
            "url": "it_link",
            "format": "ass"
        },
        "de-DE": {
            "locale": "de-DE",
            "url": "de_link",
            "format": "ass"
        },
        "ru-RU": {
            "locale": "ru-RU",
            "url": "ru_link",
            "format": "ass"
        },
        "fr-FR": {
            "locale": "fr-FR",
            "url": "fr_link",
            "format": "ass"
        }
    },
    "streams": {
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
    },
    "bifs": [
        "bif_link"
    ]
})


class TestEpisodeStreamCrunchyObj(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ep_stream = EpisodeStream(json)

    @classmethod
    def tearDownClass(cls):
        cls.ep_stream = None

    def test_audio_locale(self):
        self.assertEqual(self.ep_stream.audio_locale, json["audio_locale"])

    def test_subtitles(self):
        self.assertIsInstance(self.ep_stream.subtitles, dict)

    def test_subtitles_len(self):
        self.assertEqual(len(self.ep_stream.subtitles), len(json["subtitles"]))

    def test_subtitles_values(self):
        for subtitle in self.ep_stream.subtitles.values():
            self.assertIsInstance(subtitle, Subtitle)

    def test_subtitles_keys(self):
        self.assertEqual(self.ep_stream.subtitles.keys(), json["subtitles"].keys())

    def test_streams(self):
        self.assertIsInstance(self.ep_stream.streams, Streams)

    def test_bifs(self):
        self.assertEqual(self.ep_stream.bifs, json["bifs"])
