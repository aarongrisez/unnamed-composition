# EchoChambers/train.py

"""
This is the entrypoint of the training script for the EchoChambers neural net.
The procedure is outlined below:

First Run:
    1. Generate monophony from Magenta's pretrained dataset.
        Defaults:
            a. 1000 melodies
            b. 1024 steps
    2. Pull latest tweets for a random trending hashtag.
    3. Associate each tweet with a melody from the generated monophonies in an
       extended note sequence.
        Model: Represent the tweet as noise and convolve the midi signal with
        the noise signal
            a. This step requires first representing the midi signal as a
            time-domain signal.
            b. The tweet representation is as follows:
                -Each possible position for a character in a tweet is a cell in
                the time-domain signal. Signal length is preserved by the
                length of the tweet
                -Pitch, velocity, and duration are derived from the character's
                unicode
                -The entire tweet amplitude is renormalized to the number of
                followers that user has relative to the most followed user at
                that time
        ToDo: Figure out how to incorporate NLP libraries to generate text to
        accompany melodic content
    4. Construct next training dataset

Next Runs:
    1. Use previous training dataset.
    2-4. Same

Continue this process any number of times.
"""
