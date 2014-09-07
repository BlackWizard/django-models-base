from setuptools import setup, find_packages

setup(
    name='django-models-base',
    version='1.0',
    description='Base miscellaneous models for django.',
    long_description=open('README.md').read(),
    author='BlackWizard',
    author_email='BlackWizard@mail.ru',
    url='http://github.com/BlackWizard/django-models-base',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
