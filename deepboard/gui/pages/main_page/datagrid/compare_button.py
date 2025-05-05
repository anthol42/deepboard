from typing import *
from fasthtml.common import *

def CompareButton(session, swap: bool = False):
    show = "datagrid" in session and "selected-rows" in session["datagrid"] and len(session["datagrid"]["selected-rows"]) > 1
    run_ids = session["datagrid"].get("selected-rows") or []
    url = f"/compare?run_ids={','.join([str(i) for i in run_ids])}"
    return Div(
        Button(
            "Compare",
            cls="compare-button",
            style="display: block;" if show else "display: none;",
            onclick=f"window.open('{url}', '_blank')",
            hx_get="/reset",
            hx_target="#container",
        ),
        cls="compare-button-container",
        id="compare-button-container",
        hx_swap_oob="true" if swap else "false",
    )