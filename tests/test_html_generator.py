
import pytest
from modules import html_generator

def test_markdown_conversion():
    """Test standard markdown conversion"""
    text = "**Bold** and *Italic*"
    html = html_generator.convert_to_markdown(text)
    assert "<strong>Bold</strong>" in html
    assert "<em>Italic</em>" in html

def test_latex_conversion():
    """Test LaTeX conversion"""
    text = "$E=mc^2$"
    html = html_generator.convert_to_markdown(text)
    # The output format might vary depending on extension versions, but basic checking
    assert "E=mc^2" in html

def test_thinking_block_extraction():
    """Test extraction of <think> blocks"""
    text = "<think>Exploring the universe...</think>Hello world!"
    thought, content = html_generator.extract_thinking_block(text)
    assert thought == "<think>Exploring the universe...</think>"
    assert content == "Hello world!"
