# Friendpaste API

## Installation
`pip install friendpaste-api`

## Requirements
- [requests](http://docs.python-requests.org/en/master/)

## Usage
```python
from friendpaste import fp_write

# Update post using hash
fp_write('y0Z1ia3h47j8ddRSn2QiPy', 'My new text')
```

## Authoring
```
python setup.py sdist
twine upload dist/*
```

https://pypi.org/project/friendpaste-api/