# Docker Download

참조1 : [link](https://www.bsidedoft.com/?p=7820)
참조2 : [link](http://pyrasis.com/book/DockerForTheReallyImpatient/)

## 1. 저장소 설정

>apt 패키지 update
>```
>sudo apt-get update
>```
> 필요한 패키지들을 설치
>```
>sudo apt-get install \
>apt-transport-https \
>ca-certificates \
>curl \
>gnupg-agent \
>software-properties-common
> ```
>docker 공식 gpg key 추가
>```
>curl -fsSL https://download.docker.com/linux/ubunutu/gpg | sudo apt-key add -
>```
>인식키 확인
>```
>sudo apt-key fingerprint 0EBFCD88
>```
>저장소 설정
>```
>sudo add-apt-repository \
>"deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
>```
## 2. docker ce 설치

>변경된 apt-repository로 업데이트
>```
>sudo apt-get update
>```
>docker CE 최신버전 설치
>```
>sudo apt-get install docker-ce docker-ce-cli containerd.io
>```
>만약 특정 버전의 도커가 필요하다면 버전리스트 확인
>```
>apt-cache madison docker-ce
>```
>특정버전 설치
>```
>sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
>```

## 3. docker image

>image 받아오기 (예시 hello-world)
>```
>docker pull hello-world
>```
>local에서 'hello-world' image를 찾아 컨테이너로 실행, local에 없다면 자동으로 pull을 실행
>```
>docker run hello-world
>```
>local에 저장된 image들을 확인.
>```
>docker images
>```
>만들어진 컨테이너들을 확인.
>```
>docker ps -a
>```
>컨테이너 삭제
>```
>docker rm [container ID 또는 name]
>docker stop [container ID 또는 name] #먼저 먼춰야하는 경우도 있음.
>```
>image 삭제
>```
>docker rmi [image name] #해당 image로 만들어진 컨테이너들을 모두 삭제한 후에 가능.
>```
## 4. nginx example
>nginx image를 mynginx라는 이름의 컨테이너로 8080:80포트에 연결하여 background에서 실행.
>```
>docker run -d -p 8080:80 --name mynginx nginx #실행 후 웹브라우저에 http://localhost:8080에 접속하여 확인할 수 있다.
>```
>mynginx에서 hello 출력하기.
>```
>docker exec mynginx echo "hello"
>```
>mynginx에서 bash 실행.
>```
>docker exec -i -t mynginx /bin/bash
>```
