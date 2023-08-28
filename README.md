# discordbot-pronouns
Discord bot for pronoun role assignment, adding user-defined pronoun sets, & substitution of pronouns within messages.

Current capabilities (as a Python console app):
1) Addition of user-defined pronoun sets.
2) Substitution of one set of pronouns to another within a message.
3) Matching case and punctuation between original and new messages, including:
   a) ALL CAPS
   b) Start Of Word Only
   c) mIxEd CaSE
4) Assigning existing pronoun set(s) to yourself.
5) Searching pronoun use by username.

Future plans:
1) Create listener for Discord events.
2) Allow users to choose their pronouns as a reaction to a roles message & update roles message to include user-added pronoun sets.
3) Assign server roles based on self-assigned pronoun sets.
4) Implement message pronoun substitution into a slash command.
5) Choose user to grab pronouns from for message substitution. Currently you must supply the pronouns to swap to and from.
6) Allow for message substitution to swap between pronoun sets for users with multiple pronouns listed.
