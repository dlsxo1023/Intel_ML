#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
	Mat img = imread("../images/lena.jpg");

	imshow("image", img);
	while (true)
	{
		int keycode = waitKey();

		if (keycode == 'i' || keycode == 'I')
		{
			img = ~img;
			imshow("image", img);
		}
		else if (keycode == 27 || keycode == 'q' || keycode == 'Q')
			break;
	}
	destroyAllWindows();

	return 0;
}

