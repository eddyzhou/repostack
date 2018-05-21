image: golang:latest

variables:
  REPO_NAME: gitlab.com/{{ group }}/{{ repo }}

before_script:
  - mkdir -p $GOPATH/src/$(dirname $REPO_NAME)
  - ln -svf $CI_PROJECT_DIR $GOPATH/src/$REPO_NAME
  - cd $GOPATH/src/$REPO_NAME

stages:
    - test
    - build

format:
    stage: test
    script:
      - go fmt $(go list ./... | grep -v /vendor/)
      - go vet $(go list ./... | grep -v /vendor/)
      - go test -race $(go list ./... | grep -v /vendor/)

compile:
    stage: build
    script:
      - go build -race -ldflags "-extldflags '-static'" -o $CI_PROJECT_DIR/{{ repo }}
    artifacts:
      paths:
        - {{ repo }}

