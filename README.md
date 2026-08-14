# Machine_Learning

A repository made for machine learning algorithms implemented with python

```bash
# basic setup for WSl on Windows

# update and dependency installation
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv python3-dev -y

# creates the runtime environment (venv folder)
python3 -m venv venv

# activates runtime environment for this project on Linux/WSL (using terminal activation from venv folder)
# for terminal usage has to run everytime
source venv/bin/activate

# AI & ML dependencies (pip only)
pip install numpy pandas matplotlib scikit-learn tensorflow torch seaborn

# AI & ML dependencies (venv pip only)
venv/bin/python -m pip install numpy pandas matplotlib scikit-learn tensorflow torch seaborn
```
