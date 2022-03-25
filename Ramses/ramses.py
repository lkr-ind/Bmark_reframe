import reframe as rfm
import reframe.utility.sanity as sn

#------------------------------------------------------------------------------------------------------------------------------------
# Base class for Ramses.
# Also defines the sanity test.
#------------------------------------------------------------------------------------------------------------------------------------
class RamsesMPI(rfm.RunOnlyRegressionTest):
    
    def __init__(self):
        self.descr = ('Running ramses on one single node')
        self.time_limit = '0d1h0m0s'
        self.valid_systems = ['dial:slurm-mpirun']
        self.valid_prog_environs = ['intel-oneapi-openmpi']
        self.executable = './ramses3d'
        self.num_tasks = 128
        self.executable_opts = ['params.nml']
        reference = {
        'dial:slurm-local': {
            'Total elapsed time:':  (500, None, None, 'seconds'),
                            }
                    }

    @run_before('sanity')
    def run_complete_pattern(self):
        self.pattern = r'Run completed'
        self.sanity_patterns = sn.assert_found(self.pattern, self.stdout)


    @run_before('performance')
    def runtime_extract_pattern(self):
        self.perf_patterns = {'Total elapsed time': sn.extractsingle(r'Total elapsed time:\s+(\S+)\s', self.stdout, 1, float)}

#------------------------------------------------------------------------------------------------------------------------------------
# End of base class.
#------------------------------------------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------------------------------------------------------------------
# Strong scaling test.
#------------------------------------------------------------------------------------------------------------------------------------
@rfm.simple_test
class RamsesMPI_strong(RamsesMPI):
    mpi_tasks = parameter(128*(2**i) for i in range(0,5))
    
    @run_after('init')
    def sef_num_tasks(self):
        self.num_tasks = self.mpi_tasks
        self.num_tasks_per_node = 128
        self.descr = ('Strong Scaling Ramses on '+str(self.mpi_tasks/128)+ ' node/s')

#------------------------------------------------------------------------------------------------------------------------------------
# End of strong scaling test.
#------------------------------------------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------------------------------------------------------------------
# Weak scaling tests.
#------------------------------------------------------------------------------------------------------------------------------------
@rfm.simple_test
class RamsesMPI_weak(RamsesMPI):
    
    num_nodes = parameter(2**i for i in range(0,4))
    
    @run_after('init')
    def set_1_nodes_executable(self):
        self.num_tasks = self.num_nodes * 128
        self.num_tasks_per_node = 128
        self.descr = ('Weak Scaling Ramses on '+str(self.num_nodes)+ ' node/s')
        self.executable_opts = ['params'+str(self.num_nodes)+'_weak.nml']

#------------------------------------------------------------------------------------------------------------------------------------
# End of weak scaling tests.
#------------------------------------------------------------------------------------------------------------------------------------
