# Flashing Lights Image Stack Processing Software

### Usage Cases:

* Analysis of spatially resolved components present within an image stack 
- Requires the user to input a image stack of interest.
- Package will look at within all the frames of the image stack and then proceed by looking for events
  above a threshold value set the by the code.
- From every frame, events that occur will be converted to qualitative values of
  counts and relative intensity within each pixel.
- Furthermore, this package will determine where events occur based the detection of pixel brightness.
- All of this information wil be presented to the user. 
* Presenting information from fluorescence microscopy image stacks
- Input the name of a image stack. 
- The user will be provided a heatmap of the total distribution of counts of events among the pixels.
- Be shown a plot of total intensity among the pixels from the full image stack.
- Provide user the opportunity to save and name the file as they would prefer.
* Verifying quality of fluorescence microscopy data 

