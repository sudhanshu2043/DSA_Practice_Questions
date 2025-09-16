class Solution:
    def compress(self, chars: List[str]) -> int:
        write_ptr = 0
        # read_ptr iterates through the input list to find groups of characters.
        read_ptr = 0
        n = len(chars)
        while read_ptr < n:
            current_char = chars[read_ptr]
            count = 0
            # Count consecutive occurrences of the current character
            while read_ptr < n and chars[read_ptr] == current_char:
                read_ptr += 1
                count += 1
            # 1. Write the character
            chars[write_ptr] = current_char
            write_ptr += 1
            # 2. Write the count if it's greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write_ptr] = digit
                    write_ptr += 1
        return write_ptr