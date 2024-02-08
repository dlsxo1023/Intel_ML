#include <iostream>
#include <opencv2/opencv.hpp>

//using namespace cv;
using namespace std;
void rotate(cv::Mat img, cv::Mat& rotate_img, int deg);

int main()
{
    //Rotate 함수 만들어서 사용해보기 
    cv::Mat img = cv::imread("images/lena.jpg");

    cv::Mat rotate_img;

    //cv::rotate(img, rotate_img, cv::ROTATE_90_CLOCKWISE);
    rotate(img, rotate_img, 40);

    cv::imshow("image", img);
    cv::imshow("rotate_img", rotate_img);
    cv::waitKey();
    
    //Point pt1;
    //pt1.x = 10;
    //pt1.y = 20;

    //Point pt2;
    //pt2.x = 20;
    //pt2.y = 30;
    //Point pt3 = pt1 + pt2;

    //cout << pt3 << endl;
    //
    //size
    //Size sz1, sz2(10, 20);
    //sz1.width = 5;
    //sz1.height = 10;
    //cout << sz1 + sz2 << endl;
    //cout << sz1.area() << endl;

    //rect
    //Rect rc1(10, 10, 60, 40);
    //Rect rc2;
  
    //system("pause");
}
void rotate(cv::Mat img, cv::Mat &rotate_img,  int deg)
{
    cv::Size s = img.size();

    //double theta = (CV_PI * deg) / (180.0);
    double angleRadians = (CV_PI * deg) / 180.0;
    double cosTheta = std::cos(angleRadians);
    double sinTheta = std::sin(angleRadians);

    //int newWidth = static_cast<int>(std::round(std::abs(cosTheta * img.cols) + std::abs(sinTheta * img.rows)));
    //int newHeight = static_cast<int>(std::round(std::abs(sinTheta * img.cols) + std::abs(cosTheta * img.rows)));

    rotate_img = cv::Mat(s, img.type(), cv::Scalar(0, 0, 0));// CV_8UC3);
    //rotate_img = cv::Mat(newHeight, newWidth, img.type(), cv::Scalar(0, 0, 0));
    //int center_x = int(s.width / 2);
    //int center_y = int(s.height / 2);
    cv::Point2f center(static_cast<float>(img.cols / 2), static_cast<float>(img.rows / 2));


    for (size_t y = 0; y < rotate_img.rows; y++)
    {
        for (size_t x = 0; x < rotate_img.cols; x++)
        {
            //int X = (int(x - center.x) * sin(theta) - int(y - center.y) * sin(theta)) + center.x;
            //int Y = (int(x - center.x) * sin(theta) + int(y - center.y) * cos(theta)) + center.y;
            int originalX = static_cast<int>(std::round((x - center.x) * cosTheta - (y - center.y) * sinTheta + center.x));
            int originalY = static_cast<int>(std::round((x - center.x) * sinTheta + (y - center.y) * cosTheta + center.y));

            /*
            if ((X < 0) || (X >= s.width) || (Y < 0) || (Y >= s.height))
                continue;
            rotate_img.at<uchar>(Y, X) = img.at<uchar>(y, x);
            **/
            if (originalX >= 0 && originalX < img.cols && originalY >= 0 && originalY < img.rows) {

                rotate_img.at<cv::Vec3b>(y, x) = img.at<cv::Vec3b>(originalY, originalX);
            }

        }
    }

 }