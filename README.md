# ggi

**ggi** stands for “generate .gitignore” — a simple CLI tool to create .gitignore files for your projects based on the specified programming language.

## Installation

1.	Install pipx if you haven’t already:

    ```bash
    pip install pipx
    pipx ensurepath
    ```

2.	Install ggi globally using pipx:

    ```bash
    pipx install git+https://github.com/your-username/ggi.git
    ```


## Usage

Generate a .gitignore file for your project:
```
ggi --lang python
```
This will create a .gitignore file in the current directory for Python projects.
