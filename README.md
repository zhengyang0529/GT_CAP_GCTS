# GT_CAP_GCTS

### Cloning the Repository:
```bash
git clone git@github.com:zhengyang0529/GT_CAP_GCTS.git

(for windows) https://github.com/zhengyang0529/GT_CAP_GCTS.git
```

### Setting up a Virtualenv

It's recommended to install the project's dependencies into a virtual env.
```bash
# Go into the project directory
cd JPT-CAP-GCTS

# Create a new Python 3.6 virtualenv in a directory named 'env'
virtualenv -p python3.6 env

# Activate the virtualenv
source env/bin/activate

# Install Python dependencies for development
pip install -r requirements/base.txt
```

### Running static code analyser
```bash
prospector
```
