from setuptools import setup, find_packages

version = '0.0.2'

setup(
    name='gity',
    version=version,
    url='https://github.com/mnw2212/gity',
    license='MIT',
    author='Mayuresh Waykole',
    author_email='mayuresh2212@gmail.com',
    description='The Git magician for Python',
    long_description=open('README.md').read(),
    packages=['gity'],
    include_package_data=True,
    platforms='any',
    keywords='python git shell',
    classifiers=[],
)
