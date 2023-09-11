
# REST API

The REST API to the example app is described below.

## Get a person by name

### Request

`GET /api`

    curl -i -H 'Accept: application/json'  http://localhost:8000/api?name="Mark Essien"

### Response

    HTTP/1.1 200 OK
    Date: Mon, 11 Sept 2023 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {"name": "Mark Essien", "id": 3}

## Create a person

### Request

`POST /api`

    curl -i -H 'Accept: application/json' -d 'name=Mark Essien' http://localhost:8000/api

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

`PATCH /api`

    curl -i -H 'Accept: application/json' -X PATCH -d 'name=Melody James&id=3' http://localhost:8000/api

### Response

    HTTP/1.1 200 OK
    Date: Mon, 11 Sept 2023 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 36

    {"person": {"name": "Melody James"}}

## Delete a person

### Request

`DELETE /api`

    curl -i -H 'Accept: application/json' -X DELETE -d 'id=3' http://localhost:8000/api

### Response

    HTTP/1.1 204 No Content
    Date: Mon, 11 Sept 2023 12:36:30 GMT
    Status: 204 No Content
    Connection: close
    Content-Type: application/json
    Content-Length: 1
