import os
import platform

# Autotest information
testdir = 'temp'
if not os.path.isdir(testdir):
    os.mkdir(testdir)
target_dict = {}

exclude = None
retain = False

# Compiling information
fc = 'gfortran'
# fc = 'ifort'
target_extension = ''
target_arch = 'intel64'
if platform.system() in 'Windows':
    target_extension = '.exe'

# Development version information
testpaths = [os.path.join('..', 'test-reg'),]
srcdir = os.path.join('..', 'src')
program = 'mt3d-usgs'
version = '1.0.00'
target = os.path.join('temp', program + '_' + version + target_extension)
target_dict[os.path.basename(target)] = target

# Release version information
loc_release = os.path.join('..', 'mt3dms')
dir_release = os.path.join('temp', 'mt3dms')
srcdir_release = os.path.join(dir_release, 'src')
version_release = '5.3.00'
target_release = os.path.join('temp', program + '_' + version_release +
                              target_extension)
target_dict[os.path.basename(target_release)] = target_release
target_dict[program] = target_release

# Comparison information
target_dict['mfnwt'] = 'mfnwt' + target_extension