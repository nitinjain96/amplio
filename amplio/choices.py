USER_POST_CHOICES = (
    (0, 'Student'),
    (1, 'IMG developer'),
    (2, 'IMG designer'),
    (3, 'IIT official'),
)

FEEDBACK_TYPE_CHOICES = (
    (0, 'Suggestions for improving existing apps'),
    (1, 'Bugs that need to be eliminated rapidly'),
    (2, 'Glitches that need to be eliminated casually'),
    (3, 'Ideas for building new apps'),
)

FEEDBACK_TO_CHOICES = (
    (0, 'All concerned'),
    (1, 'Developers only'),
    (2, 'Designers only'),
)

FEEDBACK_CATEGORY_CHOICES = (
    (0, 'No specific category or miscellaneous'),
    (1, 'IIT Roorkee website'),
    (2, 'IMG website'),
    (3, 'New entrants'),
    (4, 'Channel-i'),
    (5, 'Notice board'),
    (6, 'Lectures and tutorials'),
    (7, 'Lost and found'),
    (8, 'Buy and sell'),
    (9, 'People search'),
    (10, 'Jukebox'),
    (11, 'Kriti'),
    (12, 'Yaadein'),
    (13, 'Projects portal'),
    (14, 'Internship portal'),
    (15, 'Placement portal'),
    (16, 'Student home-page'),
    (17, 'DC++ hub'),
    (18, 'Bunk-o-meter Android app'),
    (19, 'Notice board Android app'),
    (20, 'Forum'),
    (21, 'FAQ'),
    (22, 'Media management system'),
    (23, 'Forminator'),
    (24, 'Status'),
)

FEEDBACK_STATUS_CHOICES = {
    {0: 'Reported'},
    {1: 'Under consideration'},
    {2: 'Under construction'},
    {3: 'Undergoing tests'},
    {4: 'Completed'},
}

COMMENT_UPON_CHOICES = (
    (0, 'Comment on feedback'),
    (1, 'Comment on comment'),
)