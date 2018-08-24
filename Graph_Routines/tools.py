import numpy as np


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


def mean_unit_vector(list_vectors):
    """ Returns the mean unit vector for a list of vectors.  """
    return unit_vector(np.mean(np.array(list_vectors), axis=0))


def cross_unit_vect(v1, v2):
    """ Cross product of unit vectors v1, v2"""
    return np.cross(unit_vector(v1), unit_vector(v2))


def sse_0_vect_cross_unit_vect(v1, v2):
    """ returns the SSE difference between the zero vector
        and the Cross product of unit vectors v1, v2"""
    c_u_v = cross_unit_vect(v1, v2)
    return np.sum((np.zeros(c_u_v.shape[0]) - c_u_v) ** 2)
