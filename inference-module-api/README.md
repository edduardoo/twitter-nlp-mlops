### Orientation to run this
- build the image: docker build -t twitter-nlp-inference-api .
- run the docker container: docker run -p 8080:8080 twitter-nlp-inference-api
- access the handler: 
curl --request POST \
  --url http://localhost:8080/2015-03-31/functions/function/invocations \
  --header 'Content-Type: application/json' \
  --data '{"texts": [""]}'