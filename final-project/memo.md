## Quick pitch

Online communities provide a great public platform for researching social-psychological phenomena. One particular phenomena I find interesting is social altruism. In this project, I am interested in the factors that contribute to our willingness to be altruistic toward online strangers, and whether we can utilize these discoveries to help out the less fortunate. Online communities provide a great way to release your own identity and strip away human factors that contribute to human bias.

For my final project, I'd like to create a website that reveals insight into online human altruism, using a dataset collected by Jurafsky et al back in 2013. I want to show an interactive graph that pinpoints the factors that go into online altruism, namely:

-What kinds of 'buzzwords' signify sincerity or vulnerability?
-Are we more likely to trust users who are active users of our community? (Aka, is account age and/or number of posts a factor?)

## The old way

Jurafsky et al [wrote a research paper](http://cs.stanford.edu/~althoff/raop-dataset/altruistic_requests_icwsm.pdf) based on their findings, which is a helpful resource in pinpointing key findings and insights into the human nature of altruism. However, as the age of the Internet becomes more heavily rooted in visualizations and infographics, I'd like to take this a step further and create a way to visualize the data so that others can benefit from the findings at-a-glance.

## The new way

Ideally, a user would be able to visit my website and type in a query that pulls up an interactive bar chart. I plan to have several different charts to display the data. I'd like to have charts that identify the success (or failure) of a request based on a query search. I'd also like to have a visualization based on age of account and success of pizza. I'd also like to show number of upvotes (relative to downvotes) on the post based on account age and query. As of now, I don't know if I'll use factors such as whether or not the post was edited, timestamp of request, or number of comments on the post (considering that comments probably consist mostly of 'I sent you pizza' and 'Thank you', along with any follow-up comments). I could foresee myself using timestamps in order to predict whether there is a best altruistic 'time', but I will only do that if I have time myself at the end of the project.

## Where the data comes from, and how it is collected

Back in 2013, Stanford professors Dan Jurafsky, Cristian Danescu-Niculescu-Mizil, and Tim Althoff collected a large public data set consisting of 5671 textual requests for pizza via Reddit's famous [Random Acts of Pizza](http://www.reddit.com/r/Random_Acts_Of_Pizza/) subreddit. More information on this dataset can be found [here](http://cs.stanford.edu/~althoff/raop-dataset/).

Their data is collected from 2013, and thus spans the entire history of the subreddit from 2009-2013. To fit within the timeframe of the project, I do not plan (at the time of writing) to collect all the data from 2013 to the present day.

(Note to self: send a memo to the owners of the original dataset to let them know that I am using their data.)

## Methods used for data-cleaning and processing

Very little cleaning will be necessary, but if I find it to be relevant, I might pull some more relevant data for purposes of comparison between more recent years.

## How the data will be stored

All the data that I will need for this project is stored in a single json file.

## Who else has done this (and how this attempt is better)

I'm not sure if anyone else has done anything like this before, though I do know that this dataset is public and is used by those who are practicing machine learning (!!), so I do not doubt that there is a better attempt at using it out there. However, as far as I know, there is no other website that uses this dataset to create visualizations.

## Pre-mortem

**Too many graphs**. Must remember to be the right amount of ambitious with the number of graphs that I want to post.

**The graphs are slow to load**. Perhaps a byproduct of the above point.