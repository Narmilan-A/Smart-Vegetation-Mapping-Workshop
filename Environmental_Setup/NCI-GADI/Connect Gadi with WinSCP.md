# Step-by-Step: Connect Gadi with WinSCP

This guide will walk you through the process of connecting **Gadi** with **WinSCP** to transfer files between your local machine and Gadi’s cluster.

## 1. Download and Install WinSCP

1. Visit the official [WinSCP download page](https://winscp.net/eng/download.php).
2. Download and install the appropriate version for your operating system.

## 2. Open WinSCP and Set Up a New Session

1. Launch **WinSCP**.
2. Click on **New Session** to configure your connection to Gadi.

## 3. Enter Connection Details in WinSCP

In the "Session" tab, enter the following details:

- **File protocol**: `SFTP`
- **Host name**: `gadi.nci.org.au`
- **Port number**: `22` (default)
- **Username**: `na0931` (your Gadi username)
- **Password**: (your Gadi password, entered when prompted)

## 4. Save Session for Future Use (Optional)

1. Under **Session** > **Saved Sessions**, type a name for this session, e.g., `Gadi`.
2. Click **Save** to save the session for quick future access.

## 5. Log In to Gadi

- Once the session is configured, click **Login**.
- A **Security Alert** may pop up; click **Yes** to accept the server’s host key.
- Enter your **Gadi password** when prompted.

## 6. Navigating File Systems in WinSCP

- On the **left panel**, you will see your **local file system**.
- On the **right panel**, you will see the **Gadi file system**, starting in your home directory (`/home/na0931`).

## 7. Transfer Files Between Local Machine and Gadi

- **Upload files**: Drag and drop files from the **left pane** (local machine) to the **right pane** (Gadi file system).
- **Download files**: Drag and drop files from the **right pane** (Gadi file system) to the **left pane** (local machine).

## 8. Access Scratch Directory on Gadi (Optional)

To navigate to your **scratch space**:

1. In the **right pane** (Gadi file system), you can access your **scratch space** by navigating to `/scratch/ru19/na0931`.
   
   To create your scratch directory (if it doesn’t exist), **run the following command** in a Gadi terminal:

   ```bash
   mkdir -p /scratch/ru19/na0931
