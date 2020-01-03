#!/bin/sh

sudo docker run -it -p 8888:8888 -v $PWD:/tmp -w /tmp tensorflow/tensorflow:2.0.0-py3-jupyter bash
