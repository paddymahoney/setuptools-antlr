"""Setup script for setuptools-antlr."""

# need to guard script here due to reentrance while testing multiprocessing:
if __name__ == '__main__':
    from setuptools import setup, find_packages
    from sys import version_info, argv

    if version_info < (3, 5):
        print('This Python version is not supported, minimal version 3.5 is required.')
        exit(1)

    needs_pytest = {'pytest', 'test', 'ptr'}.intersection(argv)
    pytest_runner_opt = ['pytest-runner>=2.0,<3dev'] if needs_pytest else []

    needs_pylint = {'lint'}.intersection(argv)
    setuptools_lint_opt = ['setuptools-lint>=0.4,<0.5dev'] if needs_pylint else []

    needs_flake8 = {'flake8'}.intersection(argv)
    flake8_opt = ['flake8>=2.0,<3dev', 'flake8-import-order>=0.9,<0.10dev',
                  'flake8-todo>=0.5,<0.6dev', 'pep8-naming>=0.3,<0.4dev'] if needs_flake8 else []

    setup(
        name='setuptools-antlr',
        version='0.0.1',
        packages=find_packages(),
        package_data={'setuptools_antlr': ['lib/antlr-4.5.3-complete.jar', 'lib/LICENSE.txt']},
        entry_points={
            "distutils.commands": [
                "antlr = setuptools_antlr.build_antlr:build_antlr",
            ]
        },
        tests_require=[
            'pytest-cov', 'pytest-mock'
        ],
        setup_requires=pytest_runner_opt + setuptools_lint_opt + flake8_opt,
        url='https://github.com/ferraith/setuptools-antlr',
        license='MIT',
        author='Andreas Schmidl',
        author_email='Andreas.Schmidl@gmail.com',
        description='Setuptools command for generating ANTLR based parsers.',
        keywords='antlr setuptools dsl',
        classifiers=[
            'Development Status :: 2 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'License :: Other/Proprietary License',
            'Programming Language :: Python :: 3.5'
        ]
    )
