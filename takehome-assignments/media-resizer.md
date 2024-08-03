## Media Resizer
We need you to create a media resizer API using Flask. This API should accept an image file as input and produce three resized output variants:

```
A WebP image with a width of 400 pixels.
A WebP image with a width of 1000 pixels.
A JPEG image with a width of 1200 pixels.
```

## Please implement the following:
```
An endpoint that accepts a POST request with an image file.
Logic to resize the image to the specified dimensions while maintaining the aspect ratio.
The resized images should be saved in WebP and JPEG formats as specified.
Return a JSON response containing the URLs or paths of the resized images.
You can use any additional libraries (e.g., Pillow for image processing) if needed. Please write the complete code for the Flask application, including any necessary setup, routes, and helper functions.
```

## Follow-up Questions:
```
How would you ensure the API handles large image files efficiently?
What considerations would you make for deploying this API in a production environment?
How would you handle error cases, such as invalid image formats or failed resizing operations?
```
