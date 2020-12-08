#! /bin/env python
# -*- coding: utf-8 -*-
# Author: Viagénie
"""
test_variant_sets - 
"""
import logging
from unittest import TestCase

from lgr.tools.idn_review.variant_sets import generate_variant_sets_report
from tests.unit.utils import load_lgr

logger = logging.getLogger('test_variant_sets')


class Test(TestCase):
    ref = load_lgr('idn_table_review', 'reference_lgr.xml')
    report_oe = {
        'set_number': (111, 101),
        'idn_table': ((111, 101), (339,)),
        'ref_lgr': ((111, 101), (339,)),
        'relevant_idn_table_repertoire': ((111, 101), (339,)),
        'symmetry_check': True,
        'transitivity_check': True,
        'report': [
            {
                'source_cp': 'U+006F U+0065',
                'source_glyph': 'oe',
                'dest_cp': 'U+0153',
                'dest_glyph': 'œ',
                'fwd_type_idn': 'blocked',
                'fwd_type_ref': 'blocked',
                'reverse': True,
                'rev_type_idn': 'blocked',
                'rev_type_ref': 'blocked',
                'dest_in_idn': True,
                'dest_in_ref': True,
                'symmetric': True,
                'result_fwd': 'MATCH',
                'result_rev': 'MATCH',
                'remark_fwd': 'Exact match (including type, conditional variant rule)',
                'remark_rev': 'Exact match (including type, conditional variant rule)'
            }
        ]
    }

    def setUp(self) -> None:
        super().setUp()
        self.maxDiff = None

    def test_generate_variant_sets_report_exact_match(self):
        idn = load_lgr('idn_table_review/variant_sets', 'variant_sets_exact_match.xml')

        result = generate_variant_sets_report(idn, self.ref)

        self.assertCountEqual(result, [{
            'set_number': (97,),
            'idn_table': ((97,), (98,), (99,)),
            'ref_lgr': ((97,), (98,), (99,)),
            'relevant_idn_table_repertoire': ((97,), (98,), (99,)),
            'symmetry_check': True,
            'transitivity_check': True,
            'report': [
                {
                    'source_cp': 'U+0061',
                    'source_glyph': 'a',
                    'dest_cp': 'U+0062',
                    'dest_glyph': 'b',
                    'fwd_type_idn': 'blocked',
                    'fwd_type_ref': 'blocked',
                    'reverse': True,
                    'rev_type_idn': 'blocked',
                    'rev_type_ref': 'blocked',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': True,
                    'result_fwd': 'MATCH',
                    'result_rev': 'MATCH',
                    'remark_fwd': 'Exact match (including type, conditional variant rule)',
                    'remark_rev': 'Exact match (including type, conditional variant rule)'
                }, {
                    'source_cp': 'U+0061',
                    'source_glyph': 'a',
                    'dest_cp': 'U+0063',
                    'dest_glyph': 'c',
                    'fwd_type_idn': 'invalid',
                    'fwd_type_ref': 'invalid',
                    'reverse': True,
                    'rev_type_idn': 'blocked',
                    'rev_type_ref': 'blocked',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': False,
                    'result_fwd': 'MATCH',
                    'result_rev': 'MATCH',
                    'remark_fwd': 'Exact match (including type, conditional variant rule)',
                    'remark_rev': 'Exact match (including type, conditional variant rule)'
                }, {
                    'source_cp': 'U+0062',
                    'source_glyph': 'b',
                    'dest_cp': 'U+0063',
                    'dest_glyph': 'c',
                    'fwd_type_idn': 'blocked',
                    'fwd_type_ref': 'blocked',
                    'reverse': True,
                    'rev_type_idn': 'allocatable',
                    'rev_type_ref': 'allocatable',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': False,
                    'result_fwd': 'MATCH',
                    'result_rev': 'MATCH',
                    'remark_fwd': 'Exact match (including type, conditional variant rule)',
                    'remark_rev': 'Exact match (including type, conditional variant rule)'
                }
            ]
        }, self.report_oe])

    def test_generate_variant_sets_subset_match(self):
        idn = load_lgr('idn_table_review/variant_sets', 'variant_sets_subset_match.xml')

        result = generate_variant_sets_report(idn, self.ref)

        self.assertCountEqual(result, [{
            'set_number': (97,),
            'idn_table': ((97,), (98,)),
            'ref_lgr': ((97,), (98,), (99,)),
            'relevant_idn_table_repertoire': ((97,), (98,)),
            'symmetry_check': True,
            'transitivity_check': True,
            'report': [
                {
                    'source_cp': 'U+0061',
                    'source_glyph': 'a',
                    'dest_cp': 'U+0062',
                    'dest_glyph': 'b',
                    'fwd_type_idn': 'blocked',
                    'fwd_type_ref': 'blocked',
                    'reverse': True,
                    'rev_type_idn': 'blocked',
                    'rev_type_ref': 'blocked',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': True,
                    'result_fwd': 'MATCH',
                    'result_rev': 'MATCH',
                    'remark_fwd': 'Exact match (including type, conditional variant rule)',
                    'remark_rev': 'Exact match (including type, conditional variant rule)'
                }, {
                    'source_cp': 'U+0061',
                    'source_glyph': 'a',
                    'dest_cp': 'U+0063',
                    'dest_glyph': 'c',
                    'fwd_type_idn': '',
                    'fwd_type_ref': 'invalid',
                    'reverse': True,
                    'rev_type_idn': '',
                    'rev_type_ref': 'blocked',
                    'dest_in_idn': False,
                    'dest_in_ref': True,
                    'symmetric': False,
                    'result_fwd': 'NOTE',
                    'result_rev': 'NOTE',
                    'remark_fwd': 'Not applicable',
                    'remark_rev': 'Not applicable'
                }, {
                    'source_cp': 'U+0062',
                    'source_glyph': 'b',
                    'dest_cp': 'U+0063',
                    'dest_glyph': 'c',
                    'fwd_type_idn': '',
                    'fwd_type_ref': 'blocked',
                    'reverse': True,
                    'rev_type_idn': '',
                    'rev_type_ref': 'allocatable',
                    'dest_in_idn': False,
                    'dest_in_ref': True,
                    'symmetric': False,
                    'result_fwd': 'NOTE',
                    'result_rev': 'NOTE',
                    'remark_fwd': 'Not applicable',
                    'remark_rev': 'Not applicable'
                }
            ]
        }, self.report_oe])

    def test_generate_variant_sets_missing_variant_members(self):
        idn = load_lgr('idn_table_review/variant_sets', 'variant_sets_missing_variant_members.xml')

        result = generate_variant_sets_report(idn, self.ref)

        self.assertCountEqual(result, [{
            'set_number': (97,),
            'idn_table': ((97,), (98,)),
            'ref_lgr': ((97,), (98,), (99,)),
            'relevant_idn_table_repertoire': ((97,), (98,), (99,)),
            'symmetry_check': True,
            'transitivity_check': True,
            'report': [
                {
                    'source_cp': 'U+0061',
                    'source_glyph': 'a',
                    'dest_cp': 'U+0062',
                    'dest_glyph': 'b',
                    'fwd_type_idn': 'blocked',
                    'fwd_type_ref': 'blocked',
                    'reverse': True,
                    'rev_type_idn': 'blocked',
                    'rev_type_ref': 'blocked',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': True,
                    'result_fwd': 'MATCH',
                    'result_rev': 'MATCH',
                    'remark_fwd': 'Exact match (including type, conditional variant rule)',
                    'remark_rev': 'Exact match (including type, conditional variant rule)'
                }, {
                    'source_cp': 'U+0061',
                    'source_glyph': 'a',
                    'dest_cp': 'U+0063',
                    'dest_glyph': 'c',
                    'fwd_type_idn': '',
                    'fwd_type_ref': 'invalid',
                    'reverse': True,
                    'rev_type_idn': '',
                    'rev_type_ref': 'blocked',
                    'dest_in_idn': False,
                    'dest_in_ref': True,
                    'symmetric': False,
                    'result_fwd': 'REVIEW',
                    'result_rev': 'REVIEW',
                    'remark_fwd': 'Variant member exists in the reference LGR',
                    'remark_rev': 'Variant member exists in the reference LGR'
                }, {
                    'source_cp': 'U+0062',
                    'source_glyph': 'b',
                    'dest_cp': 'U+0063',
                    'dest_glyph': 'c',
                    'fwd_type_idn': '',
                    'fwd_type_ref': 'blocked',
                    'reverse': True,
                    'rev_type_idn': '',
                    'rev_type_ref': 'allocatable',
                    'dest_in_idn': False,
                    'dest_in_ref': True,
                    'symmetric': False,
                    'result_fwd': 'REVIEW',
                    'result_rev': 'REVIEW',
                    'remark_fwd': 'Variant member exists in the reference LGR',
                    'remark_rev': 'Variant member exists in the reference LGR'
                }
            ]
        }, self.report_oe])

    def test_generate_variant_sets_report_mismatch_contextual_rule_idn_table_less_conservative(self):
        idn = load_lgr('idn_table_review/variant_sets',
                       'variant_sets_mismatch_contextual_rule_idn_table_less_conservative.xml')

        result = generate_variant_sets_report(idn, self.ref)

        self.assertCountEqual(result, [{
            'set_number': (97,),
            'idn_table': ((97,), (98,), (99,)),
            'ref_lgr': ((97,), (98,), (99,)),
            'relevant_idn_table_repertoire': ((97,), (98,), (99,)),
            'symmetry_check': True,
            'transitivity_check': True,
            'report': [
                {
                    'source_cp': 'U+0061',
                    'source_glyph': 'a',
                    'dest_cp': 'U+0062',
                    'dest_glyph': 'b',
                    'fwd_type_idn': 'blocked',
                    'fwd_type_ref': 'blocked',
                    'reverse': True,
                    'rev_type_idn': 'blocked',
                    'rev_type_ref': 'blocked',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': True,
                    'result_fwd': 'REVIEW',
                    'result_rev': 'MATCH',
                    'remark_fwd': 'IDN Table variant generation is less conservative as it only applies with some conditions',
                    'remark_rev': 'Exact match (including type, conditional variant rule)'
                }, {
                    'source_cp': 'U+0061',
                    'source_glyph': 'a',
                    'dest_cp': 'U+0063',
                    'dest_glyph': 'c',
                    'fwd_type_idn': 'invalid',
                    'fwd_type_ref': 'invalid',
                    'reverse': True,
                    'rev_type_idn': 'blocked',
                    'rev_type_ref': 'blocked',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': False,
                    'result_fwd': 'MATCH',
                    'result_rev': 'MATCH',
                    'remark_fwd': 'Exact match (including type, conditional variant rule)',
                    'remark_rev': 'Exact match (including type, conditional variant rule)'
                }, {
                    'source_cp': 'U+0062',
                    'source_glyph': 'b',
                    'dest_cp': 'U+0063',
                    'dest_glyph': 'c',
                    'fwd_type_idn': 'blocked',
                    'fwd_type_ref': 'blocked',
                    'reverse': True,
                    'rev_type_idn': 'allocatable',
                    'rev_type_ref': 'allocatable',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': False,
                    'result_fwd': 'MATCH',
                    'result_rev': 'MATCH',
                    'remark_fwd': 'Exact match (including type, conditional variant rule)',
                    'remark_rev': 'Exact match (including type, conditional variant rule)'
                }
            ]
        }, self.report_oe])

    def test_generate_variant_sets_report_mismatch_contextual_rule_idn_table_more_conservative(self):
        idn = load_lgr('idn_table_review/variant_sets',
                       'variant_sets_mismatch_contextual_rule_idn_table_more_conservative.xml')

        result = generate_variant_sets_report(idn, self.ref)

        self.assertCountEqual(result, [{
            'set_number': (97,),
            'idn_table': ((97,), (98,), (99,)),
            'ref_lgr': ((97,), (98,), (99,)),
            'relevant_idn_table_repertoire': ((97,), (98,), (99,)),
            'symmetry_check': True,
            'transitivity_check': True,
            'report': [
                {
                    'source_cp': 'U+0061',
                    'source_glyph': 'a',
                    'dest_cp': 'U+0062',
                    'dest_glyph': 'b',
                    'fwd_type_idn': 'blocked',
                    'fwd_type_ref': 'blocked',
                    'reverse': True,
                    'rev_type_idn': 'blocked',
                    'rev_type_ref': 'blocked',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': True,
                    'result_fwd': 'MATCH',
                    'result_rev': 'MANUAL CHECK',
                    'remark_fwd': 'Exact match (including type, conditional variant rule)',
                    'remark_rev': 'Variant condition rules are mismatched. The IDN Table misses the rule. '
                                  'If the rule is not needed for the proper variant index calculation, then this is ok'
                }, {
                    'source_cp': 'U+0061',
                    'source_glyph': 'a',
                    'dest_cp': 'U+0063',
                    'dest_glyph': 'c',
                    'fwd_type_idn': 'invalid',
                    'fwd_type_ref': 'invalid',
                    'reverse': True,
                    'rev_type_idn': 'blocked',
                    'rev_type_ref': 'blocked',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': False,
                    'result_fwd': 'MATCH',
                    'result_rev': 'MATCH',
                    'remark_fwd': 'Exact match (including type, conditional variant rule)',
                    'remark_rev': 'Exact match (including type, conditional variant rule)'
                }, {
                    'source_cp': 'U+0062',
                    'source_glyph': 'b',
                    'dest_cp': 'U+0063',
                    'dest_glyph': 'c',
                    'fwd_type_idn': 'blocked',
                    'fwd_type_ref': 'blocked',
                    'reverse': True,
                    'rev_type_idn': 'allocatable',
                    'rev_type_ref': 'allocatable',
                    'dest_in_idn': True,
                    'dest_in_ref': True,
                    'symmetric': False,
                    'result_fwd': 'MATCH',
                    'result_rev': 'MATCH',
                    'remark_fwd': 'Exact match (including type, conditional variant rule)',
                    'remark_rev': 'Exact match (including type, conditional variant rule)'
                }
            ]
        }, self.report_oe])