import tensorflow as tf
import numpy as np


def get_angles(pos, i, d_model):
    angle_rates = 1 / np.power(10000, (2 * (i//2)) / np.float32(d_model))
    return pos * angle_rates


def positional_encoding(position, d_model):
    """
    The positional encoding vector is added to the embedding vector.
    Embeddings represent a token in a d-dimensional space where tokens
    with similar meaning will be closer to each other.
    But the embeddings do not encode the relative position of words in a sentence.
    
    So after adding the positional encoding, words will be closer to each other
    based on the similarity of their meaning and their position in the sentence,
    in the d-dimensional space.
    
    >>> pos_encoding = positional_encoding(50, 512)
    >>> print (pos_encoding.shape)

    >>> plt.pcolormesh(pos_encoding[0].eval(), cmap='RdBu')
    >>> plt.xlabel('Depth')
    >>> plt.xlim((0, 512))
    >>> plt.ylabel('Position')
    >>> plt.colorbar()
    >>> plt.show()
    """
    angle_rads = get_angles(
        np.arange(position)[:, np.newaxis],
        np.arange(d_model)[np.newaxis, :],
        d_model
    )

    # apply sin to even indices in the array; 2i
    sines = np.sin(angle_rads[:, 0::2])

    # apply cos to odd indices in the array; 2i+1
    cosines = np.cos(angle_rads[:, 1::2])

    pos_encoding = np.concatenate([sines, cosines], axis=-1)

    pos_encoding = pos_encoding[np.newaxis, ...]

    return tf.cast(pos_encoding, dtype=tf.float32)

