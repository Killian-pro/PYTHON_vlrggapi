# vlrggapi

An Unofficial REST API for [vlr.gg](https://www.vlr.gg/), a site for Valorant Esports match and news coverage.

Built by [CLUZEL Killian](https://github.com/Killian-pro)

### `/team/9133`

- Method: `GET`
- Response:
  ```python
  {
      "data": {
          "status": 200,
          'segments': [
              {
                  'name': str,
                  'short_name': str,
                  'logo': img,
                  'country': str,
                  'id': id,
                  'roster' : [],
                  'matches' : []
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
