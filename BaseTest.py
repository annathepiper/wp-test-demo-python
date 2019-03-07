import WPTestLib
import WPTestClient
import platform

# BaseTest
# Written by Angela Korra'ti
# Last updated 3/6/2019
#
# This is the base test class for the other ones in the suite.


class BaseTest:
    wp_lib = None
    wp_tc = None
    platform = platform.system()

    def __init__(self):
        """
        Init method for the class
        """
        self.wp_lib = WPTestLib.WPTestLib()
        self.wp_tc = WPTestClient.WPTestClient(self.wp_lib.host, self.wp_lib.protocol)
