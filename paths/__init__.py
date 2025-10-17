from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_PATH = PROJECT_ROOT / 'reddit'
OUTPUT_PATH = PROJECT_ROOT / 'reddit_processed'

__all__ = [
    'PROJECT_ROOT',
    'DATA_PATH',
    'OUTPUT_PATH'
]