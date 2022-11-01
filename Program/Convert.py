from Program import Message

# Converts the input to a valid location (a1 -> [0,0])
class LocationConvert:
    def __init__(self, value):
        """Convert a letter and a number, to a position array

        Args:
            value (str): The position to translate
        """
        self.input:str = value
        self.letters:str = ""
        self.y:str = ""

    # Thanks to Guy_732
    # changes letter to number based in the alphabet
    def _decode(self, s: str) -> int:
        s = s.lower()
        ref = ord('a') - 1
        v = 0
        exp = 1
        for c in reversed(s):
            v += (ord(c) - ref) * exp
            exp *= 26

        return v

    def Convert(self):
        """Main convert function

        Returns:
            Tuple: The cooridnate position
        """
        if len(self.input) >= 2:
            # lower input
            self.input = self.input.lower().strip()
            
            # splits the input into numbers and letters
            for v in self.input:
                if v.isdigit():
                    self.y += v
                else:
                    self.letters += v
            
            # Checks if there is at least 1 character that is not a letter
            if self.letters == self.input:
                Message.clear(1, "Must be at least two digits, a letter (x) and a number (y)")  # noqa
                return None, None

            # convert letters into numbers
            return self._decode(self.letters) - 1, (int(self.y) - 1)
        
        # Not enough characters
        Message.clear(1, "Must be at least two digits, a letter (x) and a number (y)")  # noqa
        return None, None

if __name__ == "__main__":
    data = LocationConvert("A3").Convert()
    print(data)