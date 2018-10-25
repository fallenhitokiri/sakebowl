FROM alpine:3.8
WORKDIR /app
ADD . /app
RUN apk --no-cache add -U python3
RUN pip3 install -r requirements.txt
CMD ["/app/start.sh"]
