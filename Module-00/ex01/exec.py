import sys

if __name__ == "__main__":
    # Due to the arguments are showed like a list.
    # It must be joined in one string
    if (len(sys.argv) > 1):
        joint_strings = " ".join(sys.argv[1:])

        rev_joint_strs = []
        rev_joint_strs = joint_strings[::-1]

        # Create another list to change the characters
        modified_rev_strs = []

        for character in rev_joint_strs:
            modified_rev_strs.append(character.swapcase())

        # Since it is a list. It must be joined in one string
        modified_rev_strs = "".join(modified_rev_strs)

        print(modified_rev_strs)
