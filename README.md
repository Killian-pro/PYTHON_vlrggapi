# vlrggapi

An Unofficial REST API for [vlr.gg](https://www.vlr.gg/), a site for Valorant Esports match and news coverage.

Built by [CLUZEL Killian](https://github.com/Killian-pro)

### `/team/9133`

- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- Response:
  ```python
  {
      "data": {
          "status": 200,
          'segments': [
              {
                  'title': str,
                  'description': str,
                  'date': str,
                  'author': str,
                  'url_path': str
              }
          ],
      }
  }
  ```

## Installation

```
$ pip3 install -r requirements.txt
```

### Usage

```
uvicorn main:app
```