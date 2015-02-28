import sys

if sys.version_info >= (3, ):
    def u(s):
        return s
else:
    def u(s):
        return unicode(s.replace(r'\\', r'\\\\'), "unicode_escape")
