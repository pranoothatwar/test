import tensorflow as tf

def squashing(s):
	s_norm = tf.reduced_sum(tf.square(v),-2, keepdims=True)
	v = (s_norm/((1+s_norm)(tf.sqrt(s_norm)))) * s
	return v

class PrimaryCaps():
	def __init__(self, num_capsules, capsule_output_vec_dim):

		self.num_capsules = num_capsules  # 32
		self.capsule_output_vec_dim = capsule_output_vec_dim  # 8
		print num_capsules, capsule_output_vec_dim

	def __call__(self, prev_layer, filter_size, stride, padding): # input_dim = [batch, 20,20, 256]
 		self.prev_layer = prev_layer  # [batch, 20, 20, 256] or its conv1
		self.filter_size = filter_size  # [9,9]
		self.stride = stride   # 1
		self.padding = padding  # 'valid'

		capsules = []

		for i in range(self.capsule_output_vec_dim):	
			# [batch, 6, 6, 32] 
			with tf.variable_scope('PrmaryCapsuleUnit_' + str(i)):
				cap = tf.contrib.layers.conv2d(prev_layer, self.num_outputs, self.filter_size, self.stride, self.padding)
				cap = tf.reshape(cap, shape=(None, -1, 1, 1)) #batchsize input error possible [batch, 1152, 1, 1]
				capsules.append(cap)
		capsules = squashing(tf.concat(capsules, axis=2)) # axis = 2

		return capsules


class DigitCaps():
	def __init__(self, num_capsules, capsule_output_vect_dim):

		self.num_capsules = num_capsules  # 10
		self.capsule_output_vect_dim = capsule_output_vect_dim  # 16

	def __call__(self, prev_layer): 
 		self.prev_layer = prev_layer 

		capsules = []

		
		capsules = squashing(tf.concat(capsules, axis=2)) # axis = 2

		return capsules

def routing():
	self.b = tf.var



def MarginalLoss(y, y_hat):
	Lc = y * tf.square(tf.maximum(0., 0.9 - y_hat)) + 0.5 * (1 - y) * tf.square(tf.maximum(0., y_hat - 0.1))
	return tf.reduced_mean(tf.reduced_sum(Lc, axis =1))

a = PrimaryCaps(4,5)