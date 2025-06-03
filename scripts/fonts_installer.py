import os
import re
import shutil
import sys
import zipfile


ORIGIN_DIR = '/home/vinicius/Downloads'
EXTRATION_DIR = os.path.join(ORIGIN_DIR, 'fonts')
PROJECT_DIR = '/home/vinicius/Desenvolvimento/balacobaco'
SOURCE_DIR = os.path.join(PROJECT_DIR, 'source')
FONTS_DIR = os.path.join(PROJECT_DIR, 'resources', 'fonts')
MAP_PATH = os.path.join(PROJECT_DIR, 'source', 'config', 'fonts_map.cpp')


def extract_all():
    for file in os.listdir(ORIGIN_DIR):
        file = os.path.join(ORIGIN_DIR, file)

        if file.endswith('.zip'):
            if contains_multiple_fonts(file):
                dest_dir = EXTRATION_DIR
            else:
                font_name = os.path.basename(file)
                font_name = os.path.splitext(font_name)[0]
                dest_dir = os.path.join(EXTRATION_DIR, font_name)

            with zipfile.ZipFile(file) as zip_ref:
                zip_ref.extractall(dest_dir)


def contains_multiple_fonts(file):
    return ',' in file


def install_all():
    for folder in os.listdir(EXTRATION_DIR):
        folder = os.path.join(EXTRATION_DIR, folder)

        if not os.path.basename(folder) in os.listdir(FONTS_DIR):
            shutil.move(folder, FONTS_DIR)


def walk_fonts():
    lines = []

    for root, folders, files in os.walk(FONTS_DIR):
        for file in files:
            if file.endswith('.ttf'):
                key = to_natural_case(file)
                path = os.path.join(root, file)
                path = os.path.relpath(path, SOURCE_DIR)
                lines.append(f'{" " * 4}{{"{key}", "{path}"}},\n}};')

    insert_lines(lines);


def to_natural_case(name):
    name = os.path.splitext(name)[0]
    name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
    name = re.sub(r'[-_]', ' ', name)
    name = name.lower()

    return name


def insert_lines(lines):
    map_content = read_map()

    for line in lines:
        if not line in map_content:
            map_content = map_content.replace('};', line)

    write_map(map_content)


def read_map():
    content = ''

    with open(MAP_PATH, 'r') as file:
        content = file.read()

    return content


def write_map(content):
    with open(MAP_PATH, 'w') as file:
        file.write(content)


def main():
    os.makedirs(EXTRATION_DIR, exist_ok=True)
    extract_all();
    install_all();
    walk_fonts();


if __name__ == '__main__':
    main()
