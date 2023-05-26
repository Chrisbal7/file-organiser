#!/usr/bin/python3
"""
_------------------------- FILE ORGANISER ----------------------

This program scan all the drives connected to a PC, and sort all
datas based on the type, the author, the category, so remove all
unnecessary duplicate files, and organize them into folders to
usually be suitable for searching them

-----------------------------------------------------------------

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
So datas can be provided in a disorder way, the program
will get the shit well organized
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""


# import os
# import re

# Recognize all the drives mounted and their respective filesystem
#  for Windows: NTFS, FAT16, FAT32
# for Linux: Ext2, Ext3, Ext4
# for macOs: APFS, HFS

class DriveInfo:
    def __init__(self, mounted_letter):
        self.mounted_letter = mounted_letter

    # def get_filesystem(self):
    # A method for determine the filesystem of the drive


# Datas to be indexed
# Store all extensions in lists
audioExtensions = ['aa', 'aac', 'aax', 'act', 'aiff', 'alac', 'amr',
                   'ape', 'au', 'awb', 'dss', 'dvf', 'flac', 'gsm',
                   'iklax', 'ivs', 'm4a', 'm4b', 'm4p', 'mmf', 'mp3'
                   'mpc', 'msv', 'nmf', 'ogg', 'oga', 'mogg', 'opus',
                   'ra', 'rm', 'raw', 'rf64', 'sln', 'tta', 'voc',
                   'vox', 'wav', 'wma', 'wv', 'webm', '8svx', 'cda']

videoExtensions = ['webm', 'mkv', 'flv', 'ogv', 'ogg', 'drc', 'gifv',
                   'mng', 'avi', 'mts', 'm2ts', 'ts', 'mov', 'qt',
                   'wmv', 'yuv', 'rm', 'rmvb', 'viv', 'asf', 'amv',
                   'mp4', 'm4p', 'm4v', 'mpg', 'mp2', 'mpeg', 'mpe',
                   'mpv', 'm2v', 'svi', '3gp', '3g2', 'mxf', 'roq',
                   'nsv', 'flv', 'f4v', 'f4p', 'f4a', 'f4b']

imageExtensions = ['jpeg', 'jpg', 'gif', 'png', 'webp', 'jp2', 'hdr',
                   'heif', 'avif', 'jxl', 'tiff', 'bmp', 'ppm', 'pgm',
                   'pbm', 'pnm', 'svg']

documentExtensions = ['txt', 'docx', 'xlsx', 'doc', 'djvu', 'doc',
                      'html', 'htm', 'fb2', 'md', 'odt', 'sxw', 'oxps',
                      'pdf', 'ps', 'rtf', 'svg', 'wpd', 'wp', 'wp7',
                      'ppt', 'pptx', 'xls', 'epub']

archiveExtensions = ['a', 'ar', 'cpio', 'shar', 'lbr', 'iso', 'mar',
                     'sbx', 'tar', 'br', 'bz2', 'f', 'xf', 'genozip',
                     'gz', 'lz', 'lz4', 'lzma', 'lzo', 'rz', 'sfark',
                     'sz', 'q', 'z', 'xz', 'zst', '7z', 's7z', 'ace',
                     'afa', 'alz', 'apk', 'arc', 'ark', 'cdx', 'arj',
                     'b1', 'b6z', 'ba', 'bh', 'cab', 'car', 'cfs',
                     'cpt', 'dar', 'dd', 'dgc', 'dmg', 'ear', 'gca',
                     'ha', 'hki', 'ice', 'jar', 'kgb', 'lzh', 'lha',
                     'lzx', 'pak', 'partimg', 'paq6', 'paq7', 'paq8',
                     'pea', 'phar', 'pim', 'pit', 'qda', 'rar', 'rk',
                     'sda', 'sea', 'sen', 'sfx', 'shk', 'sit', 'sitx',
                     'sqx', 'tar.gz', 'tgz', 'tar.z', 'tar.bz2', 'tbz2',
                     'tar.lz', 'tlz', 'tar.xz', 'txz', 'tar.zst', 'uc',
                     'uc0', 'uc2', 'ucn', 'ur2', 'ue2', 'uca', 'uha',
                     'war', 'wim', 'xar', 'xp3', 'yz1', 'zip', 'zipx',
                     'zoo', 'zpaq', 'zz', 'ecc', 'ecsbx', 'par', 'par2',
                     'rev']

packageExtensions = ['deb', 'pkg', 'mpkg', 'rpm', 'tgz', 'msi', 'jar',
                     'crx', 'pkg.tar.zst', 'pkg.tar', 'apk']
