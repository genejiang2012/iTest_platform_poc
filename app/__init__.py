
# Author: gene.jiang
# Date: 2024-10-23 19:25:08
# LastEditors: gene.jiang
# LastEditTime: 2024-10-23 19:25:59
# Description: file content
# FilePath: \iTest_platform_poc\app\__init__.py

from flask import Flask
from config import Config

iTest = Flask(__name__)
iTest.config.from_object(Config)