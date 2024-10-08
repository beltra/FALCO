#ifndef MOTOR_H
#define MOTOR_H

#include <Arduino.h>

#include "pinDef.h"

void initializeMotors();
void driveMotors(float thrust[4]);
void throttleCut(unsigned long cutOffCmd, float pwm[], bool *armedFly);

#endif