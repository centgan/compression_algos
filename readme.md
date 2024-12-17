# Run Length Encoding
## How it Works
Run length encoding like many other compression alogrithms works well off very repeated data and this repetition has to be following one another. To put it simply run length encoding (RLE) works by iterating through the entire data provided, and counting the number of repeated subsequent characters. This algorithm is a form of lossless compression and treats the inputted data as individual characters. 

## How I Wrote Mine
I wrote the RLE to take in the inputted data iterate through each character and always output the character as well as the counter of the character even if it only occurs once. I decided to write it this way as it removes ambiguity for decompression as for example something like `A8BBC` if we removed the need to write the count of single occurances then the encoded will be `A8B2C` and how would you be able to differentiate between if A occures 8 times or is just the character 8. That's why I decided to write it so that the encoded will be `A181B2C1`. This no longer compresses it in fact it grew in size which is why this algorithm is extremely dependent on the number of times there are subsequent repeated characters. 

## Examples
>`AAABBBccc` => `A3B3c3`

This works well because there are many subsequent repeated characters which saves space.
>`235 235` => `213151 1213151` <br />

Even though from a human's point of view this can easily be compressed by saying `235 * 2` but computers can't pick up on this. They need very hard defined rules and while this time it works out to be `235 * 2` you can say delimiter by ' ' it wouldn't be able to do this anymore then `loooook` you could code it in but there are better compression algorithms to do it. 
