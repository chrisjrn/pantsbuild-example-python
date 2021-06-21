FROM amd64/python:3.9-buster 

WORKDIR /usr/src/app
COPY . .

CMD ["./pants", "--no-pantsd", "--no-watch-filesystem"]