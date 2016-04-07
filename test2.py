# coding: utf-8

import skip32
import numpy
import random

if __name__ == '__main__':
    key = ''.join([str(x) for x in xrange(10)])[::-1]
    uint32_max = numpy.iinfo(numpy.uint32).max
    data = [random.randint(0, uint32_max) for _ in xrange(20)]

    for x in data:
        data_encrypt = skip32.encrypt(key, x)
        print "{data} encrypt to: {data_encrypt}, base36 to: {data_base36}".format(
            data=x,
            data_encrypt=data_encrypt,
            data_base36=numpy.base_repr(data_encrypt, 36)
        )

