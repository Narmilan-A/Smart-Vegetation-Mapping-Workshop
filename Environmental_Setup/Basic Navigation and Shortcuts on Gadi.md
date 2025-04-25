# Gadi Basic Navigation and Shortcuts Guide

This guide introduces basic navigation commands and keyboard shortcuts for users of the Gadi supercomputing environment at NCI.

---

**🔹 Basic Navigation Commands**

- **`man <cmd>`**  
  View the manual page for a command. For example, `man ls` or `man pwd`.  
  If no manpage exists, try `<program> -h` or `<program> --help`.

- **`ls -l`**  
  List contents of the current directory in long format.

- **`pwd`**  
  Print the current working directory path.

- **`cd <path>`**  
  Change to the specified directory.

- **`mkdir <pathname>`**  
  Create a new directory. Equivalent to creating a new folder.

- **`cp <source> <destination>`**  
  Copy files from source to destination.  
  Example: `cp /home/user/file.txt /g/data/project/`  
  If destination is a directory, the file is placed inside it.

- **`quota -s`**  
  Show your user disk quota, including usage and limit.

- **`lquota`**  
  Show quota information for the project you're associated with.

- **`rm <filename>`**  
  Permanently delete a file.  
  ⚠️ No confirmation is given — use with caution, especially on `/scratch` and `/gdata`.

---

**🔹 Keyboard Shortcuts**

- **`Ctrl+C`**  
  Cancel or interrupt the currently running command.

- **`Ctrl+A`**  
  Move cursor to the beginning of the command line.

- **`Ctrl+E`**  
  Move cursor to the end of the command line.

- **`Ctrl+K`**  
  Delete from the cursor position to the end of the line.

- **`Ctrl+Z`**  
  Suspend the foreground process and put it in the background (stopped).

- **`Ctrl+D`**  
  Log out of the session (same as `exit`).

---

**🔹 Tips and Additional Resources**

- These commands are ideal for beginners in the Unix/Linux environment.
- Use NCI's [Linux Command Quick Reference Guide](https://opus.nci.org.au/display/Help/Linux+Command+Quick+Reference) for more detailed usage.
- Explore the [Gadi User Guide](https://opus.nci.org.au/display/Help/Gadi+User+Guide) for comprehensive system documentation.
- For persistent issues, contact the **NCI Helpdesk** at 📧 **help@nci.org.au**

---

**Authors:** Yue Sun, Andrew Johnston  
**Source:** [Opus - NCI Confluence](https://opus.nci.org.au)
