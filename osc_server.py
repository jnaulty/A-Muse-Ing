from liblo import *
import sys
import time
import serial
import math

ser = serial.Serial('/dev/tty.usbmodem1451')

class MuseServer(ServerThread):
    mellow_val = 0.0
    concentrate_val = 0.0
    #listen for messages on port 5004
    #ya...it's hardcoded in for now. (dirty hax)
    def __init__(self):
        ServerThread.__init__(self, port=5004)
        self.port=5004
	self.mel = 0.0
        self.con = 0.0
        self.horse = 0.0
        self.alpha = 0.0
        self.beta = 0.0
        self.gamma = 0.0
        self.theta = 0.0

    #receive accelrometer data
    # @make_method('/muse/acc', 'fff')
    # def acc_callback(self, path, args):
    #     acc_x, acc_y, acc_z = args
    #     print "%s %f %f %f" % (path, acc_x, acc_y, acc_z)

    #receive EEG data
    # @make_method('/muse/eeg', 'ffff')
    # def eeg_callback(self, path, args):
    #     l_ear, l_forehead, r_forehead, r_ear = args
    #     print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

    # @make_method('/muse/elements/theta_absolute', 'ffff')
    # def theta_callback(self, path, args):
    #     l_ear, l_forehead, r_forehead, r_ear = args
    #     print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)


    
    @make_method('/muse/elements/alpha_relative', 'ffff')
    def alpha_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

        # l_ear = l_ear || 0.0

        if math.isnan(l_ear):
            l_ear = 0.0
        if math.isnan(l_forehead):
            l_forehead = 0.0
        if math.isnan(r_forehead):
            r_forehead = 0.0
        if math.isnan(r_ear):
            r_ear = 0.0
        self.alpha = l_ear + r_forehead + r_ear

    @make_method('/muse/elements/beta_relative', 'ffff')
    def beta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)
        if math.isnan(l_ear):
            l_ear = 0.0
        if math.isnan(l_forehead):
            l_forehead = 0.0
        if math.isnan(r_forehead):
            r_forehead = 0.0
        if math.isnan(r_ear):
            r_ear = 0.0
        self.beta = l_ear + r_forehead + r_ear

    @make_method('/muse/elements/theta_relative', 'ffff')
    def theta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)
        if math.isnan(l_ear):
            l_ear = 0.0
        if math.isnan(l_forehead):
            l_forehead = 0.0
        if math.isnan(r_forehead):
            r_forehead = 0.0
        if math.isnan(r_ear):
            r_ear = 0.0
        self.theta = l_ear + r_forehead + r_ear

    @make_method('/muse/elements/horseshoe', 'ffff')
    def beta_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)
        self.horse=l_ear+l_forehead+r_forehead+r_ear

    @make_method('/muse/elements/gamma_relative', 'ffff')
    def gamma_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)
        if math.isnan(l_ear):
            l_ear = 0.0
        if math.isnan(l_forehead):
            l_forehead = 0.0
        if math.isnan(r_forehead):
            r_forehead = 0.0
        if math.isnan(r_ear):
            r_ear = 0.0
        self.gamma = l_ear + r_forehead + r_ear


        if self.alpha > self.gamma and self.alpha > self.theta and self.alpha > self.beta:
            ser.write('A')
            print ('a')
        elif self.beta > self.gamma and self.beta > self.theta and self.beta > self.alpha:
            ser.write('B')
            print ('b')
        elif self.theta > self.gamma and self.theta > self.alpha and self.theta > self.beta:
            ser.write('T')
            print ('t')
            
            
        elif self.gamma > self.alpha and self.gamma > self.theta and self.gamma > self.beta:
            ser.write('G')
            print('g')

        elif self.horse > 15:
            ser.write('D')
            print('d')
        else:
            print 'nothing'

    # @make_method('/muse/elements/beta_absolute', 'ffff')
    # def beta_callback(self, path, args):
    #     l_ear, l_forehead, r_forehead, r_ear = args
    #     print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

   
            

    # @make_method('/muse/elements/experimental/concentration', 'f')
    # def concentration_callback(self, path, args):
    #     concentrate = args
    #     print "%s %f" % (path, concentrate[0])
    #     self.con = concentrate[0]
    #     #concentrate_val = concentrate[0]
        

     
    # @make_method('/muse/elements/experimental/mellow', 'f')
    # def attention_callback(self, path, args):
    #     mellow = args
    #     print "%s %f" % (path, mellow[0])
    #     self.mel = mellow[0]
        
    #     if self.alpha >= .60:
    #         ser.write('A')
    #     elif self.horse == 16:
    #         ser.write('D')
    #     elif self.mel > self.con:
    #         ser.write('H')
            
            
    #     elif self.con > self.mel:
    #         ser.write('L')
            
    #     else:
    #         ser.write('Nada')
            



    
    # @make_method('/muse/elements/gamma_absolute', 'ffff')
    # def theta_absolute(self, path, args):
    #     l_ear, l_forehead, r_forehead, r_ear = args
    #     print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)


    #handle unexpected messages
  #   @make_method(None, None)
  #   def fallback(self, path, args, types, src):
  #       print "Unknown message \
		# \n\t Source: '%s' \
		# \n\t Address: '%s' \
		# \n\t Types: '%s ' \
		# \n\t Payload: '%s'" \
		# % (src.url, path, types, args)

try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
