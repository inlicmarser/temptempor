import tensorflow as tf

fullPath = "path_to_file.tfrecord"

with tf.io.TFRecordWriter(str(fullPath), options=tf.io.TFRecordOptions(compression_type='GZIP', compression_level=4)) as writer:
    # Your code for writing records to the TFRecord file goes here
