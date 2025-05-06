# Class: `LogWriter`

**Description:** This class makes an object that is bound to a run row in the result table. This means that everything that is
logged through this object is added into the result table and this object can be used to interact with a specific
run. This object is single use. This means that once the final results are written, the object becomes read-only.

You should not instantiate this class directly, but use the ResultTable class to create it instead.

## Method: `add_hparams()`

```python
add_hparams(self, **kwargs)
```

**Description:** Add hyperparameters to the result table

**Parameters:**
- `kwargs`: The hyperparameters to save

## Method: `add_scalar()`

```python
add_scalar(self, tag: str, scalar_value: Union[float, int], step: Optional[int] = None, epoch: Optional[int] = None, walltime: Optional[float] = None, flush: bool = False)
```

**Description:** Add a scalar to the resultTable

**Parameters:**
- `tag`: The tag, formatted as: 'split/name' or simply 'split'
- `scalar_value`: The value
- `step`: The global step. If none, the one calculated is used
- `epoch`: The epoch. If None, none is saved
- `walltime`: Override the wall time with this
- `flush`: Force flush all the scalars in memory

## Method: `get_hparams()`

```python
get_hparams(self) -> Dict[str, Any]
```

**Description:** Get the hyperparameters of the current run

**Return:**
- A dict of hyperparameters
## Method: `get_repetitions()`

```python
get_repetitions(self) -> List[int]
```

**Description:** Get the all the repetitions ids of the current run

**Return:**
- A list of repetitions ids
## Method: `new_repetition()`

```python
new_repetition(self)
```

**Description:** Create a new repetition of the current run. This is useful if you want to log multiple repetitions of the same
run. This is a mutating method, meaning that you can call it at the end of the training loop before the next
full training loop is run again.

## Method: `read_scalar()`

```python
read_scalar(self, tag) -> List[deepboard.resultTable.scalar.Scalar]
```

**Description:** Read a scalar from the resultTable with the given tag

**Parameters:**
- `tag`: The tag to read formatted as: 'split/name' or simply 'split'.

**Return:**
- A list of Scalars items
## Method: `set_status()`

```python
set_status(self, status: Literal['running', 'finished', 'failed'])
```

**Description:** Manually set the status of the run

**Parameters:**
- `status`: The status to set

## Method: `write_result()`

```python
write_result(self, **kwargs)
```

**Description:** Log the results of the run to the table, then disable the logger. This means that the logger will be read-only
after this operation. If you run multiple iterations, consider writing the results only once all the runs are
finished. You can aggregate the different metrics before passing them.

**Parameters:**
- `kwargs`: The metrics to save

