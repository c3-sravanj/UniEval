from setuptools import setup, find_packages


setup(
    name="unieval",
    version=1.0,
    description="Fork of UniEval.",
    url="https://github.com/c3-sravanj/UniEval",
    author="UniEval",
    author_email="UniEval@gmail.com",
    packages=find_packages(include=["unieval"], exclude=["tests", "tests.*"]),
    install_requires=(
        [
            "transformers >= 4.17.0.dev0",
            "accelerate",
            "datasets >= 1.8.0",
            "sentencepiece != 0.1.92",
            "protobuf",
            "rouge-score",
            "nltk",
            "py7zr",
            "torch >= 1.3",
            "evaluate",
            "prettytable",
        ]
    ),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
