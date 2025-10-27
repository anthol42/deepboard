# TODO
Bugs:
- [X] Possibility to change the port in gui and listening adress
- [X] Fix that we can't set hyperparameters to NULL (NOT NULL constraint)
- [X] When value is 0.00005, it is rounded to 0.0001 in GUI. Fix this
- [X] Close cursor as soon as possible to avoid 'database is locked' errors
- [X] It prints the fragment when returned in the GUI

Next version
- [X] Add a major version number in the database to avoid running a database with a wrong version
- [X] Make cli and config parameters optional when creating a new run
- [X] Make the config within the db, not as file next to it
- [ ] Possibility to edit Notes (New field, similar to comments, but editable)
- [ ] See comments and notes in Info table. There we can edit notes
- [ ] In compare tab, add a - Notes in the legend after the run ID for easier interpretation
- [ ] monospace font and wrap in CLI section
- [ ] Add a default theme for tables customizable in the theme file (Like jupyter notebooks)
- [ ] Quick filter in table to quickly filter runs
- [ ] Add possibility to add tags to runs
- [ ] Add possibility to color run rows
- [ ] Improve the UI for figures / images / fragments to wrapt them in a card per reported step, with the epoch, step and rep as the footer of the card (small text)
- [ ] For figures / images / fragments, add a filter option by epochs, reps and tags (Can tag fragments when reporting them)
- [ ] Improve the image viewer with zooming and panning
- [ ] Add a full screen mode for single run view



Next next version
- [ ] Match tensorboard basic features
