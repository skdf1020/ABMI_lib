FROM ubuntu:18.04

RUN apt update
RUN apt -y upgrade
RUN apt install -y python3-pip
RUN pip3 install jupyter matplotlib pandas tensorflow==1.5
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py

EXPOSE 8888
EXPOSE 6006
