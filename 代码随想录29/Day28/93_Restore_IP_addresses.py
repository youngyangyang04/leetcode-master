class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtracking(s, 0, 0, "", result)
        return result

    def backtracking(self, s, startIndex, pointNum, current, result):
        # Check if we have placed three dots (representing four segments in an IP address)
        if pointNum == 3:
            # Check if the remaining segment is valid
            if self.is_valid(s, startIndex, len(s) - 1):
                current += s[startIndex:]
                result.append(current)
            return

        # Iterate through the string
        for i in range(startIndex, len(s)):
            # Check if the current segment is valid
            if self.is_valid(s, startIndex, i):
                sub = s[startIndex : i + 1]
                # Recursively call the backtracking function for the next segment
                self.backtracking(s, i + 1, pointNum + 1, current + sub + ".", result)
            else:
                # Break the loop if the current segment is not valid
                break

    def is_valid(self, s: str, start: int, end: int):
        # Check if the segment is not empty
        if start > end:
            return False
        # Check for leading zeros
        if s[start] == "0" and start != end:
            return False
        num = 0
        # Convert the segment to a number and check if it is within the valid range (0-255)
        for i in range(start, end + 1):
            if not s[i].isdigit():
                return False
            num = num * 10 + int(s[i])
            if num > 255:
                return False
        return True
