# <center> PROJECT  OBJECTIVES <center>

- Built a production-ready streaming and predicting pipeline using MeetupAPI and AWS
- Predicted in real-time the next industry-specific trend and tracked its popularity over time through
interactive time-series graphs 
- Discovered the emergence of a new community (category) in a city using Network Graphs
- Implementing Time Series to see the rise of a topic and how different topics evolve over time


# <center> Methodology <center>

# <center> Data Architecture <center>
![logo](./Images/Diagram.png)


- **Example of raw rsvp streaming file**
![logo](./Images/jsonfile.png)

- For more information [click here](https://github.com/Charlotte1904/MeetupAPI/blob/master/README.ipynb) .

 #  <center> Analysis <center>
----

<center> Category Distribution - San Francisco <center>
---

To explore trending activities in San Francisco, group categories are extracted from event information. The chart below shows most meetup focus on socializing, business/networking, language meetups and technology.

<center><img src="./Images/categorydist.png" ></center>

#  <center> NETWORK GRAPH <center>
---

The graphs below are screenshots of interactive network graphs (using plotly) segment topics into subgroup (industry-categories) illuminates relationships between topics.
 
 - Topics here are the hashtags, keywords that organizers use to describe events

<center><h3> A graph of the tech landscape in San Francisco </h3><center>

The basic idea is that topics in the same tech field will often be mentioned by the same Meetup groups.For example, if the business challenge of creating value from big data requires the combination of database technologies, analytics methods and parallel processing frameworks, these topics are likely to be of interest to the same practitioners. As a consequence, we would expect to find them mentioned by the same groups, in a way that defines a ‘data’ technology field and its community of practitioners.

We visualise these associations in a “topic network”  where topics that are often mentioned together are linked and “pulled together” (see graph below). After constructing that network, we use community detection algorithms to look for densely connected “clusters” of topics inside them.


<center><img src="./Images/techtopicnetwork.png" ></center>
---

<center><h3> San Francisco Activity Landscape </h3><center>

Using the similar concept for topics described in all events. 

<center><img src="./Images/sftopicsnetwork.png"></center>



#  <center> TIME SERIES <center>
---

With the topic networks, we can see a new keyword appear within a subgroup/cluster. We then track its activity overtime to see its popularity using time series.  

<center><h3> Top Trending Topics -  San Francisco </h3><center>
<center><img src="./Images/poptrendsf2.png" ></center>
<br>
<center><h3> DataScience Topics - San Francisco </h3><center>
<center><img src="./Images/dstopic2.png" ></center>
<br>
<center><h3> Labled-Category Groups </h3><center>
<center><img src="./Images/labledts.png" ></center>

