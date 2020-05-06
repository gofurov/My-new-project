import ezgmail
# ezgmail.send("inomjon.gafurov@yahoo.com", "test", "hi, boss")
recentThread = ezgmail.recent(maxResults= 100)
# ezgmail.summary(recentThread)
print(len(recentThread))
