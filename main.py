import abjad
import random
import time

time_between_changes = 30  # in seconds
num_of_changes = 6
counter = 1

while 0 <= counter <= num_of_changes:
    # Maj [0, 2, 4, 5, 7, 9, 8]
    # #creates random rhythm
    def rhythm(num_of_rhythms):
        duration = []
        amount_of_notes = [4, 8]
        note_length = [16]
        for i in range(num_of_rhythms):
            duration.append((random.choice(amount_of_notes), random.choice(note_length)))
        return duration

        # creates random short notes


    def short_notes(number_of_notes):
        pitches = [2]
        dim_scale = [2, 4, 5, 7, 8, 10, 11]
        for n in range(number_of_notes):
            pitches.append(random.choice(dim_scale))
            """for _ in range(3):
                new_pitches = [pitch + 2 for pitch in pitches[-4:]]
                pitches.extend(new_pitches)"""
        return pitches

        # creates random long notes


    def long_notes(number_of_notes):
        pitches = []
        dim_scale = [2, 4, 5, 7, 8, 10, 11]
        for n in range(number_of_notes):
            pitches.append(random.choice(dim_scale))
            """for _ in range(3):
                new_pitches = [pitch + 2 for pitch in pitches[-4:]]
                pitches.extend(new_pitches)"""
        return pitches

        # creates rhythm notes


    def rhythm_notes(number_of_notes):
        pitches = []
        dim_scale = [2, 4, 5, 7, 8, 10, 11]
        for n in range(number_of_notes):
            pitches.append(random.choice(dim_scale))

        return pitches


    short_pitches = short_notes(random.randrange(4, 8, 2))
    short_duration = rhythm(5)
    print(short_duration)

    short_pitches2 = short_notes(15)
    long_dur_list = [(8, 16), (4, 16), (8, 16), (2, 16), (1, 16), (random.randint(1, 2), 16)]
    short_duration2 = random.choice(long_dur_list)
    # reverses the pitches
    reversed_pitches = short_pitches[::-1]

    long_pitches = long_notes(1)
    long_duration = [(1, 1)]
    long_pitches2 = long_notes(3)
    long_duration2 = [(1, 1)]

    rhythm_pitches = rhythm_notes(1)
    rhythm_duration = [(1, 16), (random.randint(1, 2), 16), (random.randint(1, 2), 16), (1, 16), (1, 16),
                       (random.randint(1, 2), 16)]

    maker = abjad.LeafMaker()
    # create  staves and score
    short_leaves = maker(short_pitches, short_duration)
    short_voice = abjad.Voice(short_leaves)
    short_staff = abjad.Staff([short_voice], name="Instrument 1")

    short_leaves2 = maker(short_pitches2, short_duration2)
    short_voice2 = abjad.Voice(short_leaves2)
    short_staff2 = abjad.Staff([short_voice2], name="Instrument 2")

    reversed_leaves = maker(reversed_pitches, short_duration)
    reversed_voice = abjad.Voice(reversed_leaves)
    reversed_staff = abjad.Staff([reversed_voice], name="Instrument 3")

    long_leaves = maker(long_pitches, long_duration)
    long_voice = abjad.Voice(long_leaves)
    long_staff = abjad.Staff([long_voice], name="Instrument 4")
    long_leaves2 = maker(long_pitches2, long_duration2)
    long_voice2 = abjad.Voice(long_leaves2)
    long_staff2 = abjad.Staff([long_voice2], name="Instrument 5")

    rhythm_leaves = maker(rhythm_pitches, rhythm_duration)
    rhythm_voice = abjad.Voice(rhythm_leaves)
    rhythm_staff = abjad.Staff([rhythm_voice], name="Instrument 6")

    staff_names = [short_staff, long_staff, reversed_staff, rhythm_staff, short_staff2, long_staff2]
    staff_names_shuffled = random.sample(staff_names, len(staff_names))

    main_staff = abjad.StaffGroup(lilypond_type="Staff", name="Main_Staff")
    main_staff.extend(staff_names_shuffled)

    score = abjad.Score([main_staff], name="Score")

    abjad.show(score)

    counter += 1
    time.sleep(time_between_changes)