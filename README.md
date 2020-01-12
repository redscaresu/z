# EMOJIFY

#docker build  
docker build -t emojify-server:v1.0 .

#run in interactive mode to see standard out  
docker run --rm -ti -p 12000:12000/udp --name myemojifyserver emojify-server:v1.0

#run in deattached mode and run docker logs   
docker run --rm -d -p 12000:12000/udp --name myemojifyserver emojify-server:v1.0

#cli usage example  
./emoji-cli.py -n 10 thumbsup
