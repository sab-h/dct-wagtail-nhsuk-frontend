from distutils.command.build import build
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    'Wagtail>=2.0',
]

TESTING_REQUIRES = [
    'beautifulsoup4==4.7.1'
]


class CompileCSSCommand(build):
    """Combine CSS from the frontend library with our wagtail-specific fixes"""

    def run(self):
        filepath_base = 'wagtailnhsukfrontend/static/wagtailnhsukfrontend/css/'
        filenames = [
            'nhsuk-3.0.4.min.css',
            'fixes.css',
        ]

        with open(filepath_base + 'wagtail-nhsuk-frontend.min.css', 'w') as outfile:
            for fname in filenames:
                with open(filepath_base + fname) as infile:
                    for line in infile:
                        outfile.write(line)


setup(
    cmdclass={
        'build': CompileCSSCommand,
    },
    name="dct-wagtail-nhsuk-frontend",
    version="0.1.0",
    description="NHSUK Frontend Styles for Wagtail",
    author="Mike Monteith",
    author_email="<mike.monteith@nhs.net>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sab-h/dct-wagtail-nhsuk-frontend",
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    extras_require={'testing': TESTING_REQUIRES},
)
