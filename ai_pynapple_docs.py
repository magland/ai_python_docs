import click
import os
import json
import openai


pynapple_src_dir = os.environ.get("PYNAPPLE_SRC_DIR", "/home/magland/src/pynapple")


@click.command()
def generate_topics():
    package_name = "pynapple"
    concatenated_docs = _concatenate_documents(
        [pynapple_src_dir + "/docs/api_guide", pynapple_src_dir + "/docs/examples"]
    )
    system_message = f"""
I am going to provide documentation for a software package called {package_name}.
Based on these docs, respond to the user's request.

Here's the documentation:

{concatenated_docs}
"""
    user_message = """
Based on the docs, please provide a list of titles and brief descriptions of 20 how-to guides that could be created.
Please cover a variety of topics to give a good amount of coverage.
Please respond in json format with the following structure:
[{"title": "Example Title", "description": "Example description"}, ...]
"""
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    gpt_model = "gpt-4o"
    if not OPENAI_API_KEY:
        raise Exception("OPENAI_API_KEY environment variable not set.")
    client = openai.Client(
        api_key=OPENAI_API_KEY,
    )
    chat_completion = client.chat.completions.create(
        model=gpt_model, messages=messages  # type: ignore
    )
    resp = chat_completion.choices[0].message.content
    if resp is None:
        raise Exception("Failed to generate response")
    obj = parse_json_from_response(resp)
    if not os.path.exists("output"):
        os.mkdir("output")
    with open("output/topics.json", "w") as f:
        json.dump(obj, f, indent=4)


def extract_topic(title: str, description: str):
    concatenated_docs = _concatenate_documents(
        [pynapple_src_dir + "/docs/api_guide", pynapple_src_dir + "/docs/examples"]
    )
    system_message = f"""
I am going to provide documentation for a software package called pynapple.
Based on these docs, respond to the user's request.

Here's the documentation:

{concatenated_docs}
"""
    user_message = f"""
Based on the docs, please provide a how-to guide for "{title}".
The description is: "{description}".
"""
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    gpt_model = "gpt-4o-mini"
    if not OPENAI_API_KEY:
        raise Exception("OPENAI_API_KEY environment variable not set.")
    client = openai.Client(
        api_key=OPENAI_API_KEY,
    )
    chat_completion = client.chat.completions.create(
        model=gpt_model, messages=messages  # type: ignore
    )
    resp = chat_completion.choices[0].message.content
    if resp is None:
        raise Exception("Failed to generate response")
    return resp


def parse_json_from_response(resp):
    substr = "```json"
    ind1 = resp.find(substr)
    if ind1 < 0:
        return json.loads(resp)
    ind2 = resp.find("```", ind1 + len(substr))
    if ind2 < 0:
        raise Exception("Found start of json but not end")
    json_str = resp[ind1 + len(substr) : ind2].strip()
    return json.loads(json_str)


def _concatenate_documents(dirpaths):
    extensions = [".md", ".py"]
    docs_fnames = []
    for dirpath in dirpaths:
        for fname in os.listdir(dirpath):
            if any([fname.endswith(ext) for ext in extensions]):
                docs_fnames.append(dirpath + "/" + fname)
    print(f"Found {len(docs_fnames)} documents")
    docs = [_read_document(fname) for fname in docs_fnames]
    return "\n\n".join(docs)


def _read_document(fname):
    with open(fname, "r") as f:
        txt = f.read()
    return txt


def create_file_name_from_title(title):
    return title.replace(" ", "_") + ".md"


@click.command()
def generate_guides():
    with open("output/topics.json", "r") as f:
        topics = json.load(f)
    for topic in topics:
        title = topic["title"]
        description = topic["description"]
        print(title)
        guide = extract_topic(title, description)
        guide_file_name = create_file_name_from_title(title)
        with open("output/" + guide_file_name, "w") as f:
            f.write(guide)


@click.group()
def cli():
    pass


cli.add_command(generate_topics)
cli.add_command(generate_guides)

if __name__ == "__main__":
    cli()
