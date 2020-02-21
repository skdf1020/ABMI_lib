# Docker

참조1 : [link](https://www.bsidesoft.com/?p=7820)
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
## 5. 이미지 만들기
>Dockerfile 이라는 이름으로 텍스트 작성. 내용은 다음과 같다.
>```
>FROM ubuntu:18.04
>RUN apt update
>RUN apt install -y python3-pip
>RUN pip3 install jupyter
>RUN pip3 install matplotlib
>RUN jupyter notebook --generate-config --allow-root
>RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py
>EXPOSE 8888
>ENTRYPOINT jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --no-browser
>```
>해당 파일이 저장된 경로로 이동한 후 다음을 실행.
>```
>docker build --tag abmi:ubuntu_18.04
>```
>이미지가 만들어지면 다음을 실행.
>```
>docker run -it --rm -p 8888:8888 -v /home/yoonlab6/docker:/home/root/test abmi:ubuntu_18.04
>```
>호스트 컴퓨터에서 브라우저를 열고 localhost:8888/에 접속하면 비밀번호를 입력하게 한다.
>'root'를 입력하면 jupyter notebook을 실행
>home/root/test에 들어가서 파일을 만들면 host의 home/yoonlab6/docker안에도 똑같은 파일이 생성된다.
