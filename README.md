# Tweetstorm #

Tweetstorm it's a way to bypass Twitter's blessed 140 chars limit. It allows you to break down a larger corpus of text into tweets and post them in quick succession, forming a cohesive whole.

### Dependencies

- [Python 3.6](https://www.python.org/downloads/)

### Setup

* virtualenv -p python3 .venv
* source .venv/bin/activate
* pip install .

### Run the tests

* source .venv/bin/activate
* make requirements-dev
* make test


### Usage

Example:
```shell
tweetstorm -t "A common trope in discussions about startups & venture capital is a potential misalingnment of incentives between startup team. I don't think this percevied missalignment actually exists in most.maybe all casses -- and I Want to explain why."

# Return
1/2 A common trope in discussions about startups & venture capital is a potential misalingnment of incentives between startup team. I don't 
2/2 think this percevied missalignment actually exists in most.maybe all casses -- and I Want to explain why.
```