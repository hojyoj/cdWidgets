# -*- coding: utf-8 -*-

 ###############################################
 ##                                             ##
 ##   Slide Selector with validation             ##
 ##                                              ##
 ##                                              ##
 ##                                              ##
 ##   by Críptidos Digitales                     ##
 ##   GPL (c)2008-2012                           ##
  ##                                             ##
    ###############################################

"""
"""

__version__ = '0.1'

import sys
from PyQt4 import QtCore, QtGui


# Resource object code
#
# Created: mar 7. may 18:08:42 2013
#      by: The Resource Compiler for PyQt (Qt v4.7.2)
#
# WARNING! All changes made in this file will be lost!


qt_resource_data = b"\
\x00\x00\x02\x68\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x22\x00\x00\x00\x40\x08\x06\x00\x00\x00\x7f\x7b\xa5\x93\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\x00\x00\x00\x00\x00\xf9\x43\
\xbb\x7f\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0b\x13\x00\x00\
\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07\x74\x49\x4d\x45\x07\
\xdd\x05\x07\x14\x15\x33\xa4\x09\x9e\x36\x00\x00\x00\x1d\x69\x54\
\x58\x74\x43\x6f\x6d\x6d\x65\x6e\x74\x00\x00\x00\x00\x00\x43\x72\
\x65\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x47\x49\x4d\x50\x64\
\x2e\x65\x07\x00\x00\x01\xcc\x49\x44\x41\x54\x68\xde\xdd\x99\x4d\
\x6e\x83\x30\x10\x85\xdf\x90\x0b\x54\x8a\x7a\x90\x6c\x7a\x82\xdc\
\xa7\x87\x81\x43\x24\x67\x08\xca\x01\xba\xc9\x11\xba\x2f\x42\xe2\
\x02\xe8\x75\x43\x23\x42\xc1\x78\xfc\x83\x2d\x46\xf2\xce\x32\x1f\
\x33\xcf\xc3\xc3\x06\x12\x05\xc9\x92\xa3\x48\xfa\xf0\xcd\x41\x48\
\x7e\x72\x25\x92\x65\x60\x1a\x12\x11\x42\xf5\x96\x92\x03\x44\x14\
\x10\xd7\x7a\x4b\x0e\x10\x41\x41\x7c\x95\x2f\x39\x40\x04\x01\x09\
\xd5\x03\x24\x07\x08\x00\x28\x36\xdd\xa2\x22\x7f\xa3\x0a\x26\x4c\
\x4d\x00\x98\x1b\xa5\x57\x67\x55\x64\xa2\x15\x91\x07\x80\xb3\x61\
\x2d\x37\x8d\x68\xca\x21\x22\x3d\x80\x0e\xc0\x31\x28\x88\x12\xc2\
\x76\x4d\x9d\x58\x23\x40\x34\x00\xaa\x68\xc2\x5c\x10\xe5\xdc\xb8\
\xa8\x6c\x40\xec\x72\x58\x35\xb4\x2d\x21\x16\x41\xb6\x86\x98\x05\
\x49\x01\xf1\x0f\x24\x15\xc4\xcb\xf6\x25\x79\x49\x05\xf1\x92\x11\
\x92\x3f\x00\xde\x53\x40\x3c\x33\x42\xb2\x4c\x09\xf1\xcc\x88\x8d\
\x36\x44\xa4\x06\x70\x32\x7d\x3b\x5c\x21\xb4\x7e\xe4\x04\xe0\xcd\
\xd4\xb6\x7d\x7c\x52\x61\x21\xd2\x76\xc8\xc6\x11\xc0\xc1\x30\xef\
\xee\x65\x15\x2d\x44\xda\x8b\x48\x17\xab\x24\x63\x10\x86\x10\xa9\
\x2f\x48\x81\x4c\x22\x14\x48\x0f\xa0\xf5\x05\xb9\x5a\x98\x98\xb5\
\x39\xdd\xe0\x4f\xfd\xfe\x6b\x72\xd0\x89\xa6\x34\xf5\x5a\xfa\x6d\
\x3b\xaf\x09\xa4\xb2\x78\xdb\xb5\x86\xe6\x05\x23\x5a\x0b\x10\xf5\
\xa3\x37\xc4\x35\xe4\x03\xb4\x99\xc9\xc6\x18\xe5\x69\x15\xb3\x32\
\xcf\xa9\x60\x0a\xc3\xe2\x9a\xff\x62\x5b\xe0\x46\x44\xae\x4e\x27\
\x46\x11\x32\xd3\x02\x78\x90\x3c\xab\x8f\xae\x02\xc3\xf4\x00\x3a\
\x92\x47\x75\x8b\x77\x2c\x53\xb3\x30\xe5\x30\x67\xb2\x0a\xc5\x9b\
\x6a\x61\x4c\xd6\xf1\x4b\xad\x11\x9f\x32\x2d\x94\xaa\x01\xf0\x4d\
\xf2\xc3\xcb\x18\x89\xb2\x77\x93\x9c\xee\xaa\xfb\x14\xc2\x29\x23\
\xae\x99\x71\xea\xac\x29\x60\xf6\x71\x04\x1e\x12\x66\x5f\xd7\x24\
\x21\x60\xf6\x79\x95\xe6\x03\x93\xcd\x75\x6b\xb4\x7f\xdf\xa1\x03\
\xd7\xc8\x29\x48\x5e\x92\x5e\xc9\xcf\x00\x95\x59\x80\x4c\xa0\x6e\
\x63\x90\x5f\x86\xea\x7c\x73\x9a\x04\x06\xc3\x00\x00\x00\x00\x49\
\x45\x4e\x44\xae\x42\x60\x82\
\x00\x00\x02\x77\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x22\x00\x00\x00\x40\x08\x06\x00\x00\x00\x7f\x7b\xa5\x93\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\x00\x00\x00\x00\x00\xf9\x43\
\xbb\x7f\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0b\x13\x00\x00\
\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07\x74\x49\x4d\x45\x07\
\xdd\x05\x07\x14\x15\x1e\xe1\xd6\xc2\x43\x00\x00\x00\x1d\x69\x54\
\x58\x74\x43\x6f\x6d\x6d\x65\x6e\x74\x00\x00\x00\x00\x00\x43\x72\
\x65\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x47\x49\x4d\x50\x64\
\x2e\x65\x07\x00\x00\x01\xdb\x49\x44\x41\x54\x68\xde\xcd\x9a\xc1\
\x6d\xc3\x30\x0c\x45\x3f\xe9\x05\x0c\x04\xed\x1e\xb9\x74\x82\xee\
\xd0\x31\x3a\x4c\x32\x44\x32\x43\x8d\x0e\xd0\x4b\x06\x31\x0c\x74\
\x81\x82\xbd\x28\x85\x1b\xc8\xb6\x24\x52\x32\x09\xe4\x94\x38\x7e\
\x11\xbf\xc9\x2f\x2a\x90\xff\x71\xc2\x5e\x21\xcb\x71\xf2\x02\x72\
\x8f\x77\x2f\x20\x4d\x56\x88\x44\x44\xb2\x2e\x20\xa2\x1a\x20\x5c\
\xb2\x82\x2e\x40\x6a\xc1\xb0\x46\x5b\x2e\x40\xac\x61\xd8\xe2\xa9\
\x73\x01\x62\x05\xc3\x56\x4b\xab\x85\xe1\x48\x9d\x38\x13\x11\x4a\
\xca\x85\x0a\x66\x5e\x3a\x01\x9c\x00\xc8\xe3\x2b\x37\xd4\x95\x75\
\x63\x15\x06\x11\x39\x02\x38\xd4\xa8\xc0\x39\x20\x13\x80\x5e\x44\
\xba\x1a\xed\x20\x07\x64\x9e\x4e\xf3\xde\xf4\x28\xd6\x33\x80\x31\
\xe1\xcb\xed\x05\x1c\x11\xda\x25\x26\x58\xad\x88\x8b\x6d\x40\xeb\
\x34\xb1\xf6\x06\x56\x69\x62\x8b\x5f\x6b\x01\xc3\x56\x4b\xaf\x85\
\x61\x4b\x1d\x68\x60\x38\xe3\xc2\x1a\x30\x17\x8d\x79\xb6\x04\x1f\
\x89\xe8\xb9\xd4\x3c\x5b\x02\x3f\xdd\xb7\x29\x54\xdc\x2d\xb7\x6f\
\x34\x01\xb8\x89\xc8\x6b\x4a\x7d\xd1\x98\x67\x6c\xb4\x83\x1e\xc0\
\xb1\x95\x43\xfb\x5c\x79\xaf\x03\x70\x20\xa2\x21\xac\xce\xaa\x68\
\x49\x6b\xf1\x52\x52\x24\x22\x7d\x00\x5b\x16\x6d\x03\x90\x24\x81\
\x9b\x99\xe7\xbd\x5d\xfc\x04\xe0\x67\x77\x10\x22\xba\x01\xf8\xde\
\xf8\xd8\x35\xc1\x6c\x5d\x55\x1a\xb1\xd2\x87\xaa\x8e\x24\x16\xb4\
\xa1\x6a\x6a\x12\xcb\x77\x1f\xb6\x1f\x5b\x71\xf6\xd0\xf4\xfe\xec\
\x23\xef\x09\x11\x84\x9c\x67\x03\x6a\x9b\x69\xf6\x00\x91\x04\xd2\
\x6a\x5b\xc1\x1e\x20\x16\x41\x88\xe8\x4a\x44\x63\x2b\x88\xa8\x58\
\x83\x7f\x48\x1a\x3f\x58\x6e\xc6\x63\x20\x53\x70\x57\x5d\xcb\x89\
\x40\x2c\x35\x87\x15\x88\xb1\xd5\x58\x02\x00\xbe\xd6\xac\x61\x0d\
\x88\xb5\xa7\x66\x8c\xa5\x42\x44\xde\x6a\x40\x44\x41\x44\xe4\x65\
\x6e\x8a\x03\x40\x6e\x53\xcc\x1e\x49\x92\xf5\x4c\xbd\xf4\x18\x85\
\x3d\x40\x98\x82\x68\x0f\x94\xd8\x03\x84\x09\x88\xd5\xd1\x1a\x7b\
\x80\x50\x81\x58\x1f\x32\xb2\x07\x88\x22\x10\x0f\xc7\xad\x43\x2d\
\x88\x7b\x09\xdf\x8a\x4b\x93\x5d\xb8\xd7\x3f\x29\x7c\xec\x35\x96\
\xf8\x05\xfb\x9e\x4d\x45\xe0\x2c\x6a\x70\x00\x00\x00\x00\x49\x45\
\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x0b\
\x02\x99\x2c\x07\
\x00\x4c\
\x00\x65\x00\x66\x00\x74\x00\x5f\x00\x30\x00\x31\x00\x2e\x00\x70\x00\x6e\x00\x67\
\x00\x0c\
\x09\x2f\xe8\x07\
\x00\x52\
\x00\x69\x00\x67\x00\x68\x00\x74\x00\x5f\x00\x30\x00\x31\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x01\x00\x00\x02\x6c\
"


'''

qt_resource_data = "\
\x00\x00\x02\x68\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x22\x00\x00\x00\x40\x08\x06\x00\x00\x00\x7f\x7b\xa5\x93\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\x00\x00\x00\x00\x00\xf9\x43\
\xbb\x7f\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0b\x13\x00\x00\
\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07\x74\x49\x4d\x45\x07\
\xdd\x05\x07\x14\x15\x33\xa4\x09\x9e\x36\x00\x00\x00\x1d\x69\x54\
\x58\x74\x43\x6f\x6d\x6d\x65\x6e\x74\x00\x00\x00\x00\x00\x43\x72\
\x65\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x47\x49\x4d\x50\x64\
\x2e\x65\x07\x00\x00\x01\xcc\x49\x44\x41\x54\x68\xde\xdd\x99\x4d\
\x6e\x83\x30\x10\x85\xdf\x90\x0b\x54\x8a\x7a\x90\x6c\x7a\x82\xdc\
\xa7\x87\x81\x43\x24\x67\x08\xca\x01\xba\xc9\x11\xba\x2f\x42\xe2\
\x02\xe8\x75\x43\x23\x42\xc1\x78\xfc\x83\x2d\x46\xf2\xce\x32\x1f\
\x33\xcf\xc3\xc3\x06\x12\x05\xc9\x92\xa3\x48\xfa\xf0\xcd\x41\x48\
\x7e\x72\x25\x92\x65\x60\x1a\x12\x11\x42\xf5\x96\x92\x03\x44\x14\
\x10\xd7\x7a\x4b\x0e\x10\x41\x41\x7c\x95\x2f\x39\x40\x04\x01\x09\
\xd5\x03\x24\x07\x08\x00\x28\x36\xdd\xa2\x22\x7f\xa3\x0a\x26\x4c\
\x4d\x00\x98\x1b\xa5\x57\x67\x55\x64\xa2\x15\x91\x07\x80\xb3\x61\
\x2d\x37\x8d\x68\xca\x21\x22\x3d\x80\x0e\xc0\x31\x28\x88\x12\xc2\
\x76\x4d\x9d\x58\x23\x40\x34\x00\xaa\x68\xc2\x5c\x10\xe5\xdc\xb8\
\xa8\x6c\x40\xec\x72\x58\x35\xb4\x2d\x21\x16\x41\xb6\x86\x98\x05\
\x49\x01\xf1\x0f\x24\x15\xc4\xcb\xf6\x25\x79\x49\x05\xf1\x92\x11\
\x92\x3f\x00\xde\x53\x40\x3c\x33\x42\xb2\x4c\x09\xf1\xcc\x88\x8d\
\x36\x44\xa4\x06\x70\x32\x7d\x3b\x5c\x21\xb4\x7e\xe4\x04\xe0\xcd\
\xd4\xb6\x7d\x7c\x52\x61\x21\xd2\x76\xc8\xc6\x11\xc0\xc1\x30\xef\
\xee\x65\x15\x2d\x44\xda\x8b\x48\x17\xab\x24\x63\x10\x86\x10\xa9\
\x2f\x48\x81\x4c\x22\x14\x48\x0f\xa0\xf5\x05\xb9\x5a\x98\x98\xb5\
\x39\xdd\xe0\x4f\xfd\xfe\x6b\x72\xd0\x89\xa6\x34\xf5\x5a\xfa\x6d\
\x3b\xaf\x09\xa4\xb2\x78\xdb\xb5\x86\xe6\x05\x23\x5a\x0b\x10\xf5\
\xa3\x37\xc4\x35\xe4\x03\xb4\x99\xc9\xc6\x18\xe5\x69\x15\xb3\x32\
\xcf\xa9\x60\x0a\xc3\xe2\x9a\xff\x62\x5b\xe0\x46\x44\xae\x4e\x27\
\x46\x11\x32\xd3\x02\x78\x90\x3c\xab\x8f\xae\x02\xc3\xf4\x00\x3a\
\x92\x47\x75\x8b\x77\x2c\x53\xb3\x30\xe5\x30\x67\xb2\x0a\xc5\x9b\
\x6a\x61\x4c\xd6\xf1\x4b\xad\x11\x9f\x32\x2d\x94\xaa\x01\xf0\x4d\
\xf2\xc3\xcb\x18\x89\xb2\x77\x93\x9c\xee\xaa\xfb\x14\xc2\x29\x23\
\xae\x99\x71\xea\xac\x29\x60\xf6\x71\x04\x1e\x12\x66\x5f\xd7\x24\
\x21\x60\xf6\x79\x95\xe6\x03\x93\xcd\x75\x6b\xb4\x7f\xdf\xa1\x03\
\xd7\xc8\x29\x48\x5e\x92\x5e\xc9\xcf\x00\x95\x59\x80\x4c\xa0\x6e\
\x63\x90\x5f\x86\xea\x7c\x73\x9a\x04\x06\xc3\x00\x00\x00\x00\x49\
\x45\x4e\x44\xae\x42\x60\x82\
\x00\x00\x02\x77\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x22\x00\x00\x00\x40\x08\x06\x00\x00\x00\x7f\x7b\xa5\x93\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\x00\x00\x00\x00\x00\xf9\x43\
\xbb\x7f\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0b\x13\x00\x00\
\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07\x74\x49\x4d\x45\x07\
\xdd\x05\x07\x14\x15\x1e\xe1\xd6\xc2\x43\x00\x00\x00\x1d\x69\x54\
\x58\x74\x43\x6f\x6d\x6d\x65\x6e\x74\x00\x00\x00\x00\x00\x43\x72\
\x65\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x47\x49\x4d\x50\x64\
\x2e\x65\x07\x00\x00\x01\xdb\x49\x44\x41\x54\x68\xde\xcd\x9a\xc1\
\x6d\xc3\x30\x0c\x45\x3f\xe9\x05\x0c\x04\xed\x1e\xb9\x74\x82\xee\
\xd0\x31\x3a\x4c\x32\x44\x32\x43\x8d\x0e\xd0\x4b\x06\x31\x0c\x74\
\x81\x82\xbd\x28\x85\x1b\xc8\xb6\x24\x52\x32\x09\xe4\x94\x38\x7e\
\x11\xbf\xc9\x2f\x2a\x90\xff\x71\xc2\x5e\x21\xcb\x71\xf2\x02\x72\
\x8f\x77\x2f\x20\x4d\x56\x88\x44\x44\xb2\x2e\x20\xa2\x1a\x20\x5c\
\xb2\x82\x2e\x40\x6a\xc1\xb0\x46\x5b\x2e\x40\xac\x61\xd8\xe2\xa9\
\x73\x01\x62\x05\xc3\x56\x4b\xab\x85\xe1\x48\x9d\x38\x13\x11\x4a\
\xca\x85\x0a\x66\x5e\x3a\x01\x9c\x00\xc8\xe3\x2b\x37\xd4\x95\x75\
\x63\x15\x06\x11\x39\x02\x38\xd4\xa8\xc0\x39\x20\x13\x80\x5e\x44\
\xba\x1a\xed\x20\x07\x64\x9e\x4e\xf3\xde\xf4\x28\xd6\x33\x80\x31\
\xe1\xcb\xed\x05\x1c\x11\xda\x25\x26\x58\xad\x88\x8b\x6d\x40\xeb\
\x34\xb1\xf6\x06\x56\x69\x62\x8b\x5f\x6b\x01\xc3\x56\x4b\xaf\x85\
\x61\x4b\x1d\x68\x60\x38\xe3\xc2\x1a\x30\x17\x8d\x79\xb6\x04\x1f\
\x89\xe8\xb9\xd4\x3c\x5b\x02\x3f\xdd\xb7\x29\x54\xdc\x2d\xb7\x6f\
\x34\x01\xb8\x89\xc8\x6b\x4a\x7d\xd1\x98\x67\x6c\xb4\x83\x1e\xc0\
\xb1\x95\x43\xfb\x5c\x79\xaf\x03\x70\x20\xa2\x21\xac\xce\xaa\x68\
\x49\x6b\xf1\x52\x52\x24\x22\x7d\x00\x5b\x16\x6d\x03\x90\x24\x81\
\x9b\x99\xe7\xbd\x5d\xfc\x04\xe0\x67\x77\x10\x22\xba\x01\xf8\xde\
\xf8\xd8\x35\xc1\x6c\x5d\x55\x1a\xb1\xd2\x87\xaa\x8e\x24\x16\xb4\
\xa1\x6a\x6a\x12\xcb\x77\x1f\xb6\x1f\x5b\x71\xf6\xd0\xf4\xfe\xec\
\x23\xef\x09\x11\x84\x9c\x67\x03\x6a\x9b\x69\xf6\x00\x91\x04\xd2\
\x6a\x5b\xc1\x1e\x20\x16\x41\x88\xe8\x4a\x44\x63\x2b\x88\xa8\x58\
\x83\x7f\x48\x1a\x3f\x58\x6e\xc6\x63\x20\x53\x70\x57\x5d\xcb\x89\
\x40\x2c\x35\x87\x15\x88\xb1\xd5\x58\x02\x00\xbe\xd6\xac\x61\x0d\
\x88\xb5\xa7\x66\x8c\xa5\x42\x44\xde\x6a\x40\x44\x41\x44\xe4\x65\
\x6e\x8a\x03\x40\x6e\x53\xcc\x1e\x49\x92\xf5\x4c\xbd\xf4\x18\x85\
\x3d\x40\x98\x82\x68\x0f\x94\xd8\x03\x84\x09\x88\xd5\xd1\x1a\x7b\
\x80\x50\x81\x58\x1f\x32\xb2\x07\x88\x22\x10\x0f\xc7\xad\x43\x2d\
\x88\x7b\x09\xdf\x8a\x4b\x93\x5d\xb8\xd7\x3f\x29\x7c\xec\x35\x96\
\xf8\x05\xfb\x9e\x4d\x45\xe0\x2c\x6a\x70\x00\x00\x00\x00\x49\x45\
\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = "\
\x00\x0b\
\x02\x99\x2c\x07\
\x00\x4c\
\x00\x65\x00\x66\x00\x74\x00\x5f\x00\x30\x00\x31\x00\x2e\x00\x70\x00\x6e\x00\x67\
\x00\x0c\
\x09\x2f\xe8\x07\
\x00\x52\
\x00\x69\x00\x67\x00\x68\x00\x74\x00\x5f\x00\x30\x00\x31\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct = "\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x01\x00\x00\x02\x6c\
"

'''


def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)



class CDSlideSelector(QtGui.QFrame):

    def currentData(self):
        return self._data[self._currentIndex]
    def setCurrentData(self, value, initialToo=False):
        try:
            self.setCurrentIndex(self._data.index(value), initialToo)
        except:
            print (self._data)
            raise

    _initialIndex = -1
    _currentIndex = -1
    def currentIndex(self):
        return self._currentIndex
    def setCurrentIndex(self, value, initialToo=False):
        
        while self._currentIndex != value:
            self.moveLeft()

        if initialToo:
            self._initialIndex = self._currentIndex

    def text(self, index=None):
        if index is None:
            return self._names[self._currentIndex]
        else:
            return self._names[index]

    def count(self):
        return len(self._names)

    _data = []
    _names = []
    def data(self, index=None):
        if index is None:
            return self._data
        else:
            return self._data[index]
    def setData(self, names, data = []):
        # self.leftLI.clear()
        # self.rightLI.clear()
        # self.leftLI.setMinimumWidth(self.frame.width())
        # self.leftLI.setMaximumWidth(self.frame.width())
        # self.rightLI.setMinimumWidth(0)
        # self.rightLI.setMaximumWidth(0)
        # self._names = names
        # self._data = data
        # self._currentIndex = 0
        # self._initialIndex = 0
        
        self.clear()
        self._names = names
        self._data = data
        
        self.leftLI.setText(self._names[self._currentIndex])
        self.rightLI.setText(self._names[self._currentIndex + 1])

        self.active = 'left'
        
        if self._currentIndex == -1:
            self.setCurrentIndex(0)
        
        self.emit(QtCore.SIGNAL('changed()'))


    def roll(self, step = 1):
        self._currentIndex += step
        if self._currentIndex == len(self._names):
            self._currentIndex = 0
        elif self._currentIndex == -1:
            self._currentIndex = len(self._names) - 1


    def __init__(self, *args, **kwds):

        QtGui.QFrame.__init__(self, *args)

        qInitResources()

        self.setObjectName('Form')
        # self.setStyleSheet('background-color:rgba(0,0,0,0);')
        # self.setStyleSheet('background-color:#F0FF00;')
        self.setStyleSheet('background-color:#FFFFFF;')

        self.LY = QtGui.QHBoxLayout(self)
        self.LY.setSpacing(0)
        self.LY.setMargin(0)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.leftBU = QtGui.QPushButton(self)
        self.leftBU.setFlat(True)
        # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.leftBU.sizePolicy().hasHeightForWidth())
        # self.leftBU.setSizePolicy(sizePolicy)
        self.leftBU.setText('')
        # self.leftBU.setStyleSheet('background-color:#F0FF00;')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':/Left_01.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftBU.setIcon(icon)
        self.LY.addWidget(self.leftBU)

        self.frame = QtGui.QFrame(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        # self.frame.setFrameShape(QtGui.QFrame.Panel)
        # self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        # self.frame.setStyleSheet('background-color:#FF00FF;')

        self.frameLY = QtGui.QHBoxLayout(self.frame)
        self.frameLY.setSpacing(0)
        self.frameLY.setMargin(0)

        self.leftLI = QtGui.QLabel(self.frame)
        # self.leftLI = QtGui.QLineEdit(self.frame)
        # self.leftLI.setFrameShape(QtGui.QFrame.NoFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.leftLI.sizePolicy().hasHeightForWidth())
        self.leftLI.setSizePolicy(sizePolicy)
        # self.leftLI.setFrame(False)
        self.leftLI.setAlignment(QtCore.Qt.AlignCenter)
        self.frameLY.addWidget(self.leftLI)

        self.rightLI = QtGui.QLabel(self.frame)
        # self.rightLI = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.rightLI.sizePolicy().hasHeightForWidth())
        self.rightLI.setSizePolicy(sizePolicy)
        # self.rightLI.setFrame(False)
        # self.rightLI.setFrameShape(QtGui.QFrame.NoFrame)
        self.rightLI.setAlignment(QtCore.Qt.AlignCenter)
        self.frameLY.addWidget(self.rightLI)

        self.LY.addWidget(self.frame)

        self.rightBU = QtGui.QPushButton(self)
        self.rightBU.setFlat(True)
        # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.rightBU.sizePolicy().hasHeightForWidth())
        # self.rightBU.setSizePolicy(sizePolicy)
        self.rightBU.setText('')
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(':/Right_01.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightBU.setIcon(icon1)
        self.LY.addWidget(self.rightBU)

        self.connect(self.leftBU, QtCore.SIGNAL('clicked()'), self.moveRight)
        self.connect(self.rightBU, QtCore.SIGNAL('clicked()'), self.moveLeft)

        font = QtGui.QFont()
        font.setBold(True)

        self.leftLI.setMaximumWidth(9999)
        self.leftLI.setFont(font)
        # self.leftLI.setStyleSheet('color:#000000; background-color:#FFFFFF;')
        # self.leftLI.setStyleSheet('background-color:#FFFFFF;')

        self.rightLI.setMinimumWidth(0)
        self.rightLI.setFont(font)
        # self.rightLI.setStyleSheet('color:#000000; background-color:#FFFFFF;')
        # self.rightLI.setStyleSheet('background-color:#FFFFFF;')

        self.active = 'left'
        # self.setMaximumHeight(64)
        self.timeLine = QtCore.QTimeLine(500)
        self.timeLine.setUpdateInterval(20)
        self.timeLine.setCurveShape(QtCore.QTimeLine.EaseInOutCurve)
        self.timeLine.setFrameRange(0, 100)

        self.connect(self.timeLine, QtCore.SIGNAL('frameChanged(int)'), self.frameChanged)
        self.connect(self.timeLine, QtCore.SIGNAL("finished()"), self.finished)


    def clear(self):
        # print "CDSlideSelector.clear()"

        self.leftLI.clear()
        self.rightLI.clear()
        self.leftLI.setMinimumWidth(self.frame.width())
        self.leftLI.setMaximumWidth(self.frame.width())
        self.rightLI.setMinimumWidth(0)
        self.rightLI.setMaximumWidth(0)
        self._names = []
        self._data = []
        self._currentIndex = -1
        self._initialIndex = -1
        self.active = 'left'


    def addItem(self, text, data=None):
        # print "CDSlideSelector.addItem()"

        self._names.append(text)
        self._data.append(data)
        if len(self._names) == 1:
            self.leftLI.setText(self._names[0])
            if self._currentIndex == -1:
                # self._currentIndex = 0
                self.roll()
            self.leftBU.setEnabled(False)
            self.rightBU.setEnabled(False)
        else:
            self.leftBU.setEnabled(True)
            self.rightBU.setEnabled(True)


    def finished(self):
        # print "CDSlideSelector.finished()"

        if self.active == 'left':
            self.leftLI.setMinimumWidth(self.frame.width())
            # self.leftLI.setMaximumWidth(self.frame.width())
            self.rightLI.setMaximumWidth(0)
        else:
            self.rightLI.setMinimumWidth(self.frame.width())
            # self.rightLI.setMaximumWidth(self.frame.width())
            self.leftLI.setMaximumWidth(0)

        # if self.status == None:
            # print "status == None"
            # self.buddy.setMaximumSize(QtCore.QSize(16777215, 16777215))
        # else:
            # print "status != None"
            # self.setMaximumSize(QtCore.QSize(16777215, 16777215))
            # if self.orientation == "vertical":
                # if self.buddy.size().height() != 0:
                    # self.buddy.setMaximumSize(QtCore.QSize(16777215, 16777215))

        # self.emit(QtCore.SIGNAL("finished()"))


    def frameChanged(self, index):
        # print "cdSlideSelector.CDSlideSelector.frameChanged()"
        width = self.leftLI.width() + self.rightLI.width()
        self.leftLI.setMinimumWidth(index * width / 100)
        self.leftLI.setMaximumWidth(index * width / 100)
        self.rightLI.setMinimumWidth(width - index * width / 100)
        self.rightLI.setMaximumWidth(width - index * width / 100)


    def isModified(self):
        return not self._currentIndex == self._initialIndex


    def moveLeft(self):
        # print "CDSlideSelector.moveLeft()"

        if len(self._names) > 1:
            if self.active == 'right':
                self.leftLI.setText(self._names[self._currentIndex])
                self.leftLI.setMaximumWidth(999)
                self.roll()
                self.rightLI.setText(self._names[self._currentIndex])
            else:
                self.active = 'right'
                self.rightLI.setText(self._names[self._currentIndex+1])
                self.roll()
            self.timeLine.setDirection(QtCore.QTimeLine.Backward)
            self.timeLine.start()
            self.emit(QtCore.SIGNAL('changed()'))
        else:
            self.roll()

    def moveRight(self):
        # print "CDSlideSelector.moveRight()"

        if len(self._names) > 1:
            if self.active == 'left':
                self.rightLI.setText(self._names[self._currentIndex])
                self.leftLI.setMaximumWidth(0)
                self.roll(-1)
                self.leftLI.setText(self._names[self._currentIndex])
            else:
                self.active = 'left'
                self.roll(-1)
            self.timeLine.setDirection(QtCore.QTimeLine.Forward)
            self.timeLine.start()
            self.emit(QtCore.SIGNAL('changed()'))


    def resizeEvent(self, event):
        # print "CDSlideSelector.resizeEvent()"

        # print  self.frame.width(), self.frame.height()//1.88235294, self.active

        QtGui.QFrame.resizeEvent(self, event)

        # self.leftBU.setMaximumHeight(self.frame.height())
        # self.leftBU.setMaximumWidth(int(self.frame.height()//1.88235294))
        # self.leftBU.setIconSize(QtCore.QSize(int(self.frame.height()//1.88235294), self.frame.height()))

        # self.rightBU.setMaximumHeight(self.frame.height())
        # self.rightBU.setMaximumWidth(int(self.frame.height()//1.88235294))
        # self.rightBU.setIconSize(QtCore.QSize(int(self.frame.height()//1.88235294), self.frame.height()))


        if self.active == 'left':
            self.leftLI.setMinimumWidth(self.frame.width())
            # self.leftLI.setMaximumWidth(self.frame.width())
            self.rightLI.setMaximumWidth(0)
        else:
            self.rightLI.setMinimumWidth(self.frame.width())
            # self.rightLI.setMaximumWidth(self.frame.width())
            self.leftLI.setMaximumWidth(0)

        # print self.frame.width(), self.leftLI.width(), self.rightLI.width()


    def setFont(self, font):

        QtGui.QFrame.setFont(self, font)

        self.leftLI.setFont(font)
        self.rightLI.setFont(font)




if __name__ == '__main__':

    def update():
        label2.setText('{}'.format(widget.currentData()))

        if widget.currentData() == 5:

            widget.clear()

            widget.addItem(u'Unique option', 9)

    aplicacion = QtGui.QApplication(sys.argv)

    main = QtGui.QWidget(None)

    layout = QtGui.QVBoxLayout()

    label = QtGui.QLabel('Prueba de CDSlideSelector')
    label.setAlignment(QtCore.Qt.AlignCenter)
    layout.addWidget(label)

    widget = CDSlideSelector(main)
    layout.addWidget(widget)

    main.connect(widget, QtCore.SIGNAL('changed()'), update)

    label2 = QtGui.QLabel('')
    layout.addWidget(label2)

    main.setLayout(layout)

    widget.setData(['Dato 1', 'Prueba de opcion unica'], [4, 5])


    main.show()


    aplicacion.exec_()
