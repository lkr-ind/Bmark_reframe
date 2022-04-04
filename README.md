# Bmark_reframe

This repository contains the reframe code to run the the three benchmark codes for Leicester namely: Ramses, Sphng and Trove.

At present, the build step is separate and is not integrated with the Reframe. For building codes, we can use either Spack and its associated settings file or the normal build process using make.

We are currently including the executables in this repository.



### Steps to run a benchmark

1. You would first need to use the settings file that is included in the current repository. This file has been specifically written for Dial3 cluster while the logging format at the end is generic and can be adapted to any system.

   ```bash
   export RFM_CONFIG_FILE=settings.py
   ```

2. Then you can run the three benchmarks by one of the following three commands.

   ```bash
   #1. Trove
   reframe -c ./trove.py -r --performance-report --keep-stage-files
   
   #2. Sphng
   reframe -c ./sphng.py -r --performance-report --keep-stage-files
   
   #3. Ramses
   reframe -c ./ramses.py -r --performance-report --keep-stage-files
   ```

   

Note:- Since the benchmarks take good enough time to run and they may be in the queue for a long time, we suggest to use a method by which you can restore your SSH session such as by using `tmux`.

### Steps to visualise the data

To generate a pdf report including the benchmarks.

   ```bash
   cd graphing && make
   ```

Note:- Latex and Python are required + the Python requirements (`graphing/requirements.txt`).
