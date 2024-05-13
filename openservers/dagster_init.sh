#!/bin/bash

if [ -z "$DAGSTER_PACKAGE_NAME" ]; then
    echo "Missing dagster project definition environmental variable for DAGSTER_PACKAGE_NAME"
	git clone https://github.com/dagster-io/dagster-quickstart && cd dagster-quickstart && pip install -e ".[dev]"
fi
dagster dev --port=$1