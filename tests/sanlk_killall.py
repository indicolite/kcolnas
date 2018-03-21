#!/usr/bin/env python
# coding=utf-8
import struct
import socket
import sys
import binascii

values = (0x04282010, 0x00000001, 36, 0, 32, 0, 0, 0)
packer = struct.Struct('I I I I I I I I')
packed_data = packer.pack(*values)

try:
    sanlock_sock_path = '/run/sanlock/sanlock.sock'
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(sanlock_sock_path)
except Exception:
    print('Failed to connect sanlock socket.')
    sys.exit(1)

try:
    sock.sendall(packed_data)
    print('Send %s to sanlock socket.' % binascii.hexlify(packed_data))
except Exception:
    print('Failed to send data to sanlock socket.')
finally:
    sock.close()
