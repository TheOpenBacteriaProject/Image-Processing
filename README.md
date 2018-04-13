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

## Hough transform

In this section we'll explain in detail the AI tool we are using for detecting Petri dish, Hough transform. This is a method of extracting image features to detect mathemathically expressible shapes. In first place was proposed for straight lines although it can be extended for arbitrary shapes. We'll only need a parameterization. In our particular case we are working with circunferences, so giving a pic we obtain center an radius of our Petri dish. And our parameterization would be:
 
 ![](https://latex.codecogs.com/gif.latex?(x-x_{0})^{2}&space;&plus;&space;(y-y_{0})^{2}&space;=&space;r^{2})
 
Then our parametrical space would be![](https://latex.codecogs.com/gif.latex?(x_{0},y_{0},r)). We have to find the values of this parameters such we can draw the dish from the pics. 

So our algorithm binarize the image detecting edges in the following way:

![](https://github.com/TheOpenBacteriaProject/Image-Processing/blob/master/Images/aristas.png)

We can use Canny edge detector for this task. 

Once we have a binary pic that represents the edges we have to check it with the original pic using different parameters values. It's called transform due to we search values in a parametric space. There we'll search figures that intersects one with another, so more intersections there are, more votes there are for our figure to pass through. An illustrative example of what is described is the following:

![](https://github.com/TheOpenBacteriaProject/Image-Processing/blob/master/Images/explicacion.PNG)

In our case we have used the function [OpenCV](https://opencv.org/) to find  the circle that correspond to the Petri dish. We have chosen a range in which we "know" our algorithm will find the original dish.

## Bibliography

* Ballard, D. H. *Generalizing the Hough Transform to Detect Arbitrary
Shapes*, Pattern Recognition 13:111-122, 1981.

* Illingworth, J. and J. Kittler, *Survey of the Hough Transform*, Computer
Vision, Graphics, and Image Processing, 44(1):87-116, 1988
