# sse prototype
local **client** (dart with dart-eventsource) / **server** (python with flask) implementation to send bidirectional server-side-event from to server to client

- http server: python with flask
- client: dart

## RUN

### start http server
```sh
cd myflask
python3 server.py
```

### start client
```sh
cd mysse
dart run
```

### send http request to server (he will send this payload as sse event to the client)
```sh
#!/bin/bash
curl -X GET \
-H "Content-Type: application/json" \
-d '{"foo": "bar"}' \
http://127.0.0.1:5000/hello
```

## INSTALL

### for server side
install redis server
```sh
sudo apt-get install redis-server
```

install flask-sse
```sh
sudo apt-get install python3-flask
sudo pip3 install flask-sse
```

### for client side
install dart
```sh
https://dart.dev/get-dart
```

install dependencies
```sh
dart pub get
```

## SOURCES

```sh
https://pypi.org/project/Flask-SSE/
```

```sh
https://github.com/featurehub-io/featurehub/tree/main/sdks/dart/dart-eventsource
```
