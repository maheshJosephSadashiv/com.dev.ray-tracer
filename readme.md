# Ray Tracing for noobs

Being a gaming fan, The GTA 6 trailer was amazing the animation and computer graphic was so good that this got me thinking, how is it possible to render each strand of hair such that it flows over a persons shoulder or even reacts to wind being blown. Just amazing!! This inspired a wave of curiosity in me, and made me think about computer graphics a topic that is often over-looked by native software developers such as myself. In this post I’ll be going over simple raytracing, along with lighting, shadows and reflections with the implementations as well. 

<img width="1417" alt="Screenshot 2024-01-02 at 12 00 18 PM" src="https://github.com/maheshJosephSadashiv/ComputerGraphics/assets/38533715/a2324cbc-1ef8-4db2-b612-8ff5806032db">
GTA 6 trailer: rays of light passing through a window

The idea for ray tracing was consieved in the 16th century Albrecht Dürer where he describes multiple ways of projecting 3-D objects onto a 2-D screen, this is what we are trying to accomplish in this tutorial.

Firstly lets define few terminologies that might not be apparent right now:
 - canvas : a rectangular array of pixels where we will be drawing on.
 - scene : set of objects that we are interested in rendering
 - camera-position : the location where you would put yours eyes to veiw the scene
 - veiwport : a rectangle (of length V_l, V_h) that acts as our window to the scene, a veiwport determines our field of view

The idea behind ray-tracing is to determine the color for each pixel in the canvas. This is done by projecting rays originating from the camera-location towards the viewport and finally onto the scene. Let us assume that the camera is placed at the origin of a cartician coordinate system i.e (0, 0, 0) and our veiwport placed such that the z axis goes through the center of the veiwport and is parallel to the x-y plane at a distance of d = 1 from the origin. As shown below.

