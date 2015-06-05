from distutils.core import setup

long_description = read('README.txt')

setup(
    name='gity',
    version=sandman.__version__,
    url='https://github.com/mnw2212/gity',
    download_url = '',
    license='MIT',
    author='Mayuresh Waykole',
    author_email='mayuresh2212@gmail.com',
    description='The Git magician for Python',
    long_description=long_description,
    packages=['gity'],
    include_package_data=True,
    platforms='any',
    keywords='python git shell',
    classifiers=[],
)