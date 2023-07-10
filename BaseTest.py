import WPTestLib
import WPTestClient
import platform
import sys

# BaseTest
# Written by Angela Korra'ti
# Last updated 7/10/2023
#
# This is the base test class for the other ones in the suite.


class BaseTest:
    wp_lib = None
    wp_tc = None
    platform = platform.system()
    maxsize = sys.maxsize
    minsize = -sys.maxsize

    def setup_method(self):
        """
        Setup method for the class
        """
        self.wp_lib = WPTestLib.WPTestLib()
        self.wp_tc = WPTestClient.WPTestClient(self.wp_lib.host, self.wp_lib.protocol)
