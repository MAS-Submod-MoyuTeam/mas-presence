#!/bin/sh

# Builds a package with the submod.
# Usage: $ scripts/build SUBMOD_NAME VERSION

if [ "$#" -lt 2 ]; then echo "Usage: $0 SUBMOD_NAME VERSION"; exit 1; fi

dir="$(dirname "$(CDPATH="" cd -- "$(dirname -- "$0")" && pwd)")"
temp="$(mktemp -d)"

name="$1"
version="$2"
package="$(echo "$name" | tr "[:upper:]" "[:lower:]" | tr "[:blank:]" "-")"

mkdir -p "$temp/game/Submods"
mkdir -p "$temp/game/Submods/$name/config"

cp -r "$dir/mod" "$temp/game/Submods/$name"
cp -r "$dir/config" "$temp/game/Submods/$name/config/maintained"
cp -r "$dir/lib" "$temp/game/Submods/$name/lib"

rm "$temp/game/Submods/$name/lib/README.txt"

(cd "$temp" || exit 1; find game | zip -9@q "$dir/$package-$version.zip" && rm -rf "$temp")