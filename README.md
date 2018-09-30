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
cd GT_CAP_GCTS

# Create a new Python 3.6 virtualenv in a directory named 'env'
virtualenv -p python3.6 env

(for windows) virtualenv -p python.exe env

# Activate the virtualenv
source env/bin/activate

(for windows)C:\Users\(username)\GT_CAP_GCTS\env\Scripts\activate

# Install Python dependencies for development
pip install -r requirements/base.txt
```

### Running static code analyser
```bash
prospector
```

### Checkout a branch into a local repository
```bash
git checkout development

(to check which branch you in) git branch

```
