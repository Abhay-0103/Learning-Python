# Learning Python

A hands-on Python learning repository organized topic-by-topic, from basics to async programming.

This project is designed as a practical course workspace where each folder focuses on one concept and contains short, runnable examples.

## What You Will Learn

- Python fundamentals and syntax
- Data types and core operations
- Conditionals and loops
- Functions and scope
- Comprehensions and generators
- Decorators and object-oriented programming
- Exception handling
- Threads, multiprocessing, and concurrency basics
- Async programming patterns
- Introductory Pydantic structure

## Repository Structure

```text
00_python/               Intro examples
01_basics/               Very first Python scripts
01_virtual/              Virtual environment and requirements
02_datatypes/            Data type focused chapters
03_conditionals/         Conditional mini stories
04_loops/                Looping exercises
05_func/                 Functions, scope, parameters, return values
06_chai_business/        Mini project style folder (recipes + utils)
07_comprehensions/       List, set, dict, generator comprehensions
08_generators/           Generator basics and advanced controls
09_decorators/           Decorator patterns
10_oop/                  OOP concepts and class behavior
11_exceptions/           Exception handling notebooks
12_threads_concurrency/  Threading + multiprocessing examples
13_async/                Async and worker pattern examples
14_pydantic/             Pydantic learning area
```

## Prerequisites

- Python 3.10 or newer
- pip (comes with Python)
- Git (optional, for cloning)

## Setup

### 1) Clone the repository

```bash
git clone https://github.com/Abhay-0103/Learning-Python.git
cd Learning-Python
```

### 2) Create and activate a virtual environment

#### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### Windows (CMD)

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

If needed, install from the course requirements file:

```bash
pip install -r 01_virtual/requirements.txt
```

If the file is empty or minimal, you can still run most scripts directly without extra packages.

## How To Run Files

From the repository root, run any script with Python:

```bash
python 01_basics/pythontest.py
python 02_datatypes/chapter_1.py
python 04_loops/06_while.py
python 09_decorators/02_logging_dec.py
```

For notebook-based chapters, open the `.ipynb` files in VS Code (or Jupyter) and run cells interactively.

## Suggested Learning Path

1. Start with `00_python` and `01_basics`
2. Move through `02_datatypes`, `03_conditionals`, and `04_loops`
3. Continue with `05_func` and `07_comprehensions`
4. Learn `08_generators` and `09_decorators`
5. Study `10_oop` and `11_exceptions`
6. Finish with `12_threads_concurrency` and `13_async`
7. Explore `06_chai_business` and `14_pydantic`

## Notes

- File names include chapter numbers to keep a teaching sequence.
- Some files are intentionally simple and short for concept clarity.
- A few names may contain typos from in-course iteration (kept as-is to preserve lesson continuity).

## Author

Created and maintained by Abhay Singh.
