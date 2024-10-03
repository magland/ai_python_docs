# ai_pynapple_docs

The goal is to be able to efficiently load knowledge about using Pynapple into AI chatbots.

Uses the [Pynapple documentation](https://github.com/pynapple-org/pynapple/tree/main/docs) to create AI-generated how-to guides for using Pynapple on a wide range of topics.

Also creates an index file topics.json that contains the list of topics generated.

A chatbot can use this in two passes. First it figures out which guide(s) it needs to load into context based on the prompt. Then it loads the guide(s) and uses them to respond to the prompt.

Whereas the full concatenated documentation for Pynapple is around 33k tokens, the individual guides are less than 1k tokens each.

## Usage

First, clone pynapple and set the PYNAPPLE_SRC_DIR environment variable to the path of the pynapple source directory.

Then run:

```bash
# Generate the topics.json file
python ai_pynapple_docs.py generate-topics

# Generate the guides
python ai_pynapple_docs.py generate-guides
```


