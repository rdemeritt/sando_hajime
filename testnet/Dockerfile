# build image
FROM ubuntu:20.04

RUN apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC \
    apt-get -y install git libgtest-dev build-essential cmake pkg-config libssl-dev  \
                libzmq3-dev libunbound-dev libsodium-dev libunwind8-dev  \
                liblzma-dev libreadline6-dev libldns-dev libexpat1-dev  \
                libpgm-dev qttools5-dev-tools libhidapi-dev libusb-1.0-0-dev  \
                libprotobuf-dev protobuf-compiler libudev-dev libboost-chrono-dev  \
                libboost-date-time-dev libboost-filesystem-dev libboost-locale-dev  \
                libboost-program-options-dev libboost-regex-dev libboost-serialization-dev  \
                libboost-system-dev libboost-thread-dev ccache doxygen graphviz libcurl4-openssl-dev && \
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

RUN cd /usr/src/gtest && \
    cmake . && \
    make

WORKDIR /src
RUN git clone --recursive https://github.com/monero-project/monero
RUN cd monero &&  \
    git checkout release-v0.17 && \
    git submodule update --init --force && \
    make -j 6 release
