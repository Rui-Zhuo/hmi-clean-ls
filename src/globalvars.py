# Edited by Rui, 2025/11/13
"""Contains class to handle global variables

"""


class DopplerVars():
    """Class to handle all the global variables and 
    parameters

    Methods:
    --------
    __init__ - initializes the object
    get_dir  - gets directory path

    """

    def __init__(self, day):
        # self.scratch = "/scratch/g.samarth"
        # self.seismo = "/scratch/seismogroup"
        # self.home = "/home/g.samarth" # Edited by Rui, 2025/11/13
        # self.scratch = 'C:/Users/rzhuo/Desktop/'
        # self.seismo = 'C:/Users/rzhuo/Desktop/'
        # self.home = 'C:/Users/rzhuo/Desktop/' # Edited by Rui, 2025/11/13, 2025/11/21
        self.scratch = 'E:/Research/Work/Flux_emergence_of_bipolars_by_SDO/'
        self.seismo = 'E:/Research/Work/Flux_emergence_of_bipolars_by_SDO/'
        self.home = 'E:/Research/Work/Flux_emergence_of_bipolars_by_SDO/' # Edited by Rui, 2025/11/21
        self.hmidir = self.get_dir("hmidata")
        self.outdir = self.get_dir("output")
        self.plotdir = self.get_dir("plot")
        # self.year = "2018" # Edited by Rui, 2025/11/13
        self.year = "2024" 

        # resolution of computation lmax = 3*nside - 1
        self.nside = 512
        self.day = day

    def get_dir(self, dirname):
        """Returns directories used in the program

        Parameters:
        -----------
        dirname - str
            Selector for directories
            possible values ("hmidata", "plot", "output")

        Returns:
        --------
        directory - str
            full path

        """
        if dirname == "hmidata":
            directory = f"{self.seismo}/data/HMI/dopplergrams"
        elif dirname == "plot":
            directory = f"{self.scratch}/plots/dopplervel"
        elif dirname == "output":
            directory = f"{self.scratch}/HMIDATA/data_analysis"
        else:
            print("dirname not recognized")
            directory = None
        return directory
