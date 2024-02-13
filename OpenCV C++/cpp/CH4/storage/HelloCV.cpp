#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

void writeData();
void readData();

int main()
{
    //writeData();
    readData();


    return 0;
}

void writeData()
{
    String name = "Jame";
    int age = 10;

    FileStorage fs;
    fs.open("mydata.yml", FileStorage::WRITE);
    if (fs.isOpened() != true)
    {
        cerr << "file open error" << endl;
        return;
    }
    fs << "name" << name;
    fs << "age" << age;

    fs.release();
}

void readData()
{
    String name;
    int age;

    FileStorage fs("mydata.yml", FileStorage::READ);
    if (fs.isOpened() != true)
    {
        cerr << "file open error" << endl;
        return;
    }

    fs["name"] >> name;
    fs["age"] >> age;
    
    cout << name << " : " << age << endl;

    fs.release();
    system("pause");
}
