#Pitch
###Bot name: @TweetToTwin
###Context: 
For any given user, there are bound to be followers who closely mirror that users' interests. One simple way to find someone who thinks similarly to you is to find someone who posts similar content. In this case, we use hashtags to determine the content that is being posted, because this is one of the more simple strategies for a beginning bot.

#The steps:
1. Bot checks Twitter API endpoint of statuses/mentions_timeline
2. For each tweet, the bot checks to see if the #TweetToTwin hashtag was used. If so, the id of the user 
is saved in a variable, and the last 50 hashtags posted by that user are stored in an array.
3. Bot then checks Twitter API endpoint GET followers/ids for that user. Creates a map, where each user id is a key.
4. Bot iterates over each id of the user variable's followers. For each user id, the bot checks Twitter API endpoint for statuses/user_timeline. Bot takes the last 50 hashtags posted of each user. The bot adds each hashtag as a value to that particular user's id in the map.
5. Create two loops: one that iterates over each hashtag in the original array, and one that iterates through each value in the map. If the two hashtags match up, the bot creates an int variable for that user's id, and raises the sum up by one. For every other matching hashtag, that int variable goes up by one.
6. At the end of the cycle, the bot takes the int with the greatest number associated with it and converts the int name to a string.
7. The bot then finds the username associated with that user id.
8. Use Twitter's statuses/update endpoint and reply back to the user with a tweet containing
their twin's username.

Things to keep in mind:
There should probably be ways to exclude followers' retweets that were initially posted by the original user (will have to double check API to see if this is possible). Will also have to exclude retweets in general, because if there are 1000 instances of "#ILoveDogs" in a particularly dog-loving follower's account, and the original user posted "#ILoveDogs" once, that follower will rank very highly with the initial user.