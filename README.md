# NeXa

## About The Project
NeXa is a social networking platform designed to connect ALX students and alumni, fostering a vibrant online community for knowledge sharing, mentorship, and collaboration to empower personal and professional growth.

### Built using

- Flask 
- HTML
- CSS
- Javascript

## Getting Started

### Prerequisites

Ensure you have the following installed:
- [Python3](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [Git](https://git-scm.com/)

### Installation:
```bash
git clone https://github.com/ugberaeseac/NeXa
cd NeXa
```

### Virtual Environment
```bash
python3 -m venv venv
```

To activate the virtual environment
* On Unix
```bash
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r dependencies.txt
```

### Environment Variables
```bash
source setup_env.sh
```

### Setup MySQL
```bash
cat setup_mysql_dev.sql | sudo mysql #add -p flag if passworded
```

### Start the Application
```bash
python3 -m run
```
Access the application in your browser at http://localhost:5000

## Authors
Williams Akanni - [Github](https://github.com/shadowbanks) / [Twitter](https://twitter.com/ghostProTech)  
UGBERAESE Charles A. - [Github](https://github.com/ugberaeseac) / [Twitter](https://twitter.com/ugberaeseac)
