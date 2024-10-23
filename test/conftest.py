import sys
import os

actual_dir = os.path.dirname(__file__)
root_dir = os.path.join(actual_dir, "../")
absolute_root_dir = os.path.abspath(root_dir)

sys.path.insert(0, absolute_root_dir)
