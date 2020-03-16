# Flashing Lights Image Stack Processing Software

### Usage Cases:

1. Greg, a graduate student researcher who is responsible of in charge of understanding nanoparticle
collisions for electrochemical reactions. He wants to be able to see under what
conditions do reactions occur.

2. Peter, an undergraduate working for Greg, wants to be able to support his work by understanding
how often these colliisons and how bright the events are with accurate representations.

3. Dan, a visiting scientist, has been looking to see how comparable these observed collision reactions
are to what he sees in his neurological research.

### Case 1:
  * Greg has multiple videos that he has taken from various experimental conditions, not knowing if any of them captured any visible collisions.
  * He can insert each video into the package and with Skimage/numpy will illustrate reaction activity present in the video.
  * From there, he can determine what experimental conditions he should continue with.

### Case 2:
  * Peter notices that Greg has figured out what conditions trigger fluorescent events.
  * He wants to be able to help him summarize his results to the PI.
  * With the aid of Matplotlib, he can create heat maps that illustrate the total
  frequency and intensity displayed across the length of the video.
  * He can adjust the program such that if the video has points with very high
  frequency/intensity relative to other pixels to display a higher quality heat map.

### Case 3:
  * Dan sees the results of the package that Greg & Peter applied and is inspired
  by how easy and straight forward it is to use.
  * He inputs videos of animal brain slices into the package and instantly gets what he wanted.
  * He can see where neurons are firing in the brain through the plot.
  * On his last day, he realizes that he can't leave without the package and requests
  permission from the lab by bribing them with authorship on his next paper.  
