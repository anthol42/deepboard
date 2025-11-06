# Parametrization and Configuration

We said earlier that each non-debug experiment must be unique. By default, the uniqueness is defined by the 
combination of multiple elements:
- The configuration file
- The command line arguments
- The tag
- Comment

## Configuration file and command line arguments

You can provide a configuration file path, and command line arguments passed by the user, when creating a new run. 
Any changes in these two elements are detected, and considered when checking for uniqueness. This means that you can 
run multiple time the same script, but change the configuration file or command line arguments, and the 
`ResultTable` will accept them as different runs.

Example:
```python
from deepboard.resultTable import ResultTable

rTable = ResultTable("experiments.db")
run = rTable.new_run(
    config_path="config.yaml",
    cli=dict(learning_rate=0.001, batch_size=32)
)
```

## Run Tag
You can provide a tag when creating a new run. The tag can be any string. I recommend using tags to separate between 
different sub-experiments. Tags are also considered when checking for uniqueness. For example, you can run the same 
experiment with the same configuration file and command line arguments, but with different tags, and the 
`ResultTable` will accept them as different runs. 

## Comment
Finally, you can also provide a comment when creating a new run. The comment can be used to textually describe what 
you changed in this run, in case the `ResultTable` refuse to create a new run because it believes it not unique. 

For example:
```python
run1 = rTable.new_run(
    config_path="config.yaml",
    cli=dict(learning_rate=0.001, batch_size=32)
)
run2 = rTable.new_run(
    config_path="config.yaml",
    cli=dict(learning_rate=0.001, batch_size=32),
    comment="This will run because of the comment"
)
```

In the previous example, even if both run are the same, the second run will be accepted because of the comment. 
However, usually you should add a comment for a run that *is* different, and use it to describe what you changed in 
this run.

## Hyperparameters
You can log hyperparameters that you change between runs to the result table using the `add_hparams` method on the 
`LogWriter` object. You can provide any arguments as key-value pairs, and they will be stored in the database. 

For example:
```python
run = rTable.new_run(
    config_path="config.yaml",
    cli=dict(learning_rate=0.001, batch_size=32)
)
run.add_hparams(learning_rate=0.001, batch_size=32, optimizer="adam")
```

With the previous example, you will see in the GUI that new columns were added to the table with those 
hyperparameters. In addition, a new tab will be created containing all those hyperparameters for easier visualization.
