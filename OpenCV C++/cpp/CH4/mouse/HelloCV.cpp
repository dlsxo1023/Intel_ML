#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

void on_mouse(int event, int x, int y, int flags, void*);

Mat img = imread("images/lena.jpg");

int main()
{
    img = imread("../images/lena.jpg");

    namedWindow("img");
    setMouseCallback("img", on_mouse);

    imshow("img", img);
    waitKey();
    destroyAllWindows();

    return 0;
}

void on_mouse(int event, int x, int y, int flags, void*)
{
    Point ptold;
    switch (event)
    {
    case EVENT_LBUTTONDOWN:
        ptold = Point(x, y);
        cout << "left_down" << x << ", " << y << endl;
        break;
    case EVENT_LBUTTONUP:
        ptold = Point(x, y);
        cout << "left_up" << x << ", " << y << endl;
        break;
    case EVENT_MOUSEMOVE:
        if (flags & EVENT_FLAG_LBUTTON)
        {
            line(img, ptold, Point(x, y), Scalar(0, 0, 255), 2);
            imshow("img", img);
            ptold = Point(x, y);
        }
        break;
    default:
        break;
    }
}
