# anon_painter



# memo

docker run -it -p 8888:8888 -v $PWD:/tmp -w /tmp tensorflow/tensorflow:2.0.0-py3-jupyter bash
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root

pip install pillow
pip install tensorflow_hub
