"""Storage manager for xhs-toolkit."""
import json
import os
from pathlib import Path


_storage_manager_instance = None


def get_storage_manager(data_dir=None):
    """Get or create storage manager singleton.
    
    Args:
        data_dir: Directory for storing data files
        
    Returns:
        StorageManager instance
    """
    global _storage_manager_instance
    if _storage_manager_instance is None:
        _storage_manager_instance = StorageManager(data_dir)
    return _storage_manager_instance


class StorageManager:
    """Manages data storage for xhs-toolkit."""
    
    def __init__(self, data_dir=None):
        """Initialize storage manager.
        
        Args:
            data_dir: Directory for storing data files
        """
        if data_dir is None:
            data_dir = os.environ.get('XHS_DATA_DIR', os.path.expanduser('~/.openclaw/credentials'))
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def get_cookies_path(self):
        """Get path to cookies file."""
        return self.data_dir / 'xhs_cookies.json'
    
    def save_cookies(self, cookies):
        """Save cookies to file.
        
        Args:
            cookies: Dictionary of cookies
        """
        cookies_path = self.get_cookies_path()
        with open(cookies_path, 'w', encoding='utf-8') as f:
            json.dump(cookies, f, ensure_ascii=False, indent=2)
    
    def load_cookies(self):
        """Load cookies from file.
        
        Returns:
            Dictionary of cookies or None if not found
        """
        cookies_path = self.get_cookies_path()
        if not cookies_path.exists():
            return None
        with open(cookies_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def clear_cookies(self):
        """Clear saved cookies."""
        cookies_path = self.get_cookies_path()
        if cookies_path.exists():
            cookies_path.unlink()