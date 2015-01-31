## Generate D3.js interactive friendship network graphs with Facebook data

[Check example](adidonato.github.io/fb-redirected.html)

## Usage

* Get your FB Access Token [here](https://developers.facebook.com/tools/access_token/)

* pull your FB friends data and create cliques in your network:
```
python fb-graph-generator.py
```

* fire up the webserver with this command:
```
python -m SimpleHTTPServer [portnumber]
```

## Contents

* graph generator .py script
* html visualization files

## Requirements

* FB API Access Token
* Python modules

requests, json, facebook, network, SimpleHTTPServer, SocketServer

## COPYRIGHT

These scripts are dedicated to the public domain. Use them as you please with no restrictions whatsoever.
Developed and inspired rom https://github.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition
