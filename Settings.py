#Copyright 2016-2021 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

#
# Generic fallback configuration
#

site_configuration = {
    'systems': [
        {
            'name': 'cosma8',
            'descr': 'COSMA8',
            'hostnames': ['.*'],
            'modules_system': 'tmod4',
            'partitions': [
                {
                    'name': 'compute-node',
                    'descr': 'Compute nodes',
                    'scheduler': 'slurm',
                    'launcher': 'mpirun',
                    'access': ['--partition=cosma8','-A do006'],
                    'environs': ['intel20-mpi-durham', 'intel20_u2-mpi-durham', 'intel19-mpi-durham', 'intel19_u3-mpi-durham'],
                    'max_jobs': 64,
                    'processor': {'num_cpus': 256,
                                  'num_cpus_per_core': 2,
                                  'num_sockets': 2,
                                  'num_cpus_per_socket': 128}
                },
            ]
        },

        {
            'name': 'dial',
            'descr': 'Dirac Data Intensive @ Leicester',
            'hostnames': ['.*'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'slurm-mpirun',
                    'descr': 'Compute nodes',
                    'scheduler': 'slurm',
                    'launcher': 'mpirun',
                    'access': ['-A ds004'],
                    'environs': ['intel-oneapi-openmpi-dial3','intel19-mpi-dial3'],
                    'max_jobs': 64,
                    'processor': {'num_cpus': 128,
                                  'num_cpus_per_core': 1,
                                  'num_sockets': 2,
                                  'num_cpus_per_socket': 64}
                },
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
            'name': 'intel20-mpi-durham',
            'modules':['intel_comp/2020','intel_mpi/2020'],
            'cc': 'mpiicc',
            'cxx': 'mpiicpc',
            'ftn': 'mpiifort'
        },
        {
            'name': 'intel20_u2-mpi-durham',
            'modules':['intel_comp/2020-update2','intel_mpi/2020-update2'],
            'cc': 'mpiicc',
            'cxx': 'mpiicpc',
            'ftn': 'mpiifort'
        },
        {
            'name': 'intel19-mpi-durham',
            'modules':['intel_comp/2019','intel_mpi/2019'],
            'cc': 'mpiicc',
            'cxx': 'mpiicpc',
            'ftn': 'mpiifort'
        },
        {
            'name': 'intel19_u3-mpi-durham',
            'modules':['intel_comp/2019-update3','intel_mpi/2019-update3'],
            'cc': 'mpiicc',
            'cxx': 'mpiicpc',
            'ftn': 'mpiifort'
        },
        {
            'name':'intel-oneapi-openmpi-dial3',
            'modules':['intel-oneapi-compilers/2021.2.0','openmpi4/intel/4.0.5'],
            'cc':'mpicc',
            'cxx':'mpicxx',
            'ftn':'mpif90'
        },
        {
            'name': 'intel19-mpi-dial3',
            'modules':['intel-parallel-studio/cluster.2019.5'],
            'cc': 'mpiicc',
            'cxx': 'mpiicpc',
            'ftn': 'mpiifort'
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
    'schedulers': [
        {
            'name': 'slurm',
            'target_systems': ['cosma8'],
            'use_nodes_option': True,
        },
    ],

}

