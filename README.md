# EMOJIFY

# docker build #  
docker build -t emojify-server:v1.0 .

# run in interactive mode to see standard out #
docker run --rm -ti -p 12000:12000/udp --name myemojifyserver emojify-server:v1.0

# run in deattached mode and run docker logs #  
docker run --rm -d -p 12000:12000/udp --name myemojifyserver emojify-server:v1.0

# view cli help #
./emoji-cli.py -h

```
usage: emoji-client [options] emoji

send beautiful emojis

positional arguments:
  TYPE_OF_EMOJI         the emoji you want

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER_OF_EMOJIS   the number of emojis you need
  -s TYPE_OF_SEPARATOR  the type of separator you want
  -r                    if specified do not translate emojis server side
```

# cli usage example #  
./emoji-cli.py -n 10 thumbsup
