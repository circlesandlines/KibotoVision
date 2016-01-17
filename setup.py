from setuptools import setup

reqs = ["pyautogui", "pyscreenshot"]

setup(
    name="KibotoVision",
    version="0.0.0",
    install_requires=reqs,
    author="Radu Nicolae",
    author_email="ranicolae@gmail.com",
    description="KibotoVision grabs screenshots periodically for you to analyze",
    license="AGPL",
    keywords="AI brain kiboto vision machine learning",
    url="git@github.com:circlesandlines/KibotoVision.git",
    packages=["KibotoVision"]
)
