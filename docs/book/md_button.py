import json
import sys

def _recursive_add_md(section):
    if 'Chapter' in section:
        content = section["Chapter"]['content']
        hidden_div = f'<script type="text/markdown" class="md-content" style="display:none;">{content}</script>'
        section["Chapter"]['content'] += '\n\n' + hidden_div
        if "sub_items" in section["Chapter"]:
            for sub_section in section["Chapter"]["sub_items"]:
                _recursive_add_md(sub_section)


if __name__ == '__main__':
    if len(sys.argv) > 1: # we check if we received any argument
        if sys.argv[1] == "supports":
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    # load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)
    # Now, for each page, we hide at the end the raw markdown content
    for section in book['sections']:
        _recursive_add_md(section)
    # we are done with the book's modification, we can just print it to stdout,
    print(json.dumps(book))