```bash
# Basic Navigation and Shortcuts on Gadi

# Now that we have covered some basic login elements, we can look through some commands
# that are required to navigate within Gadi while you submit and monitor jobs.

# If you are new to the Unix environment, try out some of these commands to practice using the system.

# Tip: Use our Linux command cheat sheet when you're stuck.
# For recurring issues, contact the NCI helpdesk or email: help@nci.org.au

# ------------------------------------------------------------------------------

# Commands

# man <cmd> — access the manual for a command
man ls
man pwd

# If no manpage, try:
<program> -h
<program> --help

# ls -l — list directory contents in long format
ls -l

# pwd — present working directory
pwd

# cd <path> — change directory
cd /g/data/your_project/

# mkdir <pathname> — create a new directory
mkdir my_new_folder

# cp — copy files
cp /path/to/source.txt /path/to/destination/

# quota -s — check user disk quota
quota -s

# lquota — check project quota
lquota

# rm — remove (delete) a file permanently
rm filename.txt

# ⚠️ Files deleted using `rm` are permanently removed with no prompt.
# Be especially careful in /scratch and /gdata.

# ------------------------------------------------------------------------------

# Keyboard Shortcuts

# Ctrl+C   — Halt the current command
# Ctrl+A   — Move cursor to the beginning of the line
# Ctrl+E   — Move cursor to the end of the line
# Ctrl+K   — Delete from cursor to the end of the line
# Ctrl+Z   — Stop foreground job and place in background
# Ctrl+D   — Log out of the current session (same as `exit`)

# ------------------------------------------------------------------------------

# Looking for More?

# These are just the basics to get you started.
# - Check out the Linux Command Quick Reference Guide
# - Or search online for Linux tutorials and help

# Authors: Yue Sun, Andrew Johnston
# Powered by Atlassian Confluence 9.3.1
# Report issues at: https://opus-1.nci.org.au
