# Copyright 2016-2021 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

#
# Generic fallback configuration
#

site_configuration = {
    'systems': [
        {
            'name': 'dial',
            'descr': 'Dirac Data Intensive @ Leicester',
            'hostnames': ['.*'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'default',
                    'descr': 'Login node',
                    'scheduler': 'local',
                    'launcher': 'local',
                    'environs': ['builtin','intel19','intel21','oneapi21','amd3.0','gnu11.1','gnu10.3','gnu10.1','gnu9.3','cray8']
                },
                {
                    'name': 'login-mpirun',
                    'descr': 'Login node (mpirun)',
                    'scheduler': 'local',
                    'launcher': 'mpirun',
                    'environs': ['builtin','intel19-mpi','intel21-mpi','amd3.0-mpi','gnu10.3-mpi']
                },
                {
                    'name': 'slurm-local',
                    'descr': 'Compute nodes-shared mem only',
                    'scheduler': 'slurm',
                    'launcher': 'local',
                    'access': ['-A ds004'],
                    'environs': ['builtin','intel19','intel21','oneapi21','amd3.0','gnu11.1','gnu10.3','gnu10.1','gnu9.3','cray8'],
                },
                {
                    # NB IntelMPI need PMI env var setting currently excluded
                    'name': 'slurm-srun',
                    'descr': 'Compute nodes',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': ['-A ds004'],
                    'environs': ['builtin','amd3.0-mpi','gnu10.3-mpi','cray8-mpi'],
                    'resources': [
                        {
                            'name': 'parallel',
                            'options': ['--ntasks={n_tasks}', '--ntasks-per-node={n_tasks_per_node}']
                        }
                    ]
                },
                {
                    # NB Cray MPI does not have mpirun
                    'name': 'slurm-mpirun',
                    'descr': 'Compute nodes',
                    'scheduler': 'slurm',
                    'launcher': 'mpirun',
                    'access': ['-A ds004'],
                    'environs': ['builtin','intel19-mpi','intel21-mpi','amd3.0-mpi','gnu10.3-mpi','intel-oneapi-openmpi'],
                    'resources': [
                        {
                            'name': 'parallel',
                            'options': ['--ntasks={n_tasks}', '--ntasks-per-node={n_tasks_per_node}']
                        }
                    ]
                }
            ]
        },

         {
            'name': 'generic',
            'descr': 'Generic example system',
            'hostnames': ['.*'],
            'partitions': [
                {
                    'name': 'default',
                    'scheduler': 'local',
                    'launcher': 'local',
                    'environs': ['builtin']
                }
            ]
        },
    ],
    'environments': [
        {
            'name': 'builtin',
            'cc': 'cc',
            'cxx': 'c++',
            'ftn': 'f95'
        },
        {
            'name': 'cray8-mpi',
            'modules':['PrgEnv-cray/8.0.0', 'cray-pmi', 'cray-fftw/3.3.8.8'],
            'cc': 'cc',
            'cxx': 'CC',
            'ftn': 'ftn'
        },
        {
            'name': 'intel19-mpi',
            'modules':['intel-parallel-studio/cluster.2019.5'],
            'cc': 'mpiicc',
            'cxx': 'mpiicpc',
            'ftn': 'mpiifort'
        },
        {
            'name': 'intel21-mpi',
            'modules':['intel-oneapi-compilers/2021.2.0','intel-oneapi-mkl/2021.4.0', 'intel-oneapi-mpi/2021.4.0' ],
            'cc': 'mpiicc',
            'cxx': 'mpiicpc',
            'ftn': 'mpiifort'
        },
        {
            'name': 'amd3.0-mpi',
            'modules':['aocc/3.0.0', 'openmpi/4.0.5', 'amdblis/3.0', 'amdlibm/3.0', 'amdlibflame/3.0'],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },
        {
            'name': 'gnu10.3-mpi',
            'modules':['gcc/10.3.0', 'openmpi/4.0.5', 'openblas/0.3.15'],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        },
        {
            'name':'intel-oneapi-openmpi',
            'modules':['intel-oneapi-compilers/2021.2.0','openmpi4/intel/4.0.5'],
            'cc':'mpicc',
            'cxx':'mpicxx',
            'ftn':'mpif90'
        },
        # Serial compilation environments
        {
            'name': 'intel19',
            'modules':['intel-parallel-studio/cluster.2019.5'],
            'cc': 'icc',
            'cxx': 'icpc',
            'ftn': 'ifort'
        },
        {
            'name': 'intel21',
            'modules':['intel-oneapi-compilers/2021.2.0'],
            'cc': 'icc',
            'cxx': 'icpc',
            'ftn': 'ifort'
        },
        {
            'name': 'oneapi21',
            'modules':['intel-oneapi-compilers/2021.2.0'],
            'cc': 'icx',
            'cxx': 'icpx',
            'ftn': 'ifx'
        },
        {
            'name': 'amd3.0',
            'modules':['aocc/3.0.0', 'amdblis/3.0', 'amdlibm/3.0', 'amdlibflame/3.0'],
            'cc': 'clang',
            'cxx': 'clang++',
            'ftn': 'flang'
        },
        {
            'name': 'gnu11.1',
            'modules':['gcc/11.1.0'],
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran'
        },
        {
            'name': 'gnu10.3',
            'modules':['gcc/10.3.0', 'openblas/0.3.15'],
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran'
        },
        {
            'name': 'gnu10.1',
            'modules':['gcc/10.1.0'],
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran'
        },
        {
            'name': 'gnu9.3',
            'modules':['gcc/9.3.0'],
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran'
        },
        {
            'name': 'cray8',
            'modules':['PrgEnv-cray/8.0.0'],
            'cc': 'cc',
            'cxx': 'CC',
            'ftn': 'ftn'
        },
        
    ],
    'logging': [
        {
            'handlers': [
                {
                    'type': 'stream',
                    'name': 'stdout',
                    'level': 'info',
                    'format': '%(message)s'
                },
                {
                    'type': 'file',
                    'level': 'debug',
                    'format': '[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s', # noqa: E501
                    'append': False
                }
            ],
            'handlers_perflog': [
                {
                    'type': 'filelog',
                    'prefix': '%(check_system)s/%(check_partition)s',
                    'level': 'info',
                    'format': (
                        '%(check_job_completion_time)s|reframe %(version)s|'
                        '%(check_info)s|jobid=%(check_jobid)s|'
                        'num_tasks=%(check_num_tasks)s|'
                        'num_tasks_per_node=%(check_num_tasks_per_node)s|'
                        'num_cpus_per_task=%(check_num_cpus_per_task)s|'
                        '%(check_perf_var)s=%(check_perf_value)s|'
                        'ref=%(check_perf_ref)s '
                        '(l=%(check_perf_lower_thres)s, '
                        'u=%(check_perf_upper_thres)s)|'
                        '%(check_perf_unit)s'
                    ),
                    'append': True
                }
            ]
        }
    ],
}
