from setuptools import setup, find_packages

setup(
    name='autonomy_control_key',
    version='1.0.0',
    description='Autonomy Control Key AI system implementing the Ω equation for autonomous decision making.',
    author='Luis Ayala',
    author_email='your-email@example.com',
    url='https://github.com/aluisayala/autonomy-control',
    packages=find_packages(),
    install_requires=[
        'openai',
        'requests',
        'python-dotenv',
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)