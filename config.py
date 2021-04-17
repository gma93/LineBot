import os
from pathlib import Path
import configparser

dic_api_condig = {}

def read_ini():
    """iniファイルの設定値をディクショナリに格納します。"""
    config = configparser.ConfigParser()
    path = os.path.join(Path(__file__).parent, "config.ini")
    config.read(path)
    config.optionxform = str

    for section in config.sections():
        for key in config.options(section):
            dic_api_condig[key] = config.get(section, key)

if __name__ == '__main__':
    read_ini()