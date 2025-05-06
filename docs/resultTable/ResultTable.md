# Class: `ResultTable`

**Description:** This class represents all the results. There are a lot of method to interact with the resultTable (the database).

All actions performed by the GUI (DeepBoard) are available by public methods to get a programmatic access.

How to use:

- First, specify a path the result table. If the db was not created, it will be created automatically.

- Then, create a run with all the specific parameters describing the run. A unique run_id will be generated.
Note that each run must be unique. This security allows more reproducible runs. If one run perform better than
the others, you can run the code again with all the parameters in the result table and you should get the same
results.

- If you simply want to test your code, you can create a debug run. It won't create a permanent entry in the
table. You will still be able to see the logged scalars in the GUI with the run_id -1 that is reserved for
debug runs. This run will be overwritten by the next debug run.

- Finally, you can interact with the table with the different available methods.

## Method: `fetch_experiment()`

```python
fetch_experiment(self, run_id: int) -> Dict[str, Any]
```

**Description:** Load the row of an experiment. It will return a dictionary with the keys being the column names and the values
the actual values. Note that this does not perform any other operations than fetch in the database. This means
that it will also show columns that were hidden.

**Parameters:**
- `run_id`: The run id to fetch

**Return:**
- The raw row of an experiment
## Method: `get_file_hash()`

```python
get_file_hash(file_path: str, hash_algo: str = 'sha256') -> str
```

**Description:** Returns the hash of the file at file_path using the specified hashing algorithm.

## Method: `get_hidden_runs()`

```python
get_hidden_runs(self) -> List[int]
```

**Description:** Get the list of all hidden run ids.

**Return:**
- A list of run ids associated to hidden runs.
## Method: `get_results()`

```python
get_results(self, run_id: Optional[int] = None, show_hidden: bool = False) -> Tuple[List[str], List[str], List[List[Any]]]
```

**Description:** This function will build the result table and return it as a list. It will also return the column names and
their unique id. It will not return the columns that were hidden and will format the table to respect the
column order. By default, it does not include hidden runs, but they can be included by setting the show_hidden.
You can also get a single row by passing a run_id to the method.

**Parameters:**
- `run_id`: the run id. If none is specified, it fetches all results
- `show_hidden`: Show hidden runs.

**Return:**
- A list of columns names, a list of column ids and a list of rows
## Method: `hide_column()`

```python
hide_column(self, column: str)
```

**Description:** Hide a column in the result table.

**Parameters:**
- `column`: The column name to hide.

## Method: `hide_run()`

```python
hide_run(self, run_id: int)
```

**Description:** Instead of deleting runs and lose information, you can hide it. It will not be visible in the default view of
the result Table, however, it can be unhidden if it was a mistake.

**Parameters:**
- `run_id`: The run id to hide

## Method: `load_config()`

```python
load_config(self, run_id: int) -> str
```

**Description:** Load the configuration file of a given run id

**Parameters:**
- `run_id`: The run id

**Return:**
- The path to the configuration file
## Method: `load_run()`

```python
load_run(self, run_id) -> deepboard.resultTable.logwritter.LogWriter
```

**Description:** Load a specific run's LogWriter in read-only mode.

**Parameters:**
- `run_id`: The run id

**Return:**
- The logWriter bound to the run
## Method: `new_debug_run()`

```python
new_debug_run(self, experiment_name: str, config_path: Union[str, pathlib._local.PurePath], cli: dict, comment: Optional[str] = None, flush_each: int = 10, keep_each: int = 1) -> deepboard.resultTable.logwritter.LogWriter
```

**Description:** Create a new DEBUG socket to log the results. The results will be entered in the result table, but as the runID -1.
This means that everytime you run the same code, it will overwrite the previous one. This is useful to avoid
adding too many rows to the table when testing the code or debugging.

Note:
    It will not log the git diff or git hash






log every step to save space and speed up the process. This parameter controls every how many step we store the
log. 1 means we save at every steps. 10 would mean that we drop 9 steps to save 1.

**Parameters:**
- `experiment_name`: The name of the current experiment
- `config_path`: The path to the configuration path
- `cli`: The cli arguments
- `comment`: The comment, if any
- `flush_each`: Every how many logs does the logger save them to the database?
- `keep_each`: If the training has a lot of steps, it might be preferable to not

**Return:**
- The log writer
## Method: `new_run()`

```python
new_run(self, experiment_name: str, config_path: Union[str, pathlib._local.PurePath], cli: dict, comment: Optional[str] = None, flush_each: int = 10, keep_each: int = 1) -> deepboard.resultTable.logwritter.LogWriter
```

**Description:** Create a new logwritter object bound to a run entry in the table. Think of it as a socket.






log every step to save space and speed up the process. This parameter controls every how many step we store the
log. 1 means we save at every steps. 10 would mean that we drop 9 steps to save 1.

**Parameters:**
- `experiment_name`: The name of the current experiment
- `config_path`: The path to the configuration path
- `cli`: The cli arguments
- `comment`: The comment, if any
- `flush_each`: Every how many logs does the logger save them to the database?
- `keep_each`: If the training has a lot of steps, it might be preferable to not

**Return:**
- The log writer
## Method: `set_column_alias()`

```python
set_column_alias(self, columns: Dict[str, str])
```

**Description:** Set the alias of the column in the result table.

**Parameters:**
- `columns`: A dict of column name and their alias. The alias is the name displayed in the table.

## Method: `set_column_order()`

```python
set_column_order(self, columns: Dict[str, Optional[int]])
```

**Description:** Set the order of the column in the result table. If order is None, it will be set to NULL

If the order is None, it will be set to NULL and be hidden

**Parameters:**
- `columns`: A dict of column name and their order. The order is the index of the column in the table.

## Method: `show_column()`

```python
show_column(self, column: str, order: int = -1)
```

**Description:** Show a column in the result table.
If order is -1, it will be set to the last column.

## Method: `show_run()`

```python
show_run(self, run_id: int)
```

**Description:** This method unhide a run that has been hidden. It undo the operation performed by `hide_run`.

**Parameters:**
- `run_id`: The run id to show

## Method: `to_pd()`

```python
to_pd(self, get_hidden: bool = False) -> pandas.core.frame.DataFrame
```

**Description:** Export the table to a pandas dataframe.

**Parameters:**
- `get_hidden`: If True, it will include the hidden runs.

**Return:**
- The table as a pandas dataframe.
