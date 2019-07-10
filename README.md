# googleplayapi
get android app detail from google play and apk file

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
