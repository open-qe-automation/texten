import os
import sys
import json
import pytest
import tempfile
import shutil

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config_manager import ConfigManager
from app import (
    calculate_file_hash,
    find_pii,
    is_excluded,
    is_startswith_excluded,
    load_hashes,
    save_hashes
)


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


class TestConfigManager:
    def test_load_config(self):
        cm = ConfigManager()
        assert cm.config is not None
        assert 'patterns' in cm.config

    def test_pii_ok_list(self):
        cm = ConfigManager()
        assert cm.pii_ok is not None

    def test_exclusions(self):
        cm = ConfigManager()
        assert cm.exclusions is not None


class TestFileHash:
    def test_calculate_file_hash(self):
        test_file = os.path.join(FIXTURES_DIR, 'sample.txt')
        if os.path.exists(test_file):
            result = calculate_file_hash(test_file)
            assert isinstance(result, str)
            assert len(result) == 64

    def test_calculate_nonexistent_file(self):
        result = calculate_file_hash('/nonexistent/file.txt')
        assert result is None


class TestPIIDetection:
    def test_find_credit_card(self):
        patterns = {
            'credit_card_numbers': r"\b(?:\d{4}[ -]?){3}\d{4}\b"
        }
        text = "My card is 1234-5678-9012-3456"
        result = find_pii(text, patterns)
        assert 'credit_card_numbers' in result
        assert '1234-5678-9012-3456' in result['credit_card_numbers']

    def test_find_ssn(self):
        patterns = {
            'social_security_numbers': r"\b\d{3}-\d{2}-\d{4}\b"
        }
        text = "My SSN is 123-45-6789"
        result = find_pii(text, patterns)
        assert 'social_security_numbers' in result

    def test_no_pii_found(self):
        patterns = {
            'credit_card_numbers': r"\b(?:\d{4}[ -]?){3}\d{4}\b"
        }
        text = "This is a clean text without PII"
        result = find_pii(text, patterns)
        assert len(result) == 0


class TestExclusions:
    def test_is_excluded_pattern(self):
        exclusions = ['*.tmp', '*.log']
        assert is_excluded('test.tmp', exclusions) is True
        assert is_excluded('test.log', exclusions) is True

    def test_not_excluded(self):
        exclusions = ['*.tmp', '*.log']
        assert is_excluded('test.txt', exclusions) is False

    def test_is_startswith_excluded(self):
        assert is_startswith_excluded('~$temp.docx') is True
        assert is_startswith_excluded('.hidden.txt') is True
        assert is_startswith_excluded('normal.txt') is False


class TestHashStorage:
    def test_save_and_load_hashes(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_file = f.name
        
        try:
            hashes = {'file1.txt': 'abc123', 'file2.txt': 'def456'}
            save_hashes(temp_file, hashes)
            loaded = load_hashes(temp_file)
            assert loaded == hashes
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

    def test_load_nonexistent(self):
        result = load_hashes('/nonexistent/file.json')
        assert result == {}


if __name__ == '__main__':
    pytest.main([__file__, '-v'])