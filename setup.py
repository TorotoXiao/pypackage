from setuptools import setup

setup(
    name='testpackage',
    version='1.0.6',
    packages=['testpackage'],
    license="MIT",
    author='Sophia',
    author_email="Sophia@qq.com",
    url='https://github.com/TorotoXiao/pypackage',
    description="test publish package to github",
    install_requires=["pycrypto"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
