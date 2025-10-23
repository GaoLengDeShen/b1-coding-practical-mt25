class PDController:
    """A simple PD controller for depth control of the submarine."""
    def __init__(self, kp= 0.15, kd= 0.6):
        self._kp = kp
        self._kd = kd
        self._previous_error = 0  


    def control(self, reference,output):
        
        error = reference - output
        control_action = self._kp * error + self._kd * (error - self._previous_error)
        # Update last error
        self._previous_error = error
        return control_action
