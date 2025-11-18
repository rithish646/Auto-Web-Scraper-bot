
#!/usr/bin/env bash
# Simple entrypoint to run the CLI inside the container
if [ "$1" = "run" ]; then
  shift
  python -m src.cli run "$@"
elif [ "$1" = "scheduler" ]; then
  python -m src.scheduler
else
  exec "${@}"
fi
