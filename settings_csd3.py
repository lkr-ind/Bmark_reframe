# Copyright 2016-2021 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause


site_configuration = {
    'systems': [
            {'name': 'csd3',
            'descr': 'CSD3',
            'hostnames': ['login-e-[0-9]+'],
            'modules_system': 'tmod32',
            'partitions': [
                {
                    'name': 'icelake',
                    'descr': 'Icelake compute nodes',
                    'scheduler': 'slurm',
                    'launcher': 'mpirun',
                    'access': ['-A  DIRAC-DO006-CPU --partition=icelake'],
                    'environs': ['intel2020'],
                    'max_jobs': 64,
                    'processor': {'num_cpus': 76,
                                  'num_cpus_per_core': 1,
                                  'num_sockets': 2,
                                  'num_cpus_per_socket': 38}
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
            'name': 'intel2020',
            'modules': ["intel/compilers/2020.4",
                        "intel/mkl/2020.4",
                        "intel/impi/2020.4/intel",
                        "intel/libs/idb/2020.4",
                        "intel/libs/tbb/2020.4",
                        "intel/libs/ipp/2020.4",
                        "intel/libs/daal/2020.4",
                        "intel/bundles/complib/2020.4"],
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
}
