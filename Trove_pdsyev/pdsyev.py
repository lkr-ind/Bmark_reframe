import os
import sys
import reframe as rfm
import reframe.utility.sanity as sn
import reframe.utility.udeps as udeps


#--------------------------------------------------------------------------
# Define base class for Pdsyev.
# This class will be used for all 3 cases namely 12N, 14N and 16N.
#--------------------------------------------------------------------------
class Pdsyev(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Base class for Pdsyev'
        self.time_limit = '0d2h0m0s'
        self.exclusive_access=True
        self.valid_systems = ['*']
        self.valid_prog_environs = ['*']
        self.executable = './diag_pdsyev_darwin.x'

        reference = {
         'dial:slurm-local': {
             'Total elapsed time:':  (5000, None, None, 'seconds'),
                             }
                     }

    @run_before('sanity')
    def run_complete_pattern(self):
        self.pattern = r'Diagonalization finished successfully'
        self.sanity_patterns = sn.assert_found(self.pattern, 'output_file.text')


    @performance_function('seconds')
    def get_elapsed_time(self):
        #return sn.extractsingle(r'TROVE\s+(\S+)\s+(\S+)', self.stdout, 2, float)
        return sn.extractsingle(r'Time to diagonalize matrix is \s+(\S+)\s', 'output_file.text', 1, float)


    @run_before('performance')
    def runtime_extract_pattern(self):
        self.perf_variables = {
                'Total elapsed time':self.get_elapsed_time()
                }

#--------------------------------------------------------------------------
# End of Base class.
#--------------------------------------------------------------------------



#--------------------------------------------------------------------------
# Code to run the benchmark for input file sized 15K.
#--------------------------------------------------------------------------
@rfm.simple_test
class PDSYEV_15K(Pdsyev):

    tags = {"15K"}
    num_nodes = parameter(2**i for i in range(0,1))
    
    @run_after('setup')
    def set_job_script_variables(self):

        if self.current_partition.processor.num_cpus_per_core > 1:
            self.core_count_1_node = int(self.current_partition.processor.num_cpus/self.current_partition.processor.num_cpus_per_core)
        else:    
            self.core_count_1_node = self.current_partition.processor.num_cpus 
        
        self.num_tasks = self.num_nodes * self.core_count_1_node
        self.num_tasks_per_node = self.core_count_1_node    #We are using the full node with MPI tasks.
        self.descr = ('Running PDSYEV (15K) on '+ str(self.num_nodes) + ' node/s')

#--------------------------------------------------------------------------
# End of code for file named 15K.
#--------------------------------------------------------------------------