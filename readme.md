# Ray Tracing for noobs

Being a gaming fan, The GTA 6 trailer was amazing the animation and computer graphics were so good that this got me thinking, how is it possible to render each strand of hair such that it flows over a person's shoulder or even reacts to the wind being blown. Just amazing!! This inspired a wave of curiosity in me and made me think about computer graphics a topic that is often overlooked by native software developers such as myself. In this post, I’ll be going over simple raytracing, along with lighting, shadows, and reflections with the implementations as well. 

<img width="1417" alt="Screenshot 2024-01-02 at 12 00 18 PM" src="https://github.com/maheshJosephSadashiv/ComputerGraphics/assets/38533715/a2324cbc-1ef8-4db2-b612-8ff5806032db">
GTA 6 trailer: rays of light passing through a window

The idea for ray tracing was conceived in the 16th century Albrecht Dürer where he describes multiple ways of projecting 3-D objects onto a 2-D screen, this is what we are trying to accomplish in this tutorial.

Firstly let's define a few terminologies that might not be apparent right now:
 - canvas: a rectangular array of pixels which we will be drawing on.
 - scene: a set of objects that we are interested in rendering
 - camera-position: the location where you would put your eyes to view the scene
 - viewport: a rectangle (of length V_l and height V_h) that acts as our window to the scene, a viewport determines our field of view

The idea behind ray tracing is to determine the color for each pixel in the canvas. This is done by projecting rays originating from the camera-location towards the viewport and finally onto the scene. Let us assume that the camera is placed at the origin of a cartesian coordinate system i.e (0, 0, 0) and our viewport is placed such that the z-axis goes through the center of the viewport and is parallel to the x-y plane at a distance of d = 1 from the origin. As shown below.

![view_port](https://github.com/maheshJosephSadashiv/ComputerGraphics/assets/38533715/abaebbb8-0e54-4ba7-a3bd-7fc315327285)

The algorithm that follows is a very simple one:
```
for each pixel in canvas:
    view_point = convert_pixel_into_viewport(pixel.x, pixel.y)
    ray = create_ray(camera_position, view_point)
    color = find_nearest_interseting_objects(objects, ray)
    pixel.setColor(color)
```
The `convert_pixel_into_viewport(pixel)` function converts from the pixel coordinate system to the viewport/cartesian coordinate system. The equation for this is x = V_l/canvas_l + pixel_x and y = V_h/canvas_h - pixel_y. 

After implementing the above algorithm and adding 3 spheres to our scene we get the following.

<img width="374" alt="Screenshot 2024-01-02 at 2 58 28 PM" src="https://github.com/maheshJosephSadashiv/ComputerGraphics/assets/38533715/f488835c-9a92-4375-830d-02d8fc104d78">

Doesn't seem right does it, where is the 3-D effects!! we can fix that by adding some lighting. We are going to use 3 sources of light:
 - ambitent light: light source that is present in all directions
 - point light: a single source of light whose location is known
 - directional light: light source which only has direction

The effects of lighting in a scene can be rendered by calculating the intensity of light reflected back on to the viewport in other words we need to calculate the intencity of each po is the interaction of the light with the . 