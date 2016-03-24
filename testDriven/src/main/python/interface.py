#!/usr/bin/env python3

import abc
#from abc import ABCMeta, abstractmethod, abstractproperty

class IStream(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def read(self, maxbytes):
        return maxbytes

    @abc.abstractmethod
    def write(self, data):
        return data

class SocketStream(IStream):

    def read(self, maxbytes):
        max_bytes = super(SocketStream, self).read(maxbytes)
        print("Read socket stream with max bytes: " + str(max_bytes))

    def write(self, data):
        my_data = super(SocketStream, self).write(data)
        print("Write socket stream with data: " + str(my_data))

socket=SocketStream()
socket.read(1)
socket.write("Hello World!")