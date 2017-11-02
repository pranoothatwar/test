import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=False)
print (mnist)
x,y= mnist.train.next_batch(12)
print y