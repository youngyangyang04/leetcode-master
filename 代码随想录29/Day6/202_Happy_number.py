class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()

        while True:
            # Update the value of n by calling the get_sum function
            n = self.get_sum(n)

            # Check if the updated value of n is 1, indicating a happy number
            if n == 1:
                return True

            # Check if the updated value of n has been seen before, indicating a cycle
            if n in record:
                return False
            else:
                # Add the updated value of n to the record set
                record.add(n)

    # get_sum function to compute the sum of the squares of the digits of a number
    def get_sum(self, n: int) -> int:
        # Initialize a variable to store the sum
        new_num = 0

        # Loop through each digit of the number
        while n:
            # divmod(n, 10) returns a tuple (quotient, remainder)
            # Extract the last digit (remainder) and update n to be the quotient
            n, r = divmod(n, 10)

            # Add the square of the current digit to the sum
            new_num += r**2

        # Return the computed sum
        return new_num
