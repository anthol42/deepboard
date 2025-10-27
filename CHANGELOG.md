## 0.3.0
### New features
- Now can change the port and listening address of the GUI server
- Now can log hyperparameters with NULL values
### Fixed bugs

## 0.2.3
- Fix a bug when a run had failed, we couldn't re-run it.
## 0.2.2
- Fix a bug when the scalar logs where nan, it was crashing.
## 0.2.1
- Images now display in Pypi
- Copy icon now looks better (add a class that had width=100% and wasn't supposed to)
## 0.2.0
### Bug Fixes
- Table now support inf and NaN values: They are displayed as 'inf' and 'NaN' in the table
- When a row is selected in the session, it will not crash if the row does not exist anymore
### New Features
- You can now disable the result socket: Useful when optimizing with optuna
- Added an option to display charts with a log scale in the GUI
- When a tab has nothing (image, plot, text, scalars, etc), it will not be displayed in the GUI
- CLI command run to launch the script is now automatically logged
- Now can log images and has a tab in the GUI
- Now can log matplotlib plots and has a tab in the GUI (Automatically or Manually)
- Now can log text and has a tab in the GUI
- Now can log HTML fragments and has a tab in the GUI
- Possibility to install only the ResultTable (pip install deepboard) or with the GUI (pip install deepboard[gui])
## 0.1.0
- Fullscreen mode: Now can visualize the table in full screen mode with the 'F' keyboard shortcut
- New default theme colors: primary is green
- Fix rounding in datatable: If a value is about to be rounded to 0, it is converted to scientific notation
## 0.0.1
- Fix not able to load theme at initial startup
- Fix duration charts: Now will be the good duration from start
## 0.0.0
- Initial release