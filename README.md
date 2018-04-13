# Image-Processing
![](https://raw.githubusercontent.com/TheOpenBacteriaProject/Branding/master/Documentation-Media/Document-Header.png)

In this repository we'll share the code of the images obtained throught the experiments. The images will also be uploaded.

## Introducction

In this project we will contemplate the creation of an engine that took photographs in an automatic way for being upladed later to the platform. For that purpose we need a system of artificial vision which help us on this task. One of the possible problems will be recognize Petri dish and bacteria population inside of it. Other interesting things would be estimating the amount of bacteria or area that this population fill.

In this repository we propose a method to detect in an automatic way, using AI techniques, our Petri dish and give an estimation of filled area.

## Our Algorithm

Our algorithm consist in firstly detect Petri dish. Por that we'll use Hough transform. As we watch on next images, we can detect dish from every pic taken from the experiments:

![](https://github.com/TheOpenBacteriaProject/Image-Processing/blob/master/Images/hough.png)

![](https://github.com/TheOpenBacteriaProject/Image-Processing/blob/master/Images/hough2.png)

![](https://github.com/TheOpenBacteriaProject/Image-Processing/blob/master/Images/seg4.png)

Once we have defined border of our Petri dish we opt for a pic binarization such that an separation value is chosen we can clearly define what it's bacteria and what it's dish. In this algorithm we opt for a fixed separation value but algorithm can learn to chose a value depending of luminosity an photography conditions so we can obtain a thinner representation but we'll leave it for future results.

Now we can count which pixels have been activated and calculate the filled area.

![](https://github.com/TheOpenBacteriaProject/Image-Processing/blob/master/Images/2.png)

![](https://github.com/TheOpenBacteriaProject/Image-Processing/blob/master/Images/3.png)

![](https://github.com/TheOpenBacteriaProject/Image-Processing/blob/master/Images/4.png)
