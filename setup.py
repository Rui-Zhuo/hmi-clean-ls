 # Edited by Rui, 2025/11/13
# File: setup.py
from setuptools import find_packages, setup

# setup(
#     use_scm_version=True,
#     name="hmi_clean",
#     packages=find_packages(where="src"),
#     package_dir={"", "src"},
# ) # Edited by Rui, 2025/11/13

setup(
    version="0.1.0",
    name="hmi_clean",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyshtools",
        "sunpy",
        "matplotlib",
        "astropy",
        "numpy",
        "argparse",
    ],
)  # Edited by Rui, 2025/11/13
