IRTS Notebook
=============

Notebooks to explore pyIRTS. I hope this repository will host a collection of notebooks exploring the development of an "IRTS" python library and give the option of exploring IRTS with a notebook.

# Setting up the Environement

Creating the repository with GitHub CLI:

```
(pyIRTS) mgarcia@PC-KL-26743:~/Work$ gh repo create kaust-library-systems/irts_notebook \
--public \
--add-readme \
--description "Notebooks to explore pyIRTS" \
--license MIT \
--gitignore Python
✓ Created repository kaust-library-systems/irts_notebook on github.com
  https://github.com/kaust-library-systems/irts_notebook
(pyIRTS) mgarcia@PC-KL-26743:~/Work$
```

Next we initialize the UV environment

```
(pyIRTS) mgarcia@PC-KL-26743:~/Work$ cd irts_notebook/
(pyIRTS) mgarcia@PC-KL-26743:~/Work/irts_notebook$ uv init
Initialized project `irts-notebook`
(pyIRTS) mgarcia@PC-KL-26743:~/Work/irts_notebook$ 
```

I forgot to deactivate the previous virtual environment, and I got a warning when I tried to install `marimo` inside the UV environment since UV also initalize its own virtual environment. Looking at the message from UV, it seems that Marimo was installed on the correct virtual enviroment, `.venv`.

```
(pyIRTS) mgarcia@PC-KL-26743:~/Work/irts_notebook$ uv add marimo
warning: `VIRTUAL_ENV=/home/mgarcia/Work/pyIRTS/venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
Using CPython 3.13.6
Creating virtual environment at: .venv
Resolved 25 packages in 4.00s
Prepared 8 packages in 7.91s
Installed 23 packages in 102ms
 + anyio==4.11.0
 + click==8.3.0
 (...)
```

