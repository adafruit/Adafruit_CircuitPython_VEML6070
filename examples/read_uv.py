#VEML6070 Driver Example Code
import time
import busio
import veml6070
import board

with busio.I2C(board.SCL, board.SDA) as i2c:
    uv = veml6070.VEML6070(i2c)
    # Alternative constructors with parameters
    #uv = veml6070.VEML6070(i2c, 'VEML6070_1_T')
    #uv = veml6070.VEML6070(i2c, 'VEML6070_HALF_T', True)

    # take 10 readings
    for j in range(10):
        uv_raw = uv.read
        risk_level = uv.get_index(uv_raw)
        print('Reading: {0} | Risk Level: {1}'.format(uv_raw, risk_level))
        time.sleep(1)
