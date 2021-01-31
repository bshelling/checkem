# Checkem
Python application compares the checksum hash of two files. The is a important step when it comes to ensuring a downloaded from it's owner hasn't be altered in anyway.

## Installation
This can be ran globally or from an virtualenv(recommended)
```
# Create, activate environment and install dependencies
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip -i requirements.txt
```

## Usage
From the directory of the original file run
```
$ python app.py
$ Enter the original file's checksum: [original file's hash]
$ Enter the name of the file to validate: [new file's name]
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

