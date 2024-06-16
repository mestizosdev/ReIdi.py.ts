## Create python virtual environment
```
virtualenv venv
```
or
```
virtualenv -p python3.12 venv
```
or
```
python3.12 -m venv venv
```
## Activate python virtual environment
```
source venv/bin/activate
```
## Update pip and tools
```
pip install -U pip
pip install --upgrade wheel
pip install --upgrade setuptools
```
## Install linter and code formatter (Ruff)
```
pip install ruff
```
### Check syntax
```
ruff check .
```
### Format
```
ruff format .
```
## Install dependencies
```
pip install -r requirements.txt
```

