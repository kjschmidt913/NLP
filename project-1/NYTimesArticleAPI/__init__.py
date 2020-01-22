from .search_api import *

__version__ = "1.0.0"
__author__ = "Matt Morrison (@MattDMo)"
__all__ = ["articleAPI"]

if __name__ == "__main__":
    print("This module cannot be run on its own. Please use by running ",
          "\"from NYTimesArticleAPI import articleAPI\"")
    exit(0)
