#!/bin/sh

go fmt ./...
go vet ./...
golint .
go test ./...
