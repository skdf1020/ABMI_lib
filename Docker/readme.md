# Docker Download

참조 : [link](https://www.bsidedoft.com/?p=7820)

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
>만약 특정 버전의 도커가 필요하다면
>버전리스트 확인
>```
>apt-cache madison docker-ce
>```
>특정버전 설치
>```
>sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
>```
