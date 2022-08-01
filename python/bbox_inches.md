# Fixing clipped matplotlib saved images

I was running into an issue where an image saved to disk was getting clipped so that some of the y-axis was not showing up in the saved image. The y-axis looked fine in the notebook output.

The fix was to add:

```
bbox_inches='tight'
```

to the `plt.save`  call.
