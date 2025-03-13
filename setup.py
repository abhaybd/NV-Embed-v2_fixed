from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="nv_embed_v2",
    version="0.1.0",
    description="NV-Embed-v2: A generalist embedding model that ranks No. 1 on the Massive Text Embedding Benchmark",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="NVIDIA",
    author_email="chankyul@nvidia.com",
    url="https://github.com/NVIDIA/NV-Embed-v2",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="embeddings, transformers, nlp, machine learning, deep learning",
)
