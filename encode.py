#! /Users/appa/.pyenv/versions/3.9.4/bin/python
# coding: EUC-JP

import locale
print("locale.getpreferredencoding:", locale.getpreferredencoding())

dummy_dir = '/Users/appa/Documents/Projects/Python/python-basics/dummy'
euc_file = 'euc.txt'
with open(dummy_dir + "/" + euc_file, mode='w') as f:
    f.write("ハローＥＵＣだよ")
print ("Done")


