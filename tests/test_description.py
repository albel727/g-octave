#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    test_description.py
    ~~~~~~~~~~~~~~~~~~~
    
    test suite for the *g_octave.description* module
    
    :copyright: (c) 2010 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

import os
import unittest

from g_octave import description


class TestDescription(unittest.TestCase):
    
    def setUp(self):
        self.desc = description.Description(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 'DESCRIPTION'
            )
        )
    
    def test_re_depends(self):
        depends = [
            ('pkg', ('pkg', None, None)),
            ('pkg(<1)', ('pkg', '<', '1')),
            ('pkg(>1)', ('pkg', '>', '1')),
            ('pkg(<=1)', ('pkg', '<=', '1')),
            ('pkg(>=1)', ('pkg', '>=', '1')),
            ('pkg(==1)', ('pkg', '==', '1')),
            ('pkg( <1)', ('pkg', '<', '1')),
            ('pkg( >1)', ('pkg', '>', '1')),
            ('pkg( <=1)', ('pkg', '<=', '1')),
            ('pkg( >=1)', ('pkg', '>=', '1')),
            ('pkg( ==1)', ('pkg', '==', '1')),
            ('pkg(<1 )', ('pkg', '<', '1')),
            ('pkg(>1 )', ('pkg', '>', '1')),
            ('pkg(<=1 )', ('pkg', '<=', '1')),
            ('pkg(>=1 )', ('pkg', '>=', '1')),
            ('pkg(==1 )', ('pkg', '==', '1')),
            ('pkg( <1 )', ('pkg', '<', '1')),
            ('pkg( >1 )', ('pkg', '>', '1')),
            ('pkg( <=1 )', ('pkg', '<=', '1')),
            ('pkg( >=1 )', ('pkg', '>=', '1')),
            ('pkg( ==1 )', ('pkg', '==', '1')),
            ('pkg(<1.0)', ('pkg', '<', '1.0')),
            ('pkg(>1.0)', ('pkg', '>', '1.0')),
            ('pkg(<=1.0)', ('pkg', '<=', '1.0')),
            ('pkg(>=1.0)', ('pkg', '>=', '1.0')),
            ('pkg(==1.0)', ('pkg', '==', '1.0')),
            ('pkg( <1.0)', ('pkg', '<', '1.0')),
            ('pkg( >1.0)', ('pkg', '>', '1.0')),
            ('pkg( <=1.0)', ('pkg', '<=', '1.0')),
            ('pkg( >=1.0)', ('pkg', '>=', '1.0')),
            ('pkg( ==1.0)', ('pkg', '==', '1.0')),
            ('pkg(<1.0 )', ('pkg', '<', '1.0')),
            ('pkg(>1.0 )', ('pkg', '>', '1.0')),
            ('pkg(<=1.0 )', ('pkg', '<=', '1.0')),
            ('pkg(>=1.0 )', ('pkg', '>=', '1.0')),
            ('pkg(==1.0 )', ('pkg', '==', '1.0')),
            ('pkg( <1.0 )', ('pkg', '<', '1.0')),
            ('pkg( >1.0 )', ('pkg', '>', '1.0')),
            ('pkg( <=1.0 )', ('pkg', '<=', '1.0')),
            ('pkg( >=1.0 )', ('pkg', '>=', '1.0')),
            ('pkg( ==1.0 )', ('pkg', '==', '1.0')),
            ('pkg(<1.0.0)', ('pkg', '<', '1.0.0')),
            ('pkg(>1.0.0)', ('pkg', '>', '1.0.0')),
            ('pkg(<=1.0.0)', ('pkg', '<=', '1.0.0')),
            ('pkg(>=1.0.0)', ('pkg', '>=', '1.0.0')),
            ('pkg(==1.0.0)', ('pkg', '==', '1.0.0')),
            ('pkg( <1.0.0)', ('pkg', '<', '1.0.0')),
            ('pkg( >1.0.0)', ('pkg', '>', '1.0.0')),
            ('pkg( <=1.0.0)', ('pkg', '<=', '1.0.0')),
            ('pkg( >=1.0.0)', ('pkg', '>=', '1.0.0')),
            ('pkg( ==1.0.0)', ('pkg', '==', '1.0.0')),
            ('pkg(<1.0.0 )', ('pkg', '<', '1.0.0')),
            ('pkg(>1.0.0 )', ('pkg', '>', '1.0.0')),
            ('pkg(<=1.0.0 )', ('pkg', '<=', '1.0.0')),
            ('pkg(>=1.0.0 )', ('pkg', '>=', '1.0.0')),
            ('pkg(==1.0.0 )', ('pkg', '==', '1.0.0')),
            ('pkg( <1.0.0 )', ('pkg', '<', '1.0.0')),
            ('pkg( >1.0.0 )', ('pkg', '>', '1.0.0')),
            ('pkg( <=1.0.0 )', ('pkg', '<=', '1.0.0')),
            ('pkg( >=1.0.0 )', ('pkg', '>=', '1.0.0')),
            ('pkg( ==1.0.0 )', ('pkg', '==', '1.0.0')),
        ]
        for pkgstr, pkgtpl in depends:
            match = description.re_depends.match(pkgstr)
            self.assertEqual(
                (match.group(1), match.group(3), match.group(4)),
                pkgtpl
            )
    
    def test_re_pkg_atom(self):
        depends = [
            ('pkg-1', ('pkg', '1')),
            ('pkg-1.0', ('pkg', '1.0')),
            ('pkg-1.0.0', ('pkg', '1.0.0')),
        ]
        for pkgstr, pkgtpl in depends:
            match = description.re_pkg_atom.match(pkgstr)
            self.assertEqual(
                (match.group(1), match.group(2)),
                pkgtpl
            )


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDescription('test_re_depends'))
    suite.addTest(TestDescription('test_re_pkg_atom'))
    return suite

