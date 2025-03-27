# Working with QUT's HPC - Workflow

## 1. Connecting to HPC
   - Method 1 - Install Putty and set aqua@qut.edu.au as host name.
   - Method 2 - In the windows terminal, type
   ```
   ssh amarasi5@aqua.qut.edu.au
   ``` 
   - Then enter password.
   - Method 3 - Open VS Code --> Terminal --> follow Method 2.

## 2. Mounting your HPC Home Folder
- [Create local network drive and mount with HPC](https://qutvirtual4.qut.edu.au/group/research-students/conducting-research/specialty-research-facilities/advanced-research-computing-storage/supercomputing/using-hpc-filesystems#h2-0)

## 3. Conda setup
### Download Miniconda
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
### Run the installer and specify a valid home directory
```
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
```
### Initialize Conda

```
$HOME/miniconda3/bin/conda init
```

### Update .bashrc
```
echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## 4. Conda create and activate

### Load Conda if not already loaded
```
source $HOME/miniconda3/bin/activate
```

```
conda init
```
#### Step 1: Create and Activate the Environment

```
conda create --name myenv python=3.10 -y
```
```
conda activate envhpc
```

#### Step 2: Install TensorFlow and Required Libraries
```
conda install -y tensorflow=2.12 keras=2.12.0 keras-preprocessing=1.1.2 -c conda-forge
```
#### Step 3: Install modules in existing environment
```
conda install --file requirements.txt` or `pip install -r requirements.txt`.
```

#### Step 4: Install required Libraries
```
conda install -y -c nvidia -c rapidsai -c conda-forge -c defaults \
    cudatoolkit=11.2.2 \
    cuda-python=11.8 \
    cudf=23.02 \
    cuml=23.02 \
    cudnn=8.1.0.77 \
    cupy=11.5.0 \
    curl=7.87.0
```
##### Install OpenCV via Pip
```
pip install opencv-python opencv-python-headless
```
##### Install Matplotlib via Pip
```
pip install matplotlib
```
##### Install Seaborn via Pip
```
pip install seaborn
```
##### Install scikit-image via Pip
```
pip install scikit-image
```
##### Install GDAL via Conda (specify the channel)
```
conda install -c conda-forge gdal
```
##### XGBoost install using pip (Recommended for most cases)
```
pip install xgboost==1.7.5
```

#### Create the Environment using existing libraries 
Open your terminal or command prompt, navigate to the directory containing your environment.yml file, and execute the following command
```
conda env create -f environment.yml
```

This command reads the environment.yml file and creates the environment as specified. If the environment.yml file includes a name field, that name will be used for the environment. Otherwise, you can specify a name using the -n or --name option:
```
conda env create -f environment.yml -n myenv
```

Activate the Environment: After creation, activate the new environment 
```
conda activate myenv
```

## 6. Submitting Jobs on GPU Nodes (Example code)

CPU-Only Interactive Jobs
You can request an interactive CPU-only session using the following command:
   ```
   qsub -I -S /bin/bash -l select=1:ncpus=1:mem=4GB -l walltime=12:00:00
   ``` 
CPU and GPU Interactive Jobs
To maximise utilisation and availability of GPUs, interactive CPU+GPU interactive sessions utilise Nvidia’s Multi Instance GPU (MIG) technology.
   ```
   qsub -I -S /bin/bash -l select=1:ncpus=6:ngpus=1:mem=34gb -l walltime=12:00:00
   ``` 

## 7. List of Useful Commands
   - `qsub`.
   - `qdel`.
   - `qstat`.
   - `pbsusage`.
   - `qjobs`.
   - `pbsnodes`.

## 8. Useful Website Links
   - [QUT HPC Aqua](https://docs.eres.qut.edu.au/major-changes-early-adopters).
   - [QUT's HPC Facilities](https://wiki.qut.edu.au/pages/viewpage.action?spaceKey=cyphy&title=Working+with+QUT%27s+HPC+%28High+Performance+Computing%29+Facilities)
   - [Map a Network Drive in Windows](https://qutvirtual4.qut.edu.au/group/research-students/conducting-research/specialty-research-facilities/advanced-research-computing-storage/supercomputing/using-hpc-filesystems#h2-0)
   - [SSHFS-Win GitHub Repository](https://github.com/winfsp/sshfs-win)
   - [WinFsp Releases](https://github.com/winfsp/winfsp/releases/tag/v1.12.22339)
   - [Miniforge GitHub Repository](https://github.com/conda-forge/miniforge)
   - [Managing Environments with Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)

## 9. Check Host Name
```python
import socket
hostname = socket.gethostname()
print(hostname)
```

## 10. Check IP address
```python
import socket
remote_host = "lyra01"
try:
    remote_ip = socket.gethostbyname(remote_host)
    print(f"The IP address of {remote_host} is {remote_ip}")
except socket.gaierror:
    print(f"Could not get the IP address of {remote_host}")
```

## 11. Check GPU and CPU number
```python
import paramiko
```

### Create an SSH client
```python
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
```

### Connect to the remote server
```python
client.connect('10.13.0.10', username='n10837647', password='NMilan!@2023')
```

### Run the nvidia-smi command on the remote server to check the number of GPUs
```python
stdin, stdout, stderr = client.exec_command('nvidia-smi -L')
num_gpus = len(stdout.readlines())
print(f"Number of GPUs: {num_gpus}")
```

### Run the lscpu command on the remote server to check the number of CPUs
```python
stdin, stdout, stderr = client.exec_command('lscpu | grep "^CPU(s):"')
output = stdout.read().decode()
num_cpus = output.strip().split()[1]
print(f"Number of CPUs: {num_cpus}")
```

### Close the SSH client
```python
client.close()
```

### Find the Current Directory (Your Folder Path)
```
pwd
```
