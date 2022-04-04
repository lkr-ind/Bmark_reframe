import os
import pandas as pd

from datetime import datetime
from glob import glob
from typing import Optional


this_dir = os.path.dirname(os.path.abspath(__file__))


class ReFrameBenchmarkLine:
    """A single benchmark present in a ReFrame perflog file"""

    def __init__(self, line: Optional[str]):

        self._raw_line = line

        self.datetime = None                  # e.g.  2022-03-24T21:01:12
        self.reframe_version = None           # e.g.  3.10.0
        self.name = None                      # e.g.  RamsesMPI_strong_128
        self.system = None                    # e.g.  dial
        self.partition = None                 # e.g.  slurm-mpirun
        self.dependencies = None              # e.g.  intel-oneapi-openmpi
        self.num_tasks = None                 # e.g.  128
        self.num_tasks_per_node = None        # e.g.  128

        self.metric_name = None               # e.g.  Total elapsed time
        self.metric_value = None              # e.g.  41.51
        self.metric_reference = None          # e.g.  0

        if line is not None:
            self._set_attributes(line)

    @property
    def values(self) -> list:
        """Create a data frame from all the public attributes in this class"""
        return [v for k, v in self.__dict__.items() if not k.startswith('_')]

    @classmethod
    def column_names(cls) -> list:
        """Names of the columns in this log line"""

        tmp = cls(line=None)

        return [k for k in tmp.__dict__.keys() if not k.startswith('_')]

    def _set_attributes(self, line: str) -> None:
        """Set all the extractable attributes from the log file"""

        self.datetime = datetime.fromisoformat(line.split('|')[0])
        self.reframe_version = self._extract_reframe_version()
        self._set_name_and_system()
        self.num_tasks = int(self._value_of('num_tasks'))
        self.num_tasks_per_node = int(self._value_of('num_tasks_per_node'))
        self.metric_name = self._extract_metric_name()
        self.metric_value = float(self._value_of(self.metric_name))
        self.metric_reference = float(self._extract_metric_ref())

    def _set_name_and_system(self) -> None:
        """Set the name and system specifics from the appropriate section"""

        section = self._raw_line.split('|')[2]
        self.name = section.split()[0]

        system_and_partition = section.split(' on ')[1].split(' using ')[0]
        self.system, self.partition = system_and_partition.split(':')

        self.dependencies = section.split(' using ')[1]

        return None

    def _extract_metric_name(self) -> str:
        return self._raw_line.split('|')[-3].split('=')[0]

    def _value_of(self, s) -> str:
        return next(x.split('=')[1] for x in self._raw_line.split('|') if s in x)

    def _extract_reframe_version(self) -> str:
        return self._raw_line.split('|')[1].split()[1].split('+')[0]

    def _extract_metric_ref(self) -> str:
        return self._raw_line.split('|')[-2].split()[0].split('=')[1]


class ReFrameLogFile:
    """A ReFrame generated perflog file containing benchmark(s)"""

    def __init__(self, file_path: str):

        self.file_path = self._validated(file_path)
        self.rows = []

        for line in open(self.file_path, 'r'):
           self.rows.append(ReFrameBenchmarkLine(line).values)

    @staticmethod
    def _validated(file_path: str) -> str:

        if not file_path.endswith('.log') or not os.path.exists(file_path):
            raise ValueError('File did not exist, or wasn\'t a .log')

        return file_path


def create_full_data_frame(relative_root: str) -> pd.DataFrame:
    """
    Create a pandas dataframe comprised of all the ReFrame benchmark data that
    can be found from a root directory relative to the path of this file and
    the sub directories within.

    ---------------------------------------------------------------------------
    Arguments:
        relative_root: Directory path relative to this one. For example: '.'
                       is the directory where this file is present and '..' one
                       directory up from this one

    Returns:
        (pd.DataFrame): Full data frame
    """
    rows = []

    for file_path in glob(os.path.join(this_dir, relative_root, '**/*.log'),
                          recursive=True):

        try:
            log_file = ReFrameLogFile(file_path)
            rows += log_file.rows

        except (ValueError, IndexError):
            continue

    return pd.DataFrame(rows, columns=ReFrameBenchmarkLine.column_names())


def plot_ramses_strong(data_frame):
    """Plot a strong scaling plot for Ramses"""


if __name__ == '__main__':

    df = create_full_data_frame(relative_root='..')

    # plot_ramses_strong(df)
    # plot_ramses_weak(df)
    # plot_sphng_strong(df)
    # plot_sphng_strong(df)
    # plot_trove(df)
