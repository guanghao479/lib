import os
import logging
import shutil

# Create console logging
logger = logging.getLogger('django-move-template')
console = logging.StreamHandler()

if __debug__:
    logger.setLevel(logging.DEBUG)
    console.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.ERROR)
    console.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

cwd = os.getcwd()
template_dir = os.path.join(cwd, 'mymd/templates')

logger.debug('cwd: ' + cwd)
logger.debug('template_dir: ' + template_dir)

for dir_temp in get_immediate_subdirectories(template_dir):
    dir_src = os.path.join(template_dir, dir_temp)
    dir_dst = os.path.join(cwd, dir_temp, 'templates', dir_temp)
    if (os.path.exists(os.path.join(cwd, dir_temp))):
        shutil.copytree(dir_src, dir_dst)
        shutil.rmtree(dir_src)
        logger.debug('dir_temp: ' + dir_temp)
