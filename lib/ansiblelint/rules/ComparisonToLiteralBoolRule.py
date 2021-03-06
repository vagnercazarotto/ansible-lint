# Copyright (c) 2016, Will Thames and contributors
# Copyright (c) 2018, Ansible Project

from ansiblelint import AnsibleLintRule
import re


class ComparisonToLiteralBoolRule(AnsibleLintRule):
    id = '601'
    shortdesc = "Don't compare to literal True/False"
    description = (
        'Use ``when: var`` rather than ``when: var == True`` '
        '(or conversely ``when: not var``)'
    )
    tags = ['idiom']
    version_added = 'v4.0.0'

    literal_bool_compare = re.compile("[=!]= ?(True|true|False|false)")

    def match(self, file, line):
        return self.literal_bool_compare.search(line)
