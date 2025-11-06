# Getting Started

First, install the package with the GUI with pip:
```shell
pip install deepboard[full]
```

The deepboard package is divided into two main components: the experiment tracking one called ResultTable, and the GUI 
application. You will interact with the ResultTable api in your code to log your experiments, and then use the GUI to 
visualize and analyze them.

## Creating a new experiment
```python
from deepboard.resultTable import ResultTable

# Step 1: Create / load the result table
rTable = ResultTable()

# Step 2: Create a new run
run = rTable.new_run("My Experiment")

# Step 3: Write the final results
run.write_result(accuracy=0.98, loss= 0.0257)
```

Here, we first create a new ResultTable instance. If no database exist at the specified path, a new result table, a 
database,  will be created. Then, we create a new entry in the table with the new run command. We can run our 
experiment, then write the final results to the result table. By default, it creates a file named `result_table.db`. 
You can visualize the results in the GUI by running and opening in your web browser.
```shell
deepboard result_table.db
```

## Experiment uniqueness and debug mode
Note that if you try to run the previous script again, it will raise an error saying that the experiment has already 
been run with runID 1. This is because each experiment must be unique in the result table. To avoid getting this 
constraint, you can run in debug mode, which will give the same runID (-1) to every run, and each run will overwrite 
the previous one. You can simply call the `new_debug_run` method instead of `new_run`, and the rest of the api 
remains the same, so we can use the same code as before.

```python
run = rTable.new_debug_run("My Experiment")
```

## The Run ID
As every run must be unique, each run is given a unique id called the RunID. You can retrieve this id by accessing the 
`run_id` attribute of the `LogWriter` object (the run variable in the previous examples). Since this id is unique, you 
can use it for whatever you want, for example, you could save checkpoints to a directory, where each checkpoint file 
or directory is named with the corresponding RunID.

---
> **Note:**\
> When an experiment fails (an exception is raised), the ResultTable will detect it, and the run won't be considered 
> when checking uniqueness. This means that you can re-run failed experiments without changing anything, and the run will 
> be accepted as a new unique experiment.

It is useful to log final results of experiments to compare them later, but we often want to log intermediate results
during training. This topic is explored in the next chapter.

