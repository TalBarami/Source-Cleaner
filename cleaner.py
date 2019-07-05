import zipfile
import glob
import os
from os import listdir, mkdir
from os.path import isfile, join


def unzip(src, dst):
    with zipfile.ZipFile(src, 'r') as file:
        print(f"unzipping: {src} to {dst}")
        file.extractall(dst)


def unzip_all(src, dst):
    files = [f for f in listdir(src) if isfile(join(src, f))]
    src_paths = [join(src, f) for f in files]
    dst_paths = [join(dst, f[0:6]) for f in files]
    for s, d in zip(src_paths, dst_paths):
        unzip(s, d)


def unzip_jars(path):
    jars = [jar_file for jar_file in glob.glob(os.path.join(path, '**/*.jar'), recursive=True)]
    for jar in jars:
        dir_path = os.path.dirname(jar)
        unzip(jar, dir_path)


def clean_files(path):
    source_files = [f for f in glob.glob(os.path.join(path, '**/*.java'), recursive=True)]
    all_files = list(set([f for f in glob.glob(os.path.join(path, '**/**'), recursive=True) if isfile(f)]))
    res = [f for f in all_files if 'java' not in f]
    for f in all_files:
        if f not in source_files:
            print(f"removing: {f}")
            os.remove(f)


if __name__ == "__main__":
    src = 'C:/Users/talba/Desktop/hw3/Assignment 3'
    dst = 'C:/Users/talba/Desktop/hw3/unzipped'
    check = 'C:/Users/talba/Desktop/hw3/check'
    # unzip_all(src, dst)
    # unzip_jars(dst)
    # clean_files(dst)
    unzip_all(src, check)
    unzip_jars(check)
