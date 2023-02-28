import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sys import stderr

class ImageProcessor:

    # https://matplotlib.org/stable/tutorials/introductory/images.html
    @staticmethod
    def load(path: str) -> np.ndarray or None:
        image = None
        try:
            image = mpimg.imread(path)
            shape = image.shape
            print(f"Loading image of dimensions {shape[0]} x {shape[1]}")
        except (Exception) as e:
            print(f"Exception: {e.__class__.__name__} -- strerror: {e.strerror if hasattr(e, 'strerror') else e}", file=stderr)
            return None
        return (image)

    @staticmethod
    def display(array: np.ndarray):
        if (not isinstance(array, np.ndarray)):
            print("ImgProcessor.display: Parameter is not a numpy array", file=stderr)
        else:
            try:
                plt.figure("Loaded image")
                plt.axis("off")
                plt.imshow(array)
                plt.show()
            except (Exception) as e:
                print(f"Exception: {e.__class__.__name__} -- strerror: {e.strerror if hasattr(e, 'strerror') else e}", file=stderr)


# if __name__ == "__main__":
#     imp = ImageProcessor()
#     arr = imp.load("../empty_file.png")
#     arr = imp.load("non_existing_file.png")
#     arr = imp.load("../module03.en.subject.pdf")
#     arr = imp.load("../42AI.png")
#     imp.display(arr)
#     arr = imp.load("../elon_canaGAN.png")
#     imp.display(arr)
#     imp.display([[0.03921569, 0.10588235, 0.19998235],
#                           [0.03921569, 0.10588235, 0.26666668],
#                           [0.03921569, 0.10588235, 0.26666668]])
#     imp.display(np.array([[0.03921569, 0.10588235, 0.19998235],
#                           [0.03921569, 0.10588235, 0.26666668],
#                           [0.03921569, 0.10588235, 0.26666668]]))
