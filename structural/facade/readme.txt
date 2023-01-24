It provides a simplified interface to a library a framework, or any other complex set of class.


# Problem

    Imagine that you must make your code work with a broad set of objects that belong to a sophisticated library or framework.
Ordinarily, you’d need to initialize all of those objects, keep track of dependencies, execute methods in the correct order, and so on.

    As a result, the business logic of your classes would become tightly coupled to the implementation details of 3rd-party classes,
making it hard to comprehend and maintain.


# Solution

    A facade is a class that provides a simple interface to a complex subsystem which contains lots of moving parts.
A facade might provide limited functionality in comparison to working with the subsystem directly.
However, it includes only those features that clients really care about.

    Having a facade is handy when you need to integrate your app with a sophisticated library that has dozens of features,
but you just need a tiny bit of its functionality.

    For instance, an app that uploads short funny videos with cats to social media could potentially use a professional video conversion library.
However, all that it really needs is a class with the single method encode(filename, format).
After creating such a class and connecting it with the video conversion library, you’ll have your first facade.


## Pseudo Code

// These are some classes of a complex 3rd-party video
// conversion framework. We don't control that code, therefore
// can't simplify it.

class VideoFile
// ...

class OggCompressionCodec
// ...

class MPEG4CompressionCodec
// ...

class CodecFactory
// ...

class BitrateReader
// ...

class AudioMixer
// ...


// We create a facade class to hide the framework's complexity
// behind a simple interface. It's a trade-off between
// functionality and simplicity.
class VideoConverter is
    method convert(filename, format):File is
        file = new VideoFile(filename)
        sourceCodec = (new CodecFactory).extract(file)
        if (format == "mp4")
            destinationCodec = new MPEG4CompressionCodec()
        else
            destinationCodec = new OggCompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = (new AudioMixer()).fix(result)
        return new File(result)

// Application classes don't depend on a billion classes
// provided by the complex framework. Also, if you decide to
// switch frameworks, you only need to rewrite the facade class.
class Application is
    method main() is
        convertor = new VideoConverter()
        mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
        mp4.save()