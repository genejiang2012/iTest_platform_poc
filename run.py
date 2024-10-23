
# Author: gene.jiang
# Date: 2024-10-23 19:27:00
# LastEditors: gene.jiang
# LastEditTime: 2024-10-23 19:28:12
# Description: file content
# FilePath: \iTest_platform_poc\run.py


from app import iTest

@iTest.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    iTest.run(host='0.0.0.0', port=5000, debug=True)