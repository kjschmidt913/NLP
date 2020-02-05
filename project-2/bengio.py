import tensorflow as tf

"""
General notes:
    - anything with embeddings or matrices should be done on GPU (i.e. using a tf method -- if we specify gpu-specific
        tf, then everything run using tf should be on GPU)
    - to run on GPU, we need to install GPU-specific version of TF
        - we can run on Wilkinson lab machines, or on AWS
    - 



Constants:
- num_dimensions = 60
- sliding_window_size = 5
- vocabulary_length = 
- num_epochs = 20


"""


# get the integer representation of our vocabulary (i.e. our vocab dict) from our Proj1 code
#       - this will be used later to index into the embedding space

# setup tensorflow to initialize the following using something like tf.get_variable():
#       - the embedding space as a (length of vocabulary) X (# dimensions) matrix of random values between [-1.0, 1.0]
#       - W layer as a () X () matrix (this is the indirect layer)
#       - H layer as a () X () matrix
#       - U layer as a () X () matrix
#       - b bias vector as a () long vector
#       - d bias vector as a () long vector

# establish placeholders (?) for the context (vector of length 5) and target (vector of length 1).

# using our sliding window (n = 5), pass the context and the target indices (gleaned from our integer representation)
#       as a numpy array to TF via tf.sess.run().

# pass the context and then target indices tp tf.embedding_lookup() to get the appropriate rows from our embedding space
#       matrix. the target vector returned from tf.embedding_lookup() is our true y values

# tf.concat() the 5 vectors we receive back for the context into one matrix, x_t. This is what we dot product with
#       the H layer and the W layer

# calculate the initial logits y from the Bengio equation y = b + Wx_t + Utanh(d + Hx_t)

# those logits we must then convert to pseudo probabilities, then normalize via softmax to produce our y_hat.
#       y_hat should be (vocabulary length) X (1) in size

