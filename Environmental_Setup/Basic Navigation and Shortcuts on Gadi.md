# Basic Navigation and Shortcuts on Gadi

Now that we have covered some basic login elements, we can look through some commands that are required to navigate within Gadi while you submit and monitor jobs.

If you are new to the Unix environment, you can try out some of these commands to practice using the system.

> **Tip:** You can use our **Linux command cheat sheet** when you're stuck. For recurring issues, feel free to contact the **NCI helpdesk** or email us at [help@nci.org.au](mailto:help@nci.org.au).

---

## Commands

### `man <cmd>`
Use `man` followed by a command (e.g., `ls`, `pwd`) to access its manual.  
If no manpage is available, try:
- `<program> -h`
- `<program> --help`

### `ls -l`
Lists the contents of the current directory in a detailed format.

### `pwd`
Displays the **present working directory**, i.e., your current location in the file system.

### `cd <path>`
Use to **change directories**. Navigate through Gadi's file system using paths.

### `mkdir <pathname>`
Creates a new directory. Think of it as creating a new folder.

### `cp`
Copies files.  
Example:
```bash
cp <path/to/target> <path/to/destination>
