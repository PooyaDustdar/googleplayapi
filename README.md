# googleplayapi
get android app detail from google play and apk file.
this script run on 
            `http://googleplayapi.ir`
## Run Server:
for run this server fallow this steps:
### Step 1:
install dependencies. for install dependencies run this code on your virtual environment:
`pip install -r requirements.txt`

### Step 2:
config `PROTOCOL`, `HOST` , `PORT` and `UPLOAD_DIR` in `config.py`

### Step 3:
run `application.py` via `python3`. for run applicatoin run this code:
`python3 application.py`

## Use in Client:
send request with package_name to:
`PROTOCOL://HOST:PORT/package_name`

###Example Response:
```
{
"docId": "docId",
"title": "title",
"author": "author",
"description": "description",
"recentChanges": "recentChanges",
"offer": [
            {
            "micros": 0,
            "currencyCode": "USD",
            "formattedAmount": "",
            "checkoutFlowRequired": false,
            "offerType": 1,
            "saleEnds": ""
            }
           ],
"images": [
            {
            "imageType": 2,
            "width": 512,
            "height": 512,
            "url": "url",
            "supportsFifeUrlOptions": true
            },
           .
           .
           .
           ],
"versionCode": versionCode,
"versionString": "versionString",
"installationSize": installationSize,
"numDownloads": "numDownloads downloads",
"uploadDate": "uploadDate",
"permission": [
    "android.permission.ACCESS_NETWORK_STATE",
   .   
   .
   .
],
"files": [
    {
        "fileType": 0,
        "version": 468,
        "size": 76903499,
        "url": "url"
    },
    .
    .
    .
],
"unstable": true,
"containsAds": "containsAds",
"aggregateRating": {
"type": 2,
"starRating": starRating,
"ratingsCount": 26312,
"oneStarRatings": 1018,
"twoStarRatings": 231,
"threeStarRatings": 449,
"fourStarRatings": 3620,
"fiveStarRatings": 20994,
"commentCount": 7857
},
"dependencies": [
    {
        "packageName": "com.google.android.gms",
        "version": 11910000
    },
    .
    .
    .
],
"category": {
"appType": "GAME",
"appCategory": ""
},
"detailsUrl": "detailsUrl"
}
```
