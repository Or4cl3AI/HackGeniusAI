```python
from setuptools import setup, find_packages

setup(
    name='HackGeniusAI',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tensorflow',
        'pytorch',
        'nltk',
        'flask',
        'tkinter',
        'ARCore',
        'ARKit'
    ],
    entry_points={
        'console_scripts': [
            'hackgeniusai = hackgeniusai.main:main'
        ]
    },
    author="HackGeniusAI Team",
    author_email="info@hackgeniusai.com",
    description="A revolutionary and immersive virtual gamified hacking tutorial",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HackGeniusAI/hackgeniusai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```