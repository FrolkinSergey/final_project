#!/bin/sh

set -e

host="$1"
shift 2
cmd="$@"

# Wait for the port to become available
until nc -z "$host"; do
  >&2 echo "Waiting for $host to become available..."
  sleep 1
done

>&2 echo "$host is available, executing command: $cmd"
exec $cmd
