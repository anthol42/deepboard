$(info [make] Current directory: $(CURDIR))
build:
	uv run tools/extract_doc.py
	uv run tools/prep_readme.py
	uv build