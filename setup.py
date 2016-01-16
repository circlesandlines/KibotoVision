from setuptools import setup

reqs = ["pyautogui", "pyscreenshot"]

setup(
    name="brain",
    version="0.0.0",
    install_requires=reqs,
    author="Radu Nicolae",
    author_email="ranicolae@gmail.com",
    description="KibotoVision grabs screenshots periodically for you to analyze",
    licence="AGPL",
    keywords="AI brain kiboto vision machine learning",
    url="git@github.com:circlesandlines/KibotoVision.git",
    packages=["brain"]
)
