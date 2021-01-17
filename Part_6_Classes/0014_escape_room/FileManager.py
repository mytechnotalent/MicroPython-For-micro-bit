class FileManager:
    """
    Class to implement micro:bit file access to store inventory if
    power lost or reset to maintain persistence
    """

    @staticmethod
    def write_inventory_file():
        """
        Write 'Red Key' to inventory file upon picking it up
        """
        try:
            with open('inventory', 'w') as file:
                file.write('Red Key')
        except OSError:
            pass

    @staticmethod
    def read_inventory_file():
        """
        Read inventory file and return its contents

        Return:
            str
        """
        try:
            with open('inventory', 'r') as file:
                inventory = file.read()
                return inventory
        except OSError:
            pass

    @staticmethod
    def clear_inventory_file():
        """
        Clear inventory file after winning a game
        """
        try:
            with open('inventory', 'w') as file:
                file.write('')
        except OSError:
            pass
