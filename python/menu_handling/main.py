"""Provides application point of entry."""

from ui import Ui

def main():
    """Provide application point of entry."""
    user_interface = Ui()
    user_interface.start()


if __name__ == "__main__":
    main()