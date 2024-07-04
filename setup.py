from setuptools import setup, find_packages  # type: ignore

setup(
    name='kmvahini',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pandas',
        'lxml',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'run_scraper=kmvahini.scraper:main',
        ],
    },
    author='Manojkumar Patil',
    author_email='patil.manojkumar@hotmail.com',
    description='Fetch Price data from Krishimaratvahini website',
    url='https://github.com/patilmanojkumar/kmvahini',
    project_urls={
        'Source': 'https://github.com/patilmanojkumar/kmvahini',
        'Bug Reports': 'https://github.com/patilmanojkumar/kmvahini/issues',
    },
)
