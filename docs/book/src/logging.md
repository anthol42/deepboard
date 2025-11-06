# Logging

With the result table, we can also log information during runs. For example, we can log the loss and accuracy at each 
step or epoch. We can also log images, raw text, and even html artefacts for more flexibility. It even automatically 
detects matplotlib figures and logs them. All of these results can be visualized in the GUI, and are all stored in a 
single file: the result table database.

## Log scalars
You can log scalar values such as loss, accuracy, or any other metric use the `add_scalar` method of the `LogWriter` 
object. Here is an example of logging loss and accuracy at each epoch:

```python
from deepboard.resultTable import ResultTable

rTable = ResultTable("results.db")

# Create a new LogWriter object named run.
run = rTable.new_debug_run("My Experiment")

loss = 1.
accuracy = 0.
for epoch in range(10):
    for step in range(100):
        global_step = epoch * 100 + step
        loss *= 0.9
        accuracy = 1 - loss
        run.add_scalar("Step/loss", loss, step=global_step, epoch=epoch)
    
    run.add_scalar("Train/loss", loss, step=global_step, epoch=epoch)
    run.add_scalar("Train/accuracy", accuracy, step=global_step, epoch=epoch)

run.write_result(accuracy=accuracy)
```

Let's explore the code above. We simulate three epochs and 100 steps per epoch. At each step, we log the loss and
accuracy using the `add_scalar` method. The first argument is the `tag`, which is a string composed of two 
parts separated by a slash. The first part is the category (e.g., "Train"), and the second part is the name of the 
metric. You will see in the GUI that metrics of the same category are grouped together when comparing runs, and 
metrics with the same name, but in different categories are found in the same figure in the single view. The second 
argument is the value to log, and the last two arguments are optional: `step` is the global step number, and `epoch` 
is the current epoch number. If you do not provide the global step, it will be automatically incremented at each call to
`add_scalar` with a specific tag.

## Log artefacts (images, html fragments, text, etc)
You can also log various type of artefacts, which share a similar api. Here, we will make an example where we log an 
image, and a html hello world fragment to show the concept.

```python
from PIL import Image
import numpy as np

...
# Add this in the previous loop

# We create a random image
img = (np.random.randn(256, 256, 3) * 128).astype(np.uint8)
img = Image.fromarray(img)
run.add_image(img, tag="Random Image", step=global_step, epoch=epoch, flush=True)

fragment = "<h1>Hello World</h1><p>This is a html fragment logged from Deepboard.</p>"
run.add_fragment(fragment, tag="Dummy text", step=global_step, epoch=epoch, flush=True)
```
Here, we introduce two new parameters: `tag` and `flush`. The `tag` parameter is optional for these methods, and is used
to categorize artefacts. Adding tags to artefacts allows you to define more precise filters in the GUI. The `flush` 
parameter will be explained later in the "Automatic cache flushing" section.


## Matplotlib figures
When you plot figures using matplotlib, the `LogWriter` object will automatically detect them and log them for you 
in the result table. Here is an example:

```python
import matplotlib.pyplot as plt

...
# Add this in the previous loop

plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Sample Plot")

run.write_results(accuracy=0.98)
```

Figures are detected when a method is called on the `LogWriter` object, such as `add_scalar`, `add_image`, etc. If 
you plot a figure and never call any method after, the figure will not be logged. Fortunately, you can force the 
figures to be detected by calling the `detect_and_log_figures` method. This method support similar parameters as the 
other artefact logging methods, such as `tag`, `step`, `epoch`, and `flush`. 

Example:
```python
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Sample Plot")
run.detect_and_log_figures()
```
> **Tip**:\
> If you want to add a tag to your figures, you can call the `detect_and_log_figures` method with the `tag` parameter 
> right after plotting. This will prevent automatic detection and will assign your tag to the figure.

## Automatic memory flushing
By default, the `LogWriter` object keeps in memory recently logged data, and only writes them to the database once 
in a while. This is done to improve performances. The parameters that controls the number of logged data kept in memory
is determined when creating the new run with the `flush_each` parameter. If you log less than this parameter value, 
you may not see the logged data in the GUI. To tackle this, you can set the `flush` parameter to `True` when logging 
data, which will force flushing everything in memory to the database. As you will write to disk, note that this 
operation is slow, so use it sparingly.

In addition, calling `write_result` method automatically flushes everything in memory to the database. This method 
should always be called at the end of your experiment.

> **Note**:\
> Each run has a state: "running", "finished" or "failed". When creating a new run, its state is set to "running". When 
> you call the `write_result` method, the state is set to "finished". If an exception occurs during your experiment, 
> the state is set to "failed". In order to get the right state, and flushes all the logs, make sure to call the 
> `write_result` method at the end of your experiment.

> **IMPORTANT**:\
> Always call the `write_result` method at the end of your experiment to ensure that all logged data is saved to 
> the database.