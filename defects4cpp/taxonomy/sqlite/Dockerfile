# Copyright 2021 Suresoft Technologies Inc.
# Licensed under the MIT
FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get install -y git liblua5.3-dev python3 python3-pip \
    wget lsb-release software-properties-common \
    tcl tcl-dev autoconf

RUN echo "end to basic command"

# Install latest cmake
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null
RUN apt-add-repository "deb https://apt.kitware.com/ubuntu/ $(lsb_release -cs) main"
RUN apt-get install -y cmake

RUN echo "end to cmake"

# Install gcovr
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 100
RUN pip3 install gcovr
RUN echo "end to gcovr"

# Install cwrap


RUN git config --global user.email "tgheo@suresofttech.com"
RUN git config --global user.name "taekwang"
RUN echo "end to git"

RUN useradd --create-home --home-dir /home/workspace --shell /bin/bash defects4cpp
RUN echo "end to path"
USER defects4cpp
RUN echo "end to USer"
WORKDIR /home/workspace
RUN echo "FISNISH"
