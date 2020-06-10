#!/bin/bash

target="data/03"

if [ ! -d data ]; then
    mkdir data
fi
if [ ! -d data/03 ]; then
    mkdir ${target}
fi

curl https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data > ${target}/housing.data
curl https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.names > ${target}/housing.names