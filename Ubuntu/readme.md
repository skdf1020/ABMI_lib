# 1. 공유폴더 마운트 하는 과정

## 삼바 설치
이미 설치 돼있는지 확인하려면
```
smbd --help 
```
설치
```
sudo apt-get install samba samba-common-bin
```

## 공유받을 폴더 생성
```
sudo mkdir /(원하는 경로)/shared
```
## 재부팅해도 마운트가 유지되도록 수정
```
sudo vi /etc/fstab 혹은 sudo gedit /etc/fstab
```
가장 아랫줄에 다음을 추가
```
//(ip)/(공유해주는 폴더 이름) /(원하는 경로)/shared cifs username=(공유폴더계정),password=(암호),uid=1000,gid=1000 0 0
```
만일 공유받는 우분투 사용자가 pi라면 uid와 gid를 다음에서 알 수 있다.
```
sudo id pi 혹은 sudo gedit /etc/passwd
```
## 마운트 명령어
```
sudo mount /(원하는 경로)/shared
```
