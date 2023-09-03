from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vkauth',
    version='1.0.0',
    author='Maehdakvan',
    author_email='visitanimation@google.com',
    description='Library that helps you to authenticate with VK.com using cookies from your browser. The library automatically fetches required cookies from supported browsers, establishes a session, and retrieves an access token',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DedInc/vkauth',
    project_urls={
        'Bug Tracker': 'https://github.com/DedInc/vkauth/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['psutil', 'requests', 'browser_cookie_3x'],
    python_requires='>=3.6'
)