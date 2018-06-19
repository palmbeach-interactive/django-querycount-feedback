from setuptools import setup, find_packages
import os
import querycount_feedback

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
]

setup(
    author="Jonas Ohrstrom",
    author_email="jonas@pbi.io",
    name='django-querycount-feedback',
    version=querycount_feedback.__version__,
    description='Slick admin styles for Django and django CMS.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/palmbeach-interactive/django-querycount-feedback/',
    license='MIT License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'django-querycount>=0.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
