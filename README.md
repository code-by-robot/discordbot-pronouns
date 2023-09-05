# discordbot-pronouns
Discord bot for pronoun role assignment, adding user-defined pronoun sets, & substitution of pronouns within messages.

Current capabilities - now as a Discord bot:
1) Substitution of one set of pronouns to another within a message.
2) Matching case and punctuation between original and new messages, including:
   a) ALL CAPS
   b) Start Of Word Only
   c) mIxEd CaSE

![image](https://github.com/code-by-robot/discordbot-pronouns/assets/96454399/2547a707-3029-4f12-8072-961278a70318)

The above shows the original message and bot message. The bot will delete the original message - it was kept to show format of input required for the bot.

3) Completes setup functions:
   a) Creates roles channel if it doesn't exist.
   b) Sends roles message with default pronoun sets.
4) Allows for user-defined pronoun sets & updates roles message accordingly.

![image](https://github.com/code-by-robot/discordbot-pronouns/assets/96454399/f396c151-8705-46db-bcb4-3b5d85b1cd2e)

Roles message (updated) & command to update message shown above. This will be prettier soon.


Future plans:
1) Tie roles to reactions to roles message.
2) Search pronoun use by username.
3) Implement message pronoun substitution into a slash command.
4) Choose user to grab pronouns from for message substitution. Currently you must supply the pronouns to swap to and from.
5) Allow for message substitution to swap between pronoun sets for users with multiple pronouns listed.
