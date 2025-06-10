import inspect
import os
from pathlib import Path
import re
from enum import Enum

# Specify class and function names to include
whitelist = [
    "ResultTable",
    "NoCommitAction",
    "LogWriter"
]
module_whitelist = [
    "deepboard.resultTable.resultTable"
]

def extract_params_and_clean_docstring(docstring):
    """
    This function extracts parameters from the docstring and returns:
    - the cleaned docstring (without parameter definitions),
    - a dictionary with parameter names as keys and their explanations as values.
    """
    # Regex to match the :param param_name: explanation pattern
    param_pattern = r':param ([A-Za-z_][A-Za-z0-9_]*):\s*(.*)'

    # Dictionary to store parameters and their explanations
    params_dict = {}

    # Find all matches
    matches = re.findall(param_pattern, docstring)

    # Extract parameters and their explanations
    for param_name, explanation in matches:
        params_dict[param_name] = explanation.strip()

    # Remove all parameter definitions from the docstring
    cleaned_docstring = re.sub(param_pattern, '', docstring)

    # Clean up any extra spaces or newlines that might remain
    cleaned_docstring = cleaned_docstring.strip()

    return cleaned_docstring, params_dict

def extract_returns_and_clean_docstring(docstring):
    """
    This function extracts returns explanations from the docstring and returns:
    - the cleaned docstring (without parameter definitions),
    - the return explanations as string.
    """
    if ":return:" in docstring:
        idx = docstring.find(":return:")

        exp = docstring[idx:].replace(":return:", "").strip()
        return docstring[:idx].strip(), exp
    else:
        return docstring, None

def extract_docstrings(package_path):
    # Create a markdown file to store the results
    markdown_path = Path("docs/resultTable")
    if not os.path.exists(markdown_path):
        os.makedirs(markdown_path, exist_ok=True)

    # Walk through the package directory
    for root, dirs, files in os.walk(package_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                module_name = file_path.replace('.py', '').replace('/', '.')

                # Import the module dynamically
                module = __import__(module_name, fromlist=[''])
                if module_name not in module_whitelist:
                    continue
                # We do not want to write the file
                # md_file.write(f"## {module_name}\n\n")

                # Extract all classes and functions from the module
                for name, obj in inspect.getmembers(module):
                    if name not in whitelist:
                        continue
                    with open(f"{markdown_path}/{name}.md", 'w') as md_file:
                        # Check if it's a class
                        if inspect.isclass(obj) and issubclass(obj, Enum):
                            md_file.write(f"# Enum: `{name}`\n\n")
                            docstring = inspect.getdoc(obj) or "No documentation available"
                            md_file.write(f"**Description:** {docstring}\n\n")

                            # Extract enum members and their values
                            md_file.write(f"```python\n")
                            for enum_member in obj:
                                md_file.write(f"    {enum_member.name} = {enum_member.value}\n")
                            md_file.write(f"```\n\n")

                        elif inspect.isclass(obj):
                            md_file.write(f"# Class: `{name}`\n\n")
                            docstring = inspect.getdoc(obj) or "No documentation available"
                            md_file.write(f"**Description:** {docstring}\n\n")

                            # Extract methods of the class
                            for method_name, method_obj in inspect.getmembers(obj):
                                if method_name.startswith("_"):
                                    continue
                                if inspect.isfunction(method_obj):
                                    docstring = inspect.getdoc(method_obj) or "No documentation available"
                                    # Extract method signature and parameters
                                    signature = inspect.signature(method_obj)
                                    docstring, parameters = extract_params_and_clean_docstring(docstring)
                                    docstring, return_exp = extract_returns_and_clean_docstring(docstring)

                                    md_file.write(f"## Method: `{method_name}()`\n\n")
                                    md_file.write(
                                        f"```python\n{method_name}{signature}\n```\n\n")
                                    md_file.write(f"**Description:** {docstring}\n\n")

                                    if len(parameters) > 0:
                                        md_file.write("**Parameters:**\n")
                                        for param, explanation in parameters.items():
                                            md_file.write(f"- `{param}`: {explanation}\n")
                                        md_file.write("\n")

                                    if return_exp and return_exp.strip() != "None":
                                        md_file.write("**Return:**\n")
                                        md_file.write(f"- {return_exp}\n")

                        # Check if it's a function (outside of class)
                        elif inspect.isfunction(obj):
                            docstring = inspect.getdoc(obj) or "No documentation available"

                            # Extract function signature and parameters
                            signature = inspect.signature(obj)
                            parameters = signature.parameters

                            md_file.write(f"# Function: `{name}()`\n\n")
                            md_file.write(
                                f"```python\n{name}({', '.join([f'{param}={parameters[param].annotation}' for param in parameters])})\n```\n\n")
                            md_file.write(f"**Description:** {docstring}\n\n")

                            # List the parameters and their types
                            if len(parameters) > 0:
                                md_file.write("**Parameters:**\n")
                                for param, explanation in parameters.items():
                                    md_file.write(f"- `{param}`: {explanation}\n")
                                md_file.write("\n")

    print(f"Docstrings extracted to {markdown_path}")


# Run the script on your package
extract_docstrings('deepboard/resultTable')
