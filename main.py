#!/usr/bin/env python3
"""
--------------------- FILE ORGANISER ----------------------------

This program scan all the drives connected to a PC, and sort all
data based on the type, the author, the category, so remove all
unnecessary duplicate files, and organize them into folders to
usually be suitable for searching them

--------------------Developed by Chrisbal------------------------

"""

import hashlib
import logging
import os
from platform import system
from re import compile

from psutil import disk_partitions

from lib import *

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s -%(asctime)s %(message)s')


class Partition:
    def __init__(self, partition):
        self.partition_path = partition.device
        self.mount_point = partition.mountpoint


def get_extension(path):
    extension_regex = compile(fr'([.]\w+)$')
    try:
        return extension_regex.search(os.path.basename(path)).group()[1:]
    except AttributeError:
        return None


def generate_hash(path):
    try:
        with open(path, 'rb') as file_binary:
            digest = hashlib.sha256()
            block_size = 65356
            file_block = file_binary.read(block_size)
            while len(file_block) > 0:
                digest.update(file_block)
                file_block = file_binary.read(block_size)
            if digest:
                return digest.hexdigest()
    except PermissionError:
        pass
    except FileNotFoundError:
        pass


# For media files only
def delete(file_path):
    # send2trash(file_path.directory)
    logging.debug(f'Deleting {os.path.basename(file_path)} at'
                  f' {os.path.dirname(file_path)}...')


def print_size(size):
    multiples = ['', 'K', 'M', 'G', 'T', 'E']
    index = 0
    while size > 1024:
        size = size / 1024
        index += 1
    try:
        prefix = multiples[index]
    except IndexError:
        prefix = ''
    return f'{round(size, 2)} {prefix}B'


def get_partitions():
    logging.debug('Looking for all mounted partitions...')

    all_partitions = set()
    partitions = disk_partitions()
    logging.debug(f'Mountpoints found :')
    for partition in partitions:
        if system().lower() == 'linux' and 'loop' in partition.device:
            continue
        all_partitions.add(Partition(partition))
    return all_partitions


# Index all files inside a folder
def index_all_files(*mountpoints):
    files = []
    logging.debug('Indexing...')
    for mountpoint in mountpoints:
        for parent_path, subfolders, filenames in os.walk(mountpoint):
            for filename in filenames:
                files.append(os.path.join(parent_path, filename))
        logging.debug(f'{len(files)}files indexed successfully')
    return files


def remove_duplicates(files_path):
    files_dict = {}
    hashes = []
    saved_space = 0
    for file_path in files_path:
        if os.path.exists(file_path) and \
                get_extension(file_path) in media_formats:
            if os.access(file_path, os.R_OK) and \
                    os.access(file_path, os.W_OK):
                size = os.stat(file_path).st_size
                if files_dict.get(size, False):
                    files_dict[size].append(file_path)
                else:
                    files_dict.setdefault(size, [file_path])

    for file_dirs in files_dict.values():
        if len(file_dirs) > 1:
            for file_dir in file_dirs:
                hash_digest = generate_hash(file_dir)
                if hash_digest in hashes:
                    delete(file_dir)
                    saved_space += os.stat(file_dir).st_size
                else:
                    hashes.append(hash_digest)

    logging.debug(f'{print_size(saved_space)} to be freed')


remove_duplicates(index_all_files('/'))
