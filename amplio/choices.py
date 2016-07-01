from amplio import choice_constants

USER_POST_CHOICES = (
    (choice_constants.STUDENT, 'Student'),
    (choice_constants.IMG_DEVELOPER, 'IMG developer'),
    (choice_constants.IMG_DESIGNER, 'IMG designer'),
    (choice_constants.IIT_OFFICIAL, 'IIT official'),
)

FEEDBACK_TYPE_CHOICES = (
    (choice_constants.NOT_SURE, 'Not really sure'),
    (choice_constants.SUGGESTIONS, 'Suggestions for improving existing apps'),
    (choice_constants.BUGS, 'Bugs that need to be eliminated rapidly'),
    (choice_constants.GLITCHES, 'Glitches that need to be eliminated casually'),
    (choice_constants.IDEAS, 'Ideas for building new apps'),
)

FEEDBACK_TO_CHOICES = (
    (choice_constants.IMG, 'IMG developers and designers'),
    (choice_constants.IMG_DEVELOPER, 'IMG developers'),
    (choice_constants.IMG_DESIGNER, 'IMG designers'),
    (choice_constants.IIT_OFFICIAL, 'IIT officials')
)

FEEDBACK_CATEGORY_CHOICES = (
    (choice_constants.NO_SPECIFIC_CATEGORY, 'No specific category or miscellaneous'),
    (choice_constants.IIT_ROORKEE_WEBSITE, 'IIT Roorkee website'),
    (choice_constants.IMG_WEBSITE, 'IMG website'),
    (choice_constants.NEW_ENTRANTS, 'New entrants'),
    (choice_constants.CHANNEL_I, 'Channel-i'),
    (choice_constants.NOTICE_BOARD, 'Notice board'),
    (choice_constants.LECTURES_AND_TUTORIALS, 'Lectures and tutorials'),
    (choice_constants.LOST_AND_FOUND, 'Lost and found'),
    (choice_constants.BUY_AND_SELL, 'Buy and sell'),
    (choice_constants.PEOPLE_SEARCH, 'People search'),
    (choice_constants.JUKEBOX, 'Jukebox'),
    (choice_constants.KRITI, 'Kriti'),
    (choice_constants.YAADEIN, 'Yaadein'),
    (choice_constants.PROJECTS_PORTAL, 'Projects portal'),
    (choice_constants.INTERNSHIP_PORTAL, 'Internship portal'),
    (choice_constants.PLACEMENTS_PORTAL, 'Placement portal'),
    (choice_constants.STUDENT_HOMEPAGE, 'Student homepage'),
    (choice_constants.DC_HUB, 'DC++ hub'),
    (choice_constants.BUNK_O_METER, 'Bunk-o-meter Android app'),
    (choice_constants.NOTICE_BOARD_APP, 'Notice board Android app'),
    (choice_constants.FORUM, 'Forum'),
    (choice_constants.FAQ, 'FAQ'),
    (choice_constants.MEDIA_MANAGEMENT_SYSTEM, 'Media management system'),
    (choice_constants.FORMINATOR, 'Forminator'),
    (choice_constants.STATUS, 'Status'),
)

FEEDBACK_STATUS_CHOICES = (
    (choice_constants.REPORTED, 'Reported'),
    (choice_constants.UNDER_CONSIDERATION, 'Under consideration'),
    (choice_constants.UNDER_CONSTRUCTION, 'Under construction'),
    (choice_constants.UNDER_TESTING, 'Under testing'),
    (choice_constants.COMPLETED, 'Completed'),
)
