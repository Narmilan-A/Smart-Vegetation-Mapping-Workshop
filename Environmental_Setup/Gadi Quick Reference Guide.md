# Gadi Quick Reference Guide

This guide provides essential commands and configurations for users of the Gadi supercomputing environment at NCI.

---

## 📁 Filesystems Overview

| Filesystem    | Description                                                                                 |
|---------------|---------------------------------------------------------------------------------------------|
| `/home`       | Backed up; 10 GiB fixed quota per user.                                                     |
| `/scratch`    | Not backed up; temporary files; auto purge policy applied.                                  |
| `/g/data`     | Not backed up; long-term large data files.                                                  |
| `/apps`       | Read-only; centrally installed software applications and their module files.                |
| `$PBS_JOBFS`  | Not backed up; local to the node; I/O intensive data.                                       |
| `massdata`    | Backed up; archiving large data files.                                                      |

---

## 🧾 Accounting Commands

- `nci_account`  
  Display compute grant and usage.

- `quota -s`  
  Display storage grant and usage on `/home`.

- `lquota`  
  Display storage grant and usage on `/scratch` and `/g/data` by project.

- `nci-files-report -f <fs> -g <grp>`  
  Report data usage on filesystem `<fs>` owned by the project `<grp>` by (project folder, user).

---

## 📦 Module Commands

- `module avail`  
  List all available modules.

- `module avail <abc>`  
  List all available modules that start with `<abc>`.

- `module load <app>/<ver>`  
  Load the module for application `<app>` version `<ver>`.

- `module unload <app>`  
  Remove the module for application `<app>` from the current shell.

- `module show <app>/<ver>`  
  Show what the module `<app>/<version>` does.

- `module list`  
  List all modules loaded in the current shell.

- `module switch abc/123 abc/789`  
  Swap between loaded module versions.

- `module purge`  
  Removes all loaded modules (Note: Will also unload the PBS module).

---

## 🎛️ PBSPro Commands

> **Note:** Run commands in this section with a frequency < 0.2 Hz.

- `qsub job.sh`  
  Submit job defined in the submission script `job.sh`.

- `qdel <jobid>`  
  Delete the job with job ID `<jobid>`.

- `qstat -swx <jobid>`  
  Display the job status in the queue with comment.

- `qstat -fx <jobid>`  
  Display full job status information.

- `qps <jobid>`  
  Take a snapshot of the process status of all current processes in the running job.

- `qcat [-s/-o/-e] <jobid>`  
  Display [submission script/STDOUT/STDERR] of the running job.

- `qls <jobid>`  
  List contents in the folder `$PBS_JOBFS`.

- `qcp <jobid> <dst>`  
  Copy files and directories from the folder `$PBS_JOBFS` to the destination folder `<dst>`.

- `nqstat_anu <jobid>`  
  Provides descriptive job information.

---

## 📝 PBSPro Directives

- `#PBS -P <prj>`  
  Project for job debiting, `/scratch` project folder access, and data ownership.

- `#PBS -q <queue>`  
  Submit the job to the queue `<queue>`.

- `#PBS -l ncpus=<xx>`  
  Request `<xx>` CPU cores.

- `#PBS -l storage=<scratch/prj1+gdata/prj2+massdata/prj3>`  
  Storage needed to be available inside the job. `massdata` is only available in `copyq` jobs.

- `#PBS -l ngpus=<yy>`  
  Number of GPUs; `ncpus` has to be 12 x `ngpus` and the job has to be submitted to `gpuvolta`.

- `#PBS -l walltime=<hh:mm:ss>`  
  Max walltime the job would run.

- `#PBS -l mem=<10GB>`  
  Memory allocation.

- `#PBS -l jobfs=<40GB>`  
  Disk allocation on compute/copyq node(s).

- `#PBS -l software=<app1,app2>`  
  Licences required.

- `#PBS -l wd`  
  Start the job from the directory in which it was submitted.

- `#PBS -W depend=beforeok:<jobid1,jobid2>`  
  Set dependencies between this and other jobs.

- `#PBS -a <YYMMhhmm>`  
  Time after which the job is eligible for execution.

- `#PBS -M <email@example.com,email2@anu.edu.au>`  
  List of receivers to whom email about the job is sent.

- `#PBS -m <aben>`  
  Email events: `a` for abortion, `b` for begin, `e` for end, `n` for none.

---

## 🔗 Useful URLs

- [User & Project Management](https://my.nci.org.au)
- [Knowledge Base](https://opus.nci.org.au)
- [Training Course](https://learning.hpc-australia.org.au)
- [Service Desk Portal](https://help.nci.org.au)
- [Licence Live Status](https://my.nci.org.au/licence-status)

---

**Authors:** Yue Sun, Andrew Johnston  
**Source:** [Gadi Quick Reference Guide](https://opus.nci.org.au/spaces/Help/pages/230490763/Gadi+Quick+Reference+Guide)

