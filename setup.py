from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='A short transcription service.',
    author='Guilherme Silveira',
    author_email='guilherme.silveira@caelum.com.br',
    license='copyright',
    python_requires='>=3.6',
    install_requires=['google-cloud-speech','ffmpy','google-cloud-storage','simplejson'],
)

