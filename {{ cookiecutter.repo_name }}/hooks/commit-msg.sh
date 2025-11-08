#!/bin/sh
msg=$(cat "$1")

# Require keyword
if ! echo "$msg" | grep -Eq "^(feat|fix|docs|chore|refactor|test):"; then
  echo "❌ Commit message must start with one of: feat|fix|docs|chore|refactor|test"
  exit 1
fi

# Enforce title length
title=$(echo "$msg" | head -n 1)
if [ ${#title} -gt 60 ]; then
  echo "❌ Commit title must be <= 60 characters."
  exit 1
fi
# os.chmod(".git/hooks/commit-msg", 0o755)