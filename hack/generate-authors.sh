#!/bin/bash

# The root of the Git repository
cd "$(git rev-parse --show-toplevel)" || exit 1

> AUTHORS

# Use Git log to extract author names and email addresses
git log --format='%aN <%aE>' | sort -u
