from setuptools import find_packages, setup

from habra_favorites import get_version


def get_long_description():
    with open('README.rst', encoding='utf-8') as f:
        return f.read()


setup(
    name='habra-favorites',

    author='Yan Kalchevskiy',
    author_email='yan.kalchevskiy@gmail.ru',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    description='Sort your favorites posts from Habrahabr.ru',
    include_package_data=True,
    keywords=['scrapy', 'habr.com', 'bookmarks', 'favorites'],
    license='MIT',
    long_description=get_long_description(),
    packages=find_packages(),
    package_data={
        '': ['*.html'],
    },
    url='https://github.com/ykalchevskiy/habra-favorites',
    version=get_version(),

    entry_points={
        'console_scripts': ['habra_favorites = habra_favorites.main:main']
    },
    install_requires=[
        'scrapy',
    ]
)
