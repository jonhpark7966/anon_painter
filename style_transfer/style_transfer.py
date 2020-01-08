#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals


import tensorflow as tf

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12,12)
mpl.rcParams['axes.grid'] = False

import numpy as np
import PIL.Image
import time
import functools
import sys

import tensorflow_hub as hub

def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return PIL.Image.fromarray(tensor)

def load_img(path_to_img):
  max_dim = 512
  img = tf.io.read_file(path_to_img)
  img = tf.image.decode_image(img, channels=3)
  img = tf.image.convert_image_dtype(img, tf.float32)

  shape = tf.cast(tf.shape(img)[:-1], tf.float32)
  long_dim = max(shape)
  scale = max_dim / long_dim

  new_shape = tf.cast(shape * scale, tf.int32)

  img = tf.image.resize(img, new_shape)
  img = img[tf.newaxis, :]
  return img


############################################################################################

def main(content_path, style_path):
  #read images.
  content_image = load_img(content_path)
  style_image = load_img(style_path)

  #load model
  hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1')
  #style it!
  stylized_image = (hub_module(tf.constant(content_image), tf.constant(style_image))[0])
  upscale = 4
  tensor_to_image(tf.image.resize(stylized_image,tf.shape(stylized_image)[1:3]*upscale,'lanczos5', True, True) ).save('test.png')


if __name__ == '__main__':
  # arg1 is content_path, arg2 is style_path
  main(sys.argv[1], sys.argv[2])
  


