FROM docker.io/golang:alpine3.14
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN go mod init cnjr
RUN go mod tidy
RUN go mod download
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o cnjr .
CMD ["/app/cnjr"]
