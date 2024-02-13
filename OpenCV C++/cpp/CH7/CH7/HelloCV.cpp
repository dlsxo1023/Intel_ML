#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

void filter_embossing();

int main()
{
    filter_embossing();

    return 0;
}

void filter_embossing()
{
    Mat img = imread("../../images/flower1.jpg");
    if (img.empty())
    {
        cerr << "Image load fail" << endl;
        return;
    }

    float data[] = {
        -1, -1, 0,
        -1, 0, 1,
         0, 1, 1
    };

    Mat emboss(3, 3, CV_32FC1, data);
    Mat dst;
    filter2D(img, dst, -1, emboss);

    imshow("image", img);
    imshow("dst", dst);
    waitKey();
    destroyAllWindows();
}
