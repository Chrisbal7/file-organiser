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

from send2trash import send2trash

from lib import *

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s -%(asctime)s %(message)s')


# logging.disable()


def get_extension(path):
    extension = os.path.splitext(path)[-1]
    if extension:
        return extension[1:]


def generate_hash(path):
    if os.path.exists(path):
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


# For media files only
def delete(file_path):
    send2trash(file_path)
    logging.debug(f'{os.path.basename(file_path)} DELETED')


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


# Index all files inside a folder
def index_all_files(mountpoints):
    files = set()
    logging.debug('Indexing...')
    for mountpoint in mountpoints:
        for parent_path, subfolders, filenames in os.walk(mountpoint):
            for subfolder in subfolders:
                if subfolder in reserved_dirs:
                    continue
            for filename in filenames:
                files.add(os.path.join(parent_path, filename))

    logging.debug(f'{len(files)}files indexed successfully')
    return files


def remove_duplicates(files_path):
    files_dict = {}
    hashes = []
    to_delete = []
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
                    to_delete.append(file_dir)
                    saved_space += os.stat(file_dir).st_size
                else:
                    hashes.append(hash_digest)
    logging.debug(f'{print_size(saved_space)} to be freed')
    return to_delete


def init():
    dup_files = ''
    logging.debug('Welcome...')
    partitions = set()
    partitions_input = input('Enter les partitions manuellement?\n'
                             '\'Y\': Oui, \'Enter\' : Non\n')
    while partitions_input:
        partition_provided = input()
        if os.path.exists(partition_provided):
            partitions.add(partition_provided)
        else:
            partitions_input = ''

    remove_dup = input('Supprimer des doublons?\n'
                       '\'Y\' : Oui, \'Enter\': refuser\n')

    if remove_dup:
        dup_files = remove_duplicates(index_all_files(partitions))

    delete_input = input('Delete all?\n'
                         '\'Y\' : Yes, \'Enter\': Non\n')

    if delete_input:
        for dup_file in dup_files:
            delete(dup_file)
    else:
        for dup_file in dup_files:
            validate_deletion = input(f'Delete {os.path.basename(dup_file)}?\n'
                                      '\'Y\' : Yes, \'N\': Non\n')
            if validate_deletion.lower() == 'y':
                delete(dup_file)


init()
