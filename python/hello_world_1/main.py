#!/usr/bin/env python3

import pickle

hw = b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00\x8c\rHello World!!\x94.'

print(pickle.loads(hw))
