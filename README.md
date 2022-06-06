# Crunchyroll API (BETA version)
## What is it?
This code allows you to connect to crunchyroll and interact with its api.

Currently, it can be used to interact with the following elements to get information:
 - get all seasons of an anime
 - get all episodes of a season
 - get a specific episode
 - get streams of a specific episode

## Installation ️
```bash
pip install git+https://github.com/mia-chono/crunchy_api@master
```

## Example Code
This API requires **a valid CR account** to work.

```python
from crunchy_api import CrunchyApi

cr = CrunchyApi(
    basic_token="BASIC_TOKEN",
    username="USERNAME",
    password="PASSWORD"
)

# Returns the account information and initializes the session
account = cr.login()

series_id = "GYWEMDGEY"  # id of the series `Senyu`
season_id = cr.get_seasons_from_series_id(series_id)[0].id
episode = cr.get_episodes_from_season_id(season_id)
# get the first hls url (m3u8) without embedded subs
hls_url = cr.get_streams(episode[0].id).streams.adaptive_hls[""].url
```