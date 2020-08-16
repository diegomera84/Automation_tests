class RobotFrameworkUtilities(object):

    def should_be_less_than(self, number1, number2):
        """
        Validates that the first value given is less than the second value.
        :param: number1  number that should be less
        :param: number2  number that should be greater
        :return: boolean value
        """
        result = number1 < int(number2)
        return result

    def insert_test_comment(self):
        """
        wait for comments on the test
        :return: text entered by the user
        """
        answer = input()
        return answer.capitalize()
