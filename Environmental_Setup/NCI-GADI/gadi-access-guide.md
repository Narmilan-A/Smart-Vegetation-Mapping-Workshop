
# Accessing Gadi HPC System

Access to Gadi is via SSH to `gadi.nci.org.au`. This provides a Unix shell on one of the Gadi login nodes.

⚠️ For security reasons, avoid setting up passwordless SSH to Gadi. It is more secure to enter your password at each login or use specialized SSH secure agents.

## Connecting from Linux/Mac/Unix

1. Open a Terminal application.
2. Use the following command (replace `abc123` with your NCI username):

   ```bash
   ssh abc123@gadi.nci.org.au
   ```

3. Enter your password when prompted.

If you've forgotten your password, you can reset it via Mancini:  
🔗 https://my.nci.org.au/mancini/reset/password/

## Copying Files

To copy files **to** Gadi (use `gadi-dm.nci.org.au`):

```bash
scp /path/to/local/file abc123@gadi-dm.nci.org.au:/path/to/destination/on/gadi
```

To copy files **from** Gadi:

```bash
scp abc123@gadi-dm.nci.org.au:/path/to/file/on/gadi /path/to/local/destination
```

## Login with X11 (X-Windows)

To allow X11 windows from Gadi, forward X11 by using the `-Y` option:

```bash
ssh -Y abc123@gadi.nci.org.au
```

💡 If you're on macOS 10.8 or later, install XQuartz first:  
🔗 https://www.xquartz.org

## Connecting from Windows

The hostname for SSH connections is `gadi.nci.org.au`. Your username is provided when your NCI account is created. You can check it via:  
🔗 https://my.nci.org.au/

Since Windows does not provide a built-in SSH client, use one of the following:

- MobaXterm: https://mobaxterm.mobatek.net
- PuTTY: http://www.chiark.greenend.org.uk/~sgtatham/putty/

### Connecting with MobaXterm:

1. Open MobaXterm.
2. Click on `Session` tab or `Sessions` menu.
3. Select SSH.
4. Set `Remote host` to `gadi.nci.org.au`.
5. Set `Specify username` to your NCI username.
6. Click OK to start session and log in.

## Copying Files on Windows

Use `gadi-dm.nci.org.au` for file transfers. Recommended applications:

- MobaXterm
- PuTTY's PSCP or PSFTP
- FileZilla: https://filezilla-project.org
- WinSCP: https://winscp.net

### With MobaXterm:

After logging in, simply drag and drop files/folders to or from Gadi and your local computer using the side file panel.

## X11 (X-Windows) Access on Windows

To enable X11 forwarding from Gadi to your Windows machine, install one of the following:

- MobaXterm: https://mobaxterm.mobatek.net
- Cygwin: https://cygwin.com
- Xming: http://www.straightrunning.com/XmingNotes/

## Notes

- Always use `gadi-dm.nci.org.au` for file transfers — not the login node.
- Do not configure passwordless SSH for security reasons.
- For help, visit the NCI Helpdesk:  
  🔗 https://opus.nci.org.au/display/Help/Getting+Help

## References

- NCI Access Guide: https://opus.nci.org.au/display/Help/Accessing+Gadi
- Mancini Portal: https://my.nci.org.au/
