
# Twitter Scrape Data
Twitter Scrap ini menggunakan Flask Framework dan lib snscrape
**ntscraper** :  <https://github.com/bocchilorenzo/ntscraper>

**Flask** :  <https://flask.palletsprojects.com/en/2.3.x>

# Introduction

Cara running Flask
```javascript
    python app.py
```

# API URL
```http
http://localhost:5000/api/twit
```

## Request
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `cari` | `string` | **Required**. Kata yang akan di cari |
| `limit` | `number` | **Required**. limit data yang diinginkan |
| `jenis` | `string` | **Required**. `hastag `/`term` 


## Example Request
ini adalah contoh request
```javascript
{
	"cari":"Bakso",
	"limit":5,
	"jenis":"term"
}
```



## Response Example
ini adalah response ketika disubmit
```javascript
{
  "data": [
    {
      "date": "Dec 7, 2023 · 8:49 AM UTC",
      "external-link": "",
      "gifs": [],
      "is-retweet": false,
      "link": "https://twitter.com/Alfordkun/status/1732683796594761871#m",
      "pictures": [],
      "quoted-post": {},
      "stats": {
        "comments": 0,
        "likes": 0,
        "quotes": 0,
        "retweets": 0
      },
      "text": "Jualan bakso laku ga ya ka",
      "user": {
        "avatar": "https://pbs.twimg.com/profile_images/1690731615901880320/6AViuxwv_bigger.png",
        "name": "al 📌Joki Spiral Abyss - @ after dm // WA // DC",
        "profile_id": "1690731615901880320",
        "username": "@Alfordkun"
      },
      "videos": []
    }
  ],
  "msg": "success",
  "status_code": 1,
  "total_data": 1
}
```

`msg` adalah  sebuah pesan 

`status_code` untuk atribut kode sukses atau tidak.

`data` kumpulan data hasil scrape


## Status Code Response
Status Code Response

| Status Code | Description |
| :--- | :--- |
| 0 | `error` |
| 1 | `success` |

## Status Code
| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 400 | `BAD REQUEST` |

