from fasthtml.common import *
from starlette.responses import Response

def _get_images_groups(socket):
    images = socket.read_images()

    index = list({(img["step"], img["epoch"], img["run_rep"], img["split"]) for img in images})

    splits = list({elem[3] for elem in index})

    # Package images
    images_groups = {}
    for key in index:
        cropped_key = key[:-1]  # Remove split
        if cropped_key not in images_groups:
            images_groups[cropped_key] = {split: [] for split in splits}

    for img in images:
        key = img["step"], img["epoch"], img["run_rep"]
        split = img["split"]
        images_groups[key][split].append(img["id"])

    # Sort image groups by step, and run_rep
    return dict(sorted(images_groups.items(), key=lambda x: (x[0][0], x[0][2])))

def SplitSelector(runID, available_splits: List[str], selected: str, step: int, epoch: int, run_rep: int, swap: bool = False):
    swap_oob = dict(swap_oob="true") if swap else {}
    return Select(
        *[
            Option(split.capitalize(), value=split, selected=selected == split, cls="artefact-split-option")
            for split in available_splits
        ],
        id=f"images-split-select",
        name="split_select",
        hx_get=f"/images/change_split?runID={runID}&step={step}&epoch={epoch}&run_rep={run_rep}",
        hx_target=f"#image-card-{step}-{epoch}-{run_rep}",
        hx_trigger="change",
        hx_swap="outerHTML",
        hx_params="*",
        **swap_oob,
        cls="artefact-split-select",
    )

def StatLine(label: str, value: str):
    return Span(
        H3(f"{label}: ", style="font-size: 1em; margin: 0.1em; margin-right: 0.5em; font-weight: bold;"),
        H3(value, style="font-size: 1em; margin: 0.1em; font-weight: normal;"),
        cls="expand"
    )

def ImageComponent(image_id: int):
    """
    Create a single image component with a specific style.
    :param image: PIL Image object.
    :return: Div containing the image.
    """
    return Div(
        Img(src=f"/images/id={image_id}", alt="Image"),
        cls="image",
    )

def ImageGroup(images_id: List[int]):
    """
    Create a group of images in a flex container that adapts to the number of images.
    :param images: List of PIL Image objects.
    :return: Div containing the images.
    """
    return Div(
        *[ImageComponent(image_id) for image_id in images_id],
        cls="artefact-group-container",
    )


def ImageCard(runID: int, step: int, epoch: Optional[int], run_rep: int, selected: Optional[str] = None):
    from __main__ import rTable

    socket = rTable.load_run(runID)
    data = _get_images_groups(socket)

    if (step, epoch, run_rep) not in data:
        avail_splits = []
        images = []
    else:
        images_splits = data[(step, epoch, run_rep)]
        avail_splits = list(images_splits.keys())
        avail_splits.sort()
        if selected is None:
            selected = avail_splits[0]
        images = images_splits[selected]

    return Div(
        Div(
            SplitSelector(runID, avail_splits, selected=selected, step=step, epoch=epoch, run_rep=run_rep),
            Div(
                StatLine("Step", str(step)),
                StatLine("Epoch", str(epoch) if epoch is not None else "N/A"),
                StatLine("Run Repetition", str(run_rep)),
                cls="artefact-stats-column"
            ),
            cls="artefact-card-header",
        ),
        ImageGroup(images),
        id=f"image-card-{step}-{epoch}-{run_rep}",
        cls="artefact-card",
    )

def ImageTab(session, runID, swap: bool = False):
    from __main__ import rTable
    socket = rTable.load_run(runID)

    images_groups = _get_images_groups(socket)
    return Div(
        *[
            ImageCard(runID, step, epoch, run_rep)
            for step, epoch, run_rep in images_groups.keys()
        ],
        style="display; flex; width: 40vw; flex-direction: column; align-items: center; justify-content: center;",
        id="images-tab",
        hx_swap_oob="true" if swap else None,
    )


def images_enable(runID):
    """
    Check if some scalars are logged and available for the runID. If not, we consider disable it.
    :param runID: The runID to check.
    :return: True if scalars are available, False otherwise.
    """
    from __main__ import rTable
    socket = rTable.load_run(runID)
    return len(socket.read_images()) > 0

# routes
def build_images_routes(rt):
    rt("/images/change_split")(change_split)
    rt("/images/id={image_id}")(load_image)


def change_split(session, runID: int, step: int, epoch: Optional[int], run_rep: int, split_select: str):
    """
    Change the split for the images.
    :param session: The session object.
    :param step: The step of the images.
    :param epoch: The epoch of the images.
    :param run_rep: The run repetition of the images.
    :param split: The split to change to.
    :return: The updated image card HTML.
    """
    return ImageCard(
        runID,
        step,
        epoch,
        run_rep,
        selected=split_select,
    )

def load_image(image_id: int):
    from __main__ import rTable
    img = rTable.get_image_by_id(image_id)
    if img is None:
        return Response(f"Image not found with id: {image_id}:(", status_code=404)
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    return Response(
        content=img_buffer.getvalue(),
        media_type="image/png"
    )
