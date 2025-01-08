#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

// header files needed for serial comms
// reference: https://www.youtube.com/watch?v=IqEO95Gfp6k
#include <QDialog>
#include <QSerialPort>
#include <QSerialPortInfo>
#include <QDebug>
#include <QtWidgets>

#include <string>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_onBtn_clicked();

    void on_offBtn_clicked();

    void readSerial();

private:
    // this is the mainwindow graphical object itself
    Ui::MainWindow *ui;
    // the remaining is specific to the board
    QSerialPort *arduino;
    static const quint16 arduino_uno_vendorID = 9025;   // fill in
    static const quint16 arduino_uno_productID = 67;  // fill in
    QString arduino_port_name;
    bool arduino_is_available;
};
#endif // MAINWINDOW_H
