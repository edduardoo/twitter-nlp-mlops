### Orientation to run this
- build the image: docker build -t inference-module-api .
- run the docker container: docker run -p 9000:8080 inference-module-api
- access the handler: 
curl --request POST \
  --url http://localhost:9000/2015-03-31/functions/function/invocations \
  --header 'Content-Type: application/json' \
  --data '{"Input": 4}'