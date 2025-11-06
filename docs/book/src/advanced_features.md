# Advanced Features
TODO

## Multiple run repetitions
TODO

## Commit flags
You can prevent the `ResultTable` from accepting a new run if there is uncommitted changes in the git repository. You 
can do this by setting the `nocommit_action` when loading the `ResultTable`. The possible values are:
- `NoCommitAction.NOP`: Ignore, do nothing
- `NoCommitAction.WARN`: Print a warning message if there are uncommitted changes (default behavior)
- `NoCommitAction.RAISE`: Raise an error and prevent the new run from being added

## Custom unique columns
TODO
