FROM jupyter/all-spark-notebook:016833b15ceb

USER root
RUN apt-get -y update && apt-get install -y zip unzip
COPY notebooks notebooks
RUN chown -R $NB_UID:$NB_UID /home/$NB_USER
USER $NB_UID
RUN curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o "awscliv2.zip"
RUN unzip awscliv2.zip
USER root
RUN ./aws/install
USER $NB_UID
WORKDIR /home/$NB_USER
WORKDIR notebooks
WORKDIR /tmp/notebooks

#todo: require password for security. Turning off in first release to avoid initial complexity for readers.
CMD jupyter notebook --ip=0.0.0.0 --no-browser --NotebookApp.token='' --NotebookApp.password=''
