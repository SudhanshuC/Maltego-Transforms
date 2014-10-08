from setuptools import setup, find_packages

setup(
    name='haveibeenpwned',
    author='Christian Heinrich',
    version='1.0',
    author_email='christian.heinrich@cmlh.id.au',
    description='cmlh.id.au',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
