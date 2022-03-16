#pragma once

#include <string>
#include <unordered_map>

namespace Shell
{
struct SensorData {
    double enc_x;
    double enc_y;
    double gyro;
    double enc_lf;
    double enc_lb;
    double enc_rb;
    double enc_rf;
    double steer_enc_lf;
    double steer_enc_lb;
    double steer_enc_rb;
    double steer_enc_rf;
    double roller_enc_l;
    double roller_enc_r;
    double roller_enc_m;
    double elevation_enc;
    double rack_enc;
    double rotation_enc;
    double kanazawa_enc_l;
    double kanazawa_enc_r;

    std::string to_s() const;  // rubyでprint等が使えるようになる
};

// wheel func
// @doc tesueth
// void wheel(int num, double cur);

// wheels func
void wheels(double lf, double lb, double rb, double rf);

// steer func
void steer(int num, double cur);

// get_sensor_data func
SensorData get_sensor_data();

// get_sensor_data_raw func
SensorData get_sensor_data_raw();

// calibrate func
void calibrate(bool is_run);

// gyro_factor_add_sample func
void gyro_factor_add_sample(bool start);

// @detail wheel func
// @brief wheel func
// @brief wheel func
void gyro_factor_calculate_result(int rotation);

// wheel func
void gyro_factor_sample_reset();


}  // namespace Shell
