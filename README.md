# Easy Pipeline Kit

Pipe your functions.

## Install

`pip install git+https://github.com/yoshiso/ppkit.git`


## Usage

```
from ppkit import make_pipeline

pipeline = (
    make_pipeline()
        .pipe(np.log)
        .pipe(lambda data: data + 1)
        .pipe(lambda data: data * 2)
)
pipeline.execute(np.array([1, 2, 3, 4, 5]))
>>> array([ 2.        ,  3.38629436,  4.19722458,  4.77258872,  5.21887582])
```
