class ApiEndpoint:
    TOKEN = "https://beta-api.crunchyroll.com/auth/v1/token"
    ME = "https://beta-api.crunchyroll.com/accounts/v1/me"
    PROFILE = "https://beta-api.crunchyroll.com/accounts/v1/me/profile"
    SEARCH = "https://beta-api.crunchyroll.com/content/v1/search"
    INDEX = "https://beta-api.crunchyroll.com/index/v2"
    OBJECTS = "https://beta-api.crunchyroll.com/cms/v2{bucket}/objects/{id}"
    STREAMS = "https://beta-api.crunchyroll.com/cms/v2{bucket}/videos/{id}/streams"
    SERIES = "https://beta-api.crunchyroll.com/cms/v2{bucket}/series/{id}"
    SEASONS = "https://beta-api.crunchyroll.com/cms/v2{bucket}/seasons"
    EPISODES = "https://beta-api.crunchyroll.com/cms/v2{bucket}/episodes"
