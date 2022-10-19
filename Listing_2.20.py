>>> soliloquy = "To be, or not to be, that is the question:"  # Just a reminder
>>> "To be" in soliloquy        # Does it include the substring "To be"?
True
>>> "question" in soliloquy     # What about "question"?
True
>>> "nonexistent" in soliloquy  # This string doesn't appear.
False
>>> "TO BE" in soliloquy        # String inclusion is case-sensitive.
False
