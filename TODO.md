# TODO
Bugs:
- [X] Possibility to change the port in gui and listening adress
- [X] Fix that we can't set hyperparameters to NULL (NOT NULL constraint)
- [X] When value is 0.00005, it is rounded to 0.0001 in GUI. Fix this
- [X] Close cursor as soon as possible to avoid 'database is locked' errors
- [X] It prints the fragment when returned in the GUI
- [X] When multiple tab in the side panel, when clicking a tab, the horizontal scroll is reset, which shouldn't happen. The scroll position should be maintained.
- [X] Fix bug when coloring rows with a filter. (Does not color the good row)
- [X] Auto update result table when updating tag
- [X] Compare page: Cannot hide lines
- [X] Hidden lines do not have style
- [X] Header columns are not frozen in the result table

Next version
- [X] Add a major version number in the database to avoid running a database with a wrong version
- [X] Make cli and config parameters optional when creating a new run
- [X] Make the config within the db, not as file next to it
- [X] Hidden runs are considered 'yanked', and not considered when checking for duplicated runs.
- [X] Possibility to edit Notes (New field, similar to comments, but editable)
- [X] See comments and notes in Info table. There we can edit notes
- [X] In compare tab, add a - Notes in the legend after the run ID for easier interpretation
- [X] monospace font and wrap in CLI section
- [X] Add a default theme for tables customizable in the theme file (Like jupyter notebooks)
- [X] Quick filter in table to quickly filter runs
- [X] Add possibility to add tag to runs
- [X] Add possibility to color run rows
- [X] Unique columns combination are to be configured at table creation
- [X] Improve the UI for figures / images / fragments to wrapt them in a card per reported step, with the epoch, step,  rep and tag as the footer of the card (small text)
- [X] For figures / images / fragments, add a filter option by epochs, reps and tags
- [X] Improve the image viewer with zooming and panning
- [ ] Add a way to save models (Save artefacts) --> Aborted, do not know how to do it properly yet
- [X] Standardize the api (set/update) (get/computed property): One expensive to fetch while the other inexpensive
- [X] Add a way to download graph data as csv

Next next version
- [ ] Full code refactor: Refactor code structure and how components are defined (their logic) and interact, to make the project more scalable and maintainable.
- [ ] Add tests: Unit tests and integration tests to ensure code quality and prevent regressions
- [ ] Match tensorboard basic features
- [ ] Add a full screen mode for single run view
