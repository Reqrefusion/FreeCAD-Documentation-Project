# Gordian Knot(FreeCAD-Documentation-Project)

While I was thinking about what the project did, I thought it would be nice to name it Gordian Knot. Because in my opinion, APIs are a thread and this project connects these APIs together. Unlike other projects, it does it without separating it into threads. Actually, this idiom is about using brute force, but since it's the most famous knot in history, it's probably okay.

Check the github wiki for more information. Any contribution is welcomed with great pleasure.

":" to ";"

Changes made here are now instantly reflected on the wiki. This is done instantly thanks to webhooks. If you want to try it, please create a PR.

With the current system, this repo is updated every 15 minutes and changes in the wiki are received. So, technically, it is an up-to-date copy of the wiki that can be stored as a file. The relevant PHP script added.

Being constantly updated: Done with cronjop

Media: Done. And now it works both ways. Carrying out the work on a shared server unfortunately causes some security measures to be blocked. The big change in the technical drawing is probably due to sending too much data and the bot protection cannot be passed by the server. The host was contacted and they whitelisted it, but since github uses variable IP, it was not fully fixed. Frankly, I expected these operations to be done on the cheapest server without requiring anything extra, but this is really sad.

Considering the slow pace of change of the wiki, this backup is actually quite sufficient. It seems that it is not necessary to update instantly. Because 15 minutes is a very long time for FreeCAD wiki. However, this may lead to some errors.

I added a system that checks the first 7 characters of the sha, but it has some problems, maybe I should use the date as some kind of id, not the sha.

Creation of a Github App: Currently, the classic personal token is being used. I think it is still easier and superior to this other ridiculous thing, but it seems necessary to create an app. Work will be done for this.
