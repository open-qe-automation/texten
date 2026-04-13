import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from msuliot.docx_loader import DocxLoader
from msuliot.pdf_loader import PdfLoader
from msuliot.xlsx_loader import XlsxLoader
from msuliot.csv_loader import CsvLoader
from msuliot.pptx_loader import PptxLoader
from msuliot.html_loader import HtmlLoader
from msuliot.data_loader_manager import DataLoaderManager


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


class TestDataLoaderManager:
    def test_get_supported_loaders(self):
        dlm = DataLoaderManager()
        loaders = dlm.get_supported_data_loaders()
        assert 'docx' in loaders
        assert 'pdf' in loaders
        assert 'xlsx' in loaders
        assert 'csv' in loaders
        assert 'pptx' in loaders
        assert 'html' in loaders

    def test_load_data_unsupported_type(self):
        dlm = DataLoaderManager()
        with pytest.raises(ValueError):
            dlm.load_data('test.xyz', 'xyz')


class TestDocxLoader:
    def test_load_data(self):
        loader = DocxLoader()
        test_file = os.path.join(FIXTURES_DIR, 'sample.docx')
        if os.path.exists(test_file):
            result = loader.load_data(test_file)
            assert isinstance(result, str)
            assert len(result) > 0


class TestPdfLoader:
    def test_load_data(self):
        loader = PdfLoader()
        test_file = os.path.join(FIXTURES_DIR, 'sample.pdf')
        if os.path.exists(test_file):
            result = loader.load_data(test_file)
            assert isinstance(result, str)


class TestXlsxLoader:
    def test_load_data(self):
        loader = XlsxLoader()
        test_file = os.path.join(FIXTURES_DIR, 'sample.xlsx')
        if os.path.exists(test_file):
            result = loader.load_data(test_file)
            assert isinstance(result, str)


class TestCsvLoader:
    def test_load_data(self):
        loader = CsvLoader()
        test_file = os.path.join(FIXTURES_DIR, 'sample.csv')
        if os.path.exists(test_file):
            result = loader.load_data(test_file)
            assert isinstance(result, str)
            assert 'John Doe' in result


class TestPptxLoader:
    def test_load_data(self):
        loader = PptxLoader()
        test_file = os.path.join(FIXTURES_DIR, 'sample.pptx')
        if os.path.exists(test_file):
            result = loader.load_data(test_file)
            assert isinstance(result, str)


class TestHtmlLoader:
    def test_load_data(self):
        loader = HtmlLoader()
        test_file = os.path.join(FIXTURES_DIR, 'sample.html')
        if os.path.exists(test_file):
            result = loader.load_data(test_file)
            assert isinstance(result, str)
            assert 'Test Document' in result


if __name__ == '__main__':
    pytest.main([__file__, '-v'])