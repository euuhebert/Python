import os
import shutil
from pathlib import Path


ROOT_PATH = Path(__file__).parent


#os.mkdir(ROOT_PATH / 'new-diretorio')

arquivo = open(ROOT_PATH /'novo.txt', 'w')
arquivo.close()

os.rename(ROOT_PATH/'new.txt', ROOT_PATH/'teste.txt')


