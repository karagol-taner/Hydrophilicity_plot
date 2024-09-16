from setuptools import setup, find_packages


setup(
    name='hydrophilicity_plot',
    version='0.5',
    license='GPL-3.0',
    description='Kyte-Doolittle hydrophilicity plot tool for FASTA single/multiple protein sequences',
    author="Taner Karagol",
    author_email='taner.karagol@gmail.com',
    url='https://github.com/karagol-taner/HGVS-missense-variants-to-FASTA',
    keywords='hydrophilicity, Kyte-Doolittle, hydropathy, protein structure',
    install_requires=[
          'biopython',
          'matplotlib',
      ],
    packages=['hydrophilicity_plot'],
    package_dir={'hydrophilicity_plot': 'hydrophilicity_plot'},
    entry_points={        'console_scripts': [
            'hydrophilicity_plot = hydrophilicity_plot.hydrophilicity_plot:main',
        ]},
    include_package_data=True,

)
