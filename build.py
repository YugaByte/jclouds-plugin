#!/usr/bin/env python3

import subprocess
import os
import shutil


def build():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    shutil.rmtree(os.path.join(project_dir, 'target'))
    shutil.rmtree(os.path.join(project_dir, 'jclouds-plugin', 'target'))
    shutil.rmtree(os.path.join(project_dir, 'jclouds-shaded', 'target'))
    subprocess.check_call(['mvn', '-DskipTests', 'install'], cwd=project_dir)
    subprocess.check_call(['mvn', 'hpi:hpi'],
                          cwd=os.path.join(project_dir, 'jclouds-plugin'))


if __name__ == '__main__':
    build()
