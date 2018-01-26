#stepper driver setup
cw = True
ccw = False

import easydriver as ed

stepper_pan = ed.easydriver(18, 0.03, 23, 24, 17, 25)
stepper_tilt= ed.easydriver(12, 0.03, 16, 24, 17, 25)#pin numbers need to be figured out


stepper_tilt.set_direction(cw)
stepper_tilt.set_full_step()
for i in range(40):
	stepper_tilt.step()
stepper_tilt.set_direction(ccw)
for i in range(40):
	stepper_tilt.step()