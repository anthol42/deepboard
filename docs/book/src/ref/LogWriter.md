# Class: `LogWriter`

**Description:** This class makes an object that is bound to a run row in the result table. This means that everything that is
logged through this object is added into the result table and this object can be used to interact with a specific
run. This object is single use. This means that once the final results are written, the object becomes read-only.

You should not instantiate this class directly, but use the ResultTable class to create it instead.

## Method: `add_fragment()`

```python
add_fragment(self, content: str, step: Optional[int] = None, tag: Optional[str] = None, epoch: Optional[int] = None, flush: bool = False)
```

**Description:** Add a html fragment to the resultTable


scalar steps.

**Parameters:**
- `content`: Must be a string containing valid HTML content.
- `step`: The global step at which the image was generated. If None, the maximum step is taken from all global
- `tag`: A tag describing the fragment.
- `epoch`: The epoch at which the image was generated. If None, no epoch is saved.
- `flush`: If True, flush all data in memory to the database.

## Method: `add_hparams()`

```python
add_hparams(self, param_dict: Optional[dict[str, Any]] = None, **kwargs)
```

**Description:** Add hyperparameters to the result table

**Parameters:**
- `param_dict`: The hyperparameters to add as a dict.
- `kwargs`: The hyperparameters to save

## Method: `add_image()`

```python
add_image(self, image: Union[bytes, PIL.Image.Image], step: Optional[int] = None, tag: Optional[str] = None, epoch: Optional[int] = None, flush: bool = False)
```

**Description:** Add an image to the resultTable


steps.

**Parameters:**
- `image`: Must be png bytes or a PIL Image object.
- `step`: The global step at which the image was generated. If None, the maximum step is taken from all global
- `tag`: A tag describing the image.
- `epoch`: The epoch at which the image was generated. If None, no epoch is saved.
- `flush`: If True, flush all data in memory to the database.

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

## Method: `add_text()`

```python
add_text(self, text: str, step: Optional[int] = None, tag: Optional[str] = None, epoch: Optional[int] = None, flush: bool = False)
```

**Description:** Add a text sample to the resultTable


scalar steps.

**Parameters:**
- `text`: Must be a string
- `step`: The global step at which the image was generated. If None, the maximum step is taken from all global
- `tag`: A tag describing the text.
- `epoch`: The epoch at which the image was generated. If None, no epoch is saved.
- `flush`: If True, flush all data in memory to the database.

## Method: `detect_and_log_figures()`

```python
detect_and_log_figures(self, step: Optional[int] = None, tag: Optional[str] = None, epoch: Optional[int] = None, flush: bool = False)
```

**Description:** Detect matplotlib figures that are currently open and log them to the result table. (Save them as png).

steps.

**Parameters:**
- `step`: The global step at which the image was generated. If None, the maximum step is taken from all global
- `tag`: A tag describing the figures.
- `epoch`: The epoch at which the images were generated. If None, no epoch is saved.
- `flush`: If True, flush all data in memory to the database.

## Method: `get_figures()`

```python
get_figures(self, id: Optional[int] = None, step: Optional[int] = None, tag: Optional[str] = None, epoch: Optional[int] = None, repetition: Optional[int] = None)
```

**Description:** Return all figures logged in the run with the given step, tag and/or epoch.

**Parameters:**
- `id`: The id of the figure to read. If None, all figures are returned.
- `step`: The step at which the figure was generated. If None, all figures are returned.
- `tag`: The tag describing the figures. If None, all tags are returned.
- `epoch`: The epoch at which the figures were generated. If None, all epochs are returned.
- `repetition`: The repetition of the figures. If None, all figures are returned.

## Method: `get_fragment()`

```python
get_fragment(self, id: Optional[int] = None, step: Optional[int] = None, tag: Optional[str] = None, epoch: Optional[int] = None, repetition: Optional[int] = None)
```

**Description:** Return all html fragments logged in the run with the given id, step, tag and/or epoch.

**Parameters:**
- `id`: The id of the html fragment to read
- `step`: The step at which the html fragment was generated. If None, all html fragment are returned.
- `tag`: The tag describing the fragment. If None, all tags are returned.
- `epoch`: The epoch at which the html fragments were generated. If None, all epochs are returned.
- `repetition`: The repetition of the run. If None, all html fragment are returned.

**Return:**
- A list of html fragment
## Method: `get_hparams()`

```python
get_hparams(self) -> Dict[str, Any]
```

**Description:** Get the hyperparameters of the current run

**Return:**
- A dict of hyperparameters
## Method: `get_images()`

```python
get_images(self, id: Optional[int] = None, step: Optional[int] = None, tag: Optional[str] = None, epoch: Optional[int] = None, repetition: Optional[int] = None) -> List[dict]
```

**Description:** Return all images logged in the run with the given step, tag and/or epoch.

**Parameters:**
- `id`: The id of the image to read
- `step`: The step at which the image was generated. If None, all images are returned.
- `tag`: The tag in which the images were generated. If None, all tags are returned.
- `epoch`: The epoch at which the images were generated. If None, all epochs are returned.
- `repetition`: The repetition of the images. If None, all images are returned.

**Return:**
- A list of image bytes
## Method: `get_repetitions()`

```python
get_repetitions(self) -> List[int]
```

**Description:** Get the all the repetitions ids of the current run

**Return:**
- A list of repetitions ids
## Method: `get_scalar()`

```python
get_scalar(self, tag) -> List[deepboard.resultTable.scalar.Scalar]
```

**Description:** Read a scalar from the resultTable with the given tag

**Parameters:**
- `tag`: The tag to read formatted as: 'split/name' or simply 'split'.

**Return:**
- A list of Scalars items
## Method: `get_text()`

```python
get_text(self, id: Optional[int] = None, step: Optional[int] = None, tag: Optional[str] = None, epoch: Optional[int] = None, repetition: Optional[int] = None)
```

**Description:** Return all text samples logged in the run with the given id, step, tag and/or epoch.

**Parameters:**
- `id`: The id of the text sample to read
- `step`: The step at which the text was generated. If None, all text samples are returned.
- `tag`: The tag describing the text. If None, all tags are returned.
- `epoch`: The epoch at which the texts were generated. If None, all epochs are returned.
- `repetition`: The repetition of the run. If None, all text samples are returned.

**Return:**
- A list of text samples
## Method: `new_repetition()`

```python
new_repetition(self)
```

**Description:** Create a new repetition of the current run. This is useful if you want to log multiple repetitions of the same
run. This is a mutating method, meaning that you can call it at the end of the training loop before the next
full training loop is run again.

## Method: `set_color()`

```python
set_color(self, color: Optional[str] = None)
```

**Description:** Set the color of the run

**Parameters:**
- `color`: The color to set (hex format without #, e.g. 'ff0000' for red)

## Method: `set_note()`

```python
set_note(self, note: str)
```

**Description:** Update the note of the run

**Parameters:**
- `note`: The note to set (will overwrite the previous one)

## Method: `set_status()`

```python
set_status(self, status: Literal['running', 'finished', 'failed'])
```

**Description:** Manually set the status of the run

**Parameters:**
- `status`: The status to set

## Method: `set_tag()`

```python
set_tag(self, tag: str)
```

**Description:** Update the tag of the run

**Parameters:**
- `tag`: The tag to set (will overwrite the previous one)

## Method: `write_result()`

```python
write_result(self, **kwargs)
```

**Description:** Log the results of the run to the table, then disable the logger. This means that the logger will be read-only
after this operation. If you run multiple iterations, consider writing the results only once all the runs are
finished. You can aggregate the different metrics before passing them.

**Parameters:**
- `kwargs`: The metrics to save

