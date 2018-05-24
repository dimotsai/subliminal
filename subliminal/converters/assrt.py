# -*- coding: utf-8 -*-
from babelfish import LanguageReverseConverter

from ..exceptions import ConfigurationError


class AssrtConverter(LanguageReverseConverter):
    def __init__(self):
        self.from_assrt = { u'简体': ('zho', 'CN'), u'繁体': ('zho', 'TW'),
                            u'簡體': ('zho', 'CN'), u'繁體': ('zho', 'TW'),
                            u'英文': ('eng',),
                            u'chs': ('zho', 'CN'), u'cht': ('zho', 'TW'),
                            u'chn': ('zho', 'CN'), u'twn': ('zho', 'TW')}
        self.to_assrt = { ('zho', 'CN'): u'chs', ('zho', 'TW'): u'cht', ('eng',) : u'eng' }
        self.codes = set(self.from_assrt.keys())

    def convert(self, alpha3, country=None, script=None):
        if (alpha3, country) in self.to_assrt:
            return self.to_assrt[(alpha3, country)]

        raise ConfigurationError('Unsupported language for assrt: %s, %s, %s' % (alpha3, country, script))

    def reverse(self, assrt):
        if assrt in self.from_assrt:
            return self.from_assrt[assrt]

        raise ConfigurationError('Unsupported language code for assrt: %s' % assrt)


