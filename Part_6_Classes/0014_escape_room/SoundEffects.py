class SoundEffects:
    """
    Base class to represent a generic collection of sound effects
    """

    def __init__(self, volume=None):
        """
        Attrs:
            volume: int
        """
        self.volume = volume
