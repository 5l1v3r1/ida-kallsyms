#!/usr/bin/env python3
import gzip
import os
import unittest

from find_kallsyms import find_kallsyms_in_rodata


class TestFindKallsyms(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.basedir = os.path.dirname(__file__)

    def _read(self, name):
        with gzip.GzipFile(os.path.join(self.basedir, name)) as fp:
            return bytearray(fp.read())

    def test_kallsyms_4_16_3_s390x(self):
        addresses_and_names = list(find_kallsyms_in_rodata(
            self._read('kallsyms-4.16.3-301.fc28.s390x.gz'), '>'))
        self.assertEquals('T_text', addresses_and_names[0][1])
        self.assertEquals('B__bss_stop', addresses_and_names[-1][1])

    def test_kallsyms_3_10_0_x86_64(self):
        addresses_and_names = list(find_kallsyms_in_rodata(
            self._read('kallsyms-3.10.0-862.11.6.el7.x86_64.gz'), '<'))
        self.assertEquals('Airq_stack_union', addresses_and_names[0][1])
        self.assertEquals('B__brk_limit', addresses_and_names[-1][1])

    def test_kallsyms_5_1_9_x86_64(self):
        addresses_and_names = list(find_kallsyms_in_rodata(
            self._read('kallsyms-5.1.9.balsnctl2019.krazynote.x86_64.gz'),
            '<'))
        self.assertEquals('Airq_stack_union', addresses_and_names[0][1])
        self.assertEquals('B__brk_limit', addresses_and_names[-1][1])


if __name__ == '__main__':
    unittest.main()