from typing import *
from datetime import datetime, timedelta
from fasthtml.common import *
from markupsafe import Markup
from fasthtml.xtend import Textarea
from ....components import AutoCompleteInput



def CopyToClipboard(text: str, cls):
    return Div(
        Span(
            I(cls=f'fas fa-copy copy-icon default-icon {cls}'),
            I(cls=f'fas fa-check copy-icon check-icon {cls}'),
            cls='copy-icon-container',
        ),
        Span(text, cls='copy-text' + ' ' + cls),
        onclick='copyToClipboard(this)',
        cls='copy-container'
    )

def Status(runID: int, status: Literal["running", "finished", "failed"], swap: bool = False):
    swap_oob = dict(swap_oob="true") if swap else {}
    return Select(
            Option("Running", value="running", selected=status == "running", cls="run-status-option running"),
            Option("Finished", value="finished", selected=status == "finished", cls="run-status-option finished"),
            Option("Failed", value="failed", selected=status == "failed", cls="run-status-option failed"),
            id=f"runstatus-select",
            name="run_status",
            hx_get=f"/runinfo/change_status?runID={runID}",
            hx_target="#runstatus-select",
            hx_trigger="change",
            hx_swap="outerHTML",
            hx_params="*",
            **swap_oob,
            cls="run-status-select" + " " + status,
        )

def DiffView(diff: Optional[str]):
    return Div(
        H2("Diff"),
            Div(
                Pre(Markup(diff), cls='raw-file-view'),
                cls="file-view",
            )
        )


def InfoView(runID: int):
    from __main__ import rTable
    # Cli
    row = rTable.fetch_experiment(runID)
    # RunID, Exp name, cfg, cfg hash, cli, command, comment, start, status, commit, diff
    start: datetime = datetime.fromisoformat(row['start'])
    status = row["status"]
    commit = row["commit_hash"]
    diff = row["diff"]
    tag = row["tag"]
    return (Table(
            Tr(
                Td(H3("Start time", cls="info-label")),
                Td(H3(start.strftime("%Y-%m-%d %H:%M:%S"), cls="info-value")),
            ),
            Tr(
                Td(H3("Status", cls="info-label")),
                Td(Status(runID, status), cls="align-right"),
            ),
            Tr(
                Td(H3("Tag", cls="info-label")),
                Td(AutoCompleteInput('run-tag-input', placeholder="Add tag", value=tag or ""), cls="align-right"),
            ),
            Tr(
                Td(H3("Commit", cls="info-label")),
                Td(CopyToClipboard(commit, cls="info-value"), cls="align-right"),
            ),
            Tr(
                Td(Div(
                    H3("Notes", cls="info-label", style="margin-bottom: 1em;"),
                    Textarea(row["note"] if row["note"] else "",
                             id="run-note-textarea",
                             name="note",
                             placeholder="Add notes for the run here...",
                             hx_post=f"/runinfo/update_note?runID={runID}",
                             hx_trigger="input changed delay:1s, focusout",
                             hx_swap="none",
                             cls="run-note-textarea",
                             rows=7,
                )), colspan=2)
            ),
            cls="info-table",
        ),
        DiffView(diff))



# Routes
def build_info_routes(rt):
    rt("/runinfo/change_status")(change_status)
    rt("/runinfo/update_note")(update_note)
    rt('/autocomplete/tags')(autocomplete_tags)

def update_note(session, runID: int, note: str):
    from __main__ import rTable
    socket = rTable.load_run(runID)
    socket.update_note(note)

def change_status(session, runID: int, run_status: str):
    from __main__ import rTable
    socket = rTable.load_run(runID)
    socket.set_status(run_status)
    return Status(runID, run_status, swap=True)

def autocomplete_tags(session, id: str, placeholder: str, search: str, eventType: str, eventKey: str = ""):
    from __main__ import rTable
    tags = rTable.active_tags
    runID = session.get("datagrid", {}).get("selected-rows", [""])[-1]
    if eventType =="keyup" and eventKey == "Enter":
        runsocket = rTable.load_run(runID)
        runsocket.update_tag(search)
        return AutoCompleteInput(id, suggestions=[], value=search, placeholder=placeholder, oob=True)

    match eventType:
        case "clicked":
            runsocket = rTable.load_run(runID)
            runsocket.update_tag(search)
            return AutoCompleteInput(id, suggestions=[], value=search, placeholder=placeholder, oob=True)
        case "keyup" | "focus":
            suggestions = [tag for tag in tags if search.lower() in tag.lower()]
            return AutoCompleteInput(id, suggestions=suggestions, placeholder=placeholder, return_suggestions=True)
        case "blur":
            tag = rTable.load_run(runID).tag
            return AutoCompleteInput(id, suggestions=[], value=tag, placeholder=placeholder, oob=True)
        case _:
            suggestions = [tag for tag in tags if search.lower() in tag.lower()]
            return AutoCompleteInput(id, suggestions=suggestions, placeholder=placeholder, return_suggestions=True),