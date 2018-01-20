from setuptools import setup

setup(
        name='plazapp',
        version='0.0.1',
        packages=['plazapp'],
        include_packages_data=True,
        install_requires=[
            'Flask==0.12.2',
        ],
    )
