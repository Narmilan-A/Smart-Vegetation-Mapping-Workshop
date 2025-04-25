
# Running Jobs on Gadi

To run compute tasks such as simulations, weather models, and sequence assemblies on Gadi, users need to submit them as ‘jobs’ to ‘queues’. Each queue has different hardware capabilities and limits. The overall procedure takes a few steps, which we will outline here. But here are a few key points before moving on:

- **Job Submission**: Users must specify the queue, duration, and resource needs of their jobs. Gadi uses PBSPro to schedule all submitted jobs and keeps nodes with different hardware in different queues.  
- **Resource Estimation**: When wrapping your tasks inside a job for submission, you need to estimate the computational resources the job will use and the duration for which it will run. This helps the job scheduler reserve the right resources for the job.
- **Over-Usage of Resources**: If a job uses more than it requested, it will be immediately terminated. See the [Gadi Queue Limit page](#) for more details on resource limits and costs on each type of node.
- **Job Execution**: Once the requested amount of resources becomes available, the job is sent to the scheduled hosting node(s). For multi-node jobs, the job starts on the head node where all commands in the job submission script are executed.
- **Internet Access**: If any task in the job requires internet access, it must be separately packed into a job on a copyq node, as none of the standard compute nodes have external network access outside of Gadi.

## Creating a Submission Script

To run jobs on Gadi, users need to create a PBS submission script. This script can be written in any editor (e.g., vim, nano) and contains simple lines to specify how PBS should run your job. Here is an example of a basic PBS script:

```bash
#!/bin/bash
#PBS -S /bin/bash
#PBS -l select=1:ncpus=48:mem=190GB:jobfs=200GB
#PBS -q normal
#PBS -P a00
#PBS -l walltime=02:00:00
#PBS -l storage=gdata/a00+scratch
#PBS -j oe
cd $PBS_O_WORKDIR
module load python3/3.7.4
python3 $PBS_NCPUS > $PBS_JOBID.log
```

### Script Explanation:
- **Shell to use**: `#!/bin/bash` specifies the shell.
- **Resources**: Requests 48 CPU cores, 190 GiB of memory, and 200 GiB of local disk.
- **Queue**: The job is submitted to the 'normal' queue.
- **Project**: Submitting under project `a00`.
- **Walltime**: Requested walltime of 2 hours.
- **Storage**: Using `gdata/a00` and `/scratch` for storage.
- **Job Output**: Redirects output of the script to a log file in `gdata/a00`.

### Job Submission Command:
After saving the script as a `.sh` file, submit it using the following command:

```bash
qsub <jobscript.sh>
```

Once the job is submitted successfully, you will be assigned a `jobID` (e.g., `12345678.gadi-pbs`). Use this jobID to monitor and inquire about your job's status.

### Monitoring Jobs:
To monitor your job, refer to the [Job Monitoring Guide](#). 

### Resource Usage Efficiency:
It is recommended to request only the necessary resources to allow the job to run close to its 'sweet spot'—where parallelism is maximized and efficiency is at least 80%. Experimentation may be required to find this efficiency.

### Standard Output/Error:
By default, the standard output and error stream of the job are saved in files named `<jobname>.o<jobid>` and `<jobname>.e<jobid>`. These are located in the directory from where the job was submitted.

---

## Interactive Jobs

Interactive jobs allow users to run jobs that can be monitored and adjusted during their lifecycle. This is useful for debugging code or installing applications that require GPUs.

To submit an interactive job, use the following command:

```bash
qsub -I -q gpuvolta -P a00 -l walltime=00:05:00,ncpus=48,ngpus=4,mem=380GB,jobfs=200GB,storage=gdata/a00,wd
```

### Example Process:
1. **Job Submission**: Submitting a job on the `gpuvolta` queue with specific resource requests (48 CPUs, 4 GPUs, 380 GiB memory, etc.).
2. **Job Start**: After the job begins, you will be logged into a compute node (e.g., `gadi-gpu-v100-0079`).
3. **Exit Command**: Use `exit` to terminate the job once it's complete.

```bash
[aaa777@gadi-gpu-v100-0079 ~]$ exit
qsub: job 11029947.gadi-pbs completed
```

---

## Copyq Jobs

For long-running jobs or those requiring internet access, submit jobs through the `copyq` queue. This queue is specifically designed for tasks like transferring large amounts of data or installing software that requires significant resources.

### Example PBS Script for Copyq:

```bash
#!/bin/bash
#PBS -l ncpus=1
#PBS -l mem=2GB
#PBS -l jobfs=2GB
#PBS -q copyq
#PBS -l other=mdss
#PBS -P a00
#PBS -l walltime=02:00:00
#PBS -l storage=gdata/a00+massdata/a00
#PBS -l wd

tar -cvf my_archive.tar /g/data/a00/aaa777/work1
mdss -P a00 mkdir -p aaa777/test/
mdss -P a00 put my_archive.tar aaa777/test/work1.tar
mdss -P a00 dmls -ltrh aaa777/test
```

### Script Explanation:
- **Queue**: The `copyq` queue is specified with `#PBS -q copyq`.
- **Mass Data**: The job requests access to massdata with `#PBS -lother=mdss`.
- **Commands**: Creates a tar archive, makes a directory on massdata, and confirms the data transfer.

---

### Reference

If you need to monitor the progress of jobs running on Gadi, you can use the *Job Monitoring* page from the NCI Opus site. This page provides instructions on how to track job statuses and check their logs:

NCI. (n.d.). *Job monitoring*. Opus - NCI Confluence. Retrieved from [https://opus.nci.org.au/spaces/Help/pages/236880322/Job+monitoring](https://opus.nci.org.au/spaces/Help/pages/236880322/Job+monitoring)

