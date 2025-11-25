# Python Sorting Packages - COS 397 Homework 5
## Team Members 
Liv Anderson, Aiden McGlaufin, Caitlin Moeykens, Garrett Rumery, Alex Sharon
![Sort Lib CI/CD](https://github.com/CapstoneBlackBearScanStream/CICDHW5/actions/workflows/main.yml/badge.svg)

## Description
The goal of this exercise is to implement a Python package for sorting integer lists using the DevOps software development approach. This package implements bubble sort, quick sort, and insertion sort with performance monitoring using Python's psutil library. This project demonstrates best practices, including automated testing, linting, and continuous integration across multiple platforms.

## Feautures
 - Bubble Sort: Monitors CPU usage during sorting 
 - Quick Sort: Measures execution runtime 
 - Insertion Sort: Tracks memory consumption

## DevOps Workflow
### Pre-commit Hooks
- File size limits: prevents committing large files
- Security: Detects AWS credentials and private keys 
- Code formatting: Automatically runs black formatter
- Style checking: Flake8 linting rules 

### Workflow Stages 
1. Linting
2. Testing
3. Packaging 

### Continuous Integration 
- Multiplatform testing: Runs on Linux, macOS, and Windows
- Multi-version support: tests with python 3.9 and 3.10 
- Automated testing: Runs pytest on every push and pull 
- Automated linting: Validates code with black and flake8 

## Performance Measurements 
| Algorithm | Metric | Ubuntu 3.9 | macOS 3.9 | Windows 3.9 | Ubuntu 3.10 | macOS 3.10 | Windows 3.10 | 
| --------- | ------ | ---------- | ----------- | --------- | ---------- | ----------- | ------------ |
| Bubble Sort | CPU (%) | 5.0 | 72.1 | 12.3 | 27.5 | 22.2 | 0 |
| Quick Sort | Runtime (s) | 0.0059 | 0.0070 | 0.0067 | 0.0060 | 0.0037 | 0.0045 |
| Insertion Sort | Memory (MB) | 0 | 0 | 0 | 0 | 0 | 0 | 

## Installation
  pip install -e .
## Run Tests
  pytest -v
