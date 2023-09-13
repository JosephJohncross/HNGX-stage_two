
# REST API

The REST API to the example app is described below.

## Get a person by name

### Request

`GET /api/id`

    curl -i -H 'Accept: application/json'  https://hngx-stage-two-8l8p.onrender.com/api/1

### Response

    HTTP/1.1 200 OK
    Date: Mon, 11 Sept 2023 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {"name": "Mark Essien", "id": 1}

## Create a person

### Request

`POST /api`

    curl -i -H 'Accept: application/json' -d 'name=Mark Essien' https://hngx-stage-two-8l8p.onrender.com/api

### Response

    HTTP/1.1 200 OK
    Date: Mon, 11 Sept 2023 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 36

    "Person created succesfully"

## Update a person

### Request

`PATCH /api/id`

    curl -i -H 'Accept: application/json' -X PATCH -d 'name=Melody James' https://hngx-stage-two-8l8p.onrender.com/api/1

### Response

    HTTP/1.1 200 OK
    Date: Mon, 11 Sept 2023 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 36

    {"name": "Mark Essien","id": 1}

## Delete a person

### Request

`DELETE /api/id`

    curl -i -H 'Accept: application/json' -X DELETE https://hngx-stage-two-8l8p.onrender.com/api/1

### Response

    HTTP/1.1 204 No Content
    Date: Mon, 11 Sept 2023 12:36:30 GMT
    Status: 204 No Content
    Connection: close
    Content-Type: application/json
    Content-Length: 1
