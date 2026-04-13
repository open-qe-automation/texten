import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from msuliot.base_64 import Base64
except ImportError:
    pytest.skip("package.utils not installed", allowmodule_level=True)


class TestBase64:
    def test_encode(self):
        result = Base64.encode("test/path/file.txt")
        assert isinstance(result, str)

    def test_encode_decode_roundtrip(self):
        original = "test/path/file.txt"
        encoded = Base64.encode(original)
        decoded = Base64.decode(encoded)
        assert decoded == original


if __name__ == '__main__':
    pytest.main([__file__, '-v'])