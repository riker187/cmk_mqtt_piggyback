#!/bin/bash
set -euo pipefail

# Build MKP package using the manifest in this repository.
#
# The mkp tool expects the project files to live beneath the given
# directory. By default it searches the Checkmk site directories, which
# would cause a "Cannot stat" error if the files are only present in the
# repository. We therefore explicitly point mkp to the current
# repository root so that the files from the agents/, checks/ and web/
# folders are found correctly.
#
# Depending on the Checkmk version, the -d option may have to be supplied
# in different ways or not at all. We try the supported variants in order,
# stopping once one succeeds.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if mkp package "$SCRIPT_DIR/manifest"; then
    :
elif mkp package -d "$SCRIPT_DIR" "$SCRIPT_DIR/manifest"; then
    :
else
    mkp -d "$SCRIPT_DIR" package "$SCRIPT_DIR/manifest"
fi
