#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;


int main()
{
    Mat src = imread("../images/airplane2.jpg", IMREAD_COLOR);
    Mat dst = imread("../images/red_sky.jpg", IMREAD_COLOR);

    Mat src_mask(src.rows, src.cols, CV_8UC1);
    Mat dst_mask(dst.rows, dst.cols, CV_8UC1);

    vector<Point> pts;
    pts.push_back(Point(0, 40));
    pts.push_back(Point(150, 60));
    pts.push_back(Point(203, 56));
    pts.push_back(Point(200, 100));
    pts.push_back(Point(88, 103));
    pts.push_back(Point(1, 75));

    fillPoly(src_mask, pts, (255, 255, 255));

    Point center(600, 150);
    Mat output;
    seamlessClone(src, dst, src_mask, center, output, NORMAL_CLONE);

    TickMeter tm;
    tm.start();

    for (int j = 0; j < dst.rows; j++)
    {
        for (int i = 0; i < dst.cols; i++)
        {
            dst_mask.at<uchar>(j, i) = 255 - dst.at<uchar>(j, i);
        }
    }

    tm.stop();
    cout << "Image inverse took" << tm.getTimeMilli() << "ms. " << endl;

    imshow("src", src);
    imshow("dst", dst);
    imshow("output", output);
    waitKey();
    destroyAllWindows();

    return 0;
}


