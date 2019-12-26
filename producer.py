from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

import random
import string
def randomString(stringLength=6):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters).upper() for i in range(stringLength))

msg = """
UNA:+.? '
UNB+IATB:1+6XPPC:ZZ+LHPPC:ZZ+940101:0950+1'
UNH+1+PNLIUQ:93:1:IA'
MSG+1:45'
IFT+3+{0}'
ERC+A7V:1:AMD'
IFT+3+{0}'
ODI'
TVL+240493:1000::1220+FRA+JFK+DL+400+C'
PDI++C:3+Y::3+F::1'
APD+74C:0:::6++++++6X'
TVL+240493:1740::2030+JFK+MIA+DL+081+C'
PDI++C:4'
APD+EM2:0:1630::6+++++++DA'
UNT+13+1'
UNZ+1+1
""".format(randomString())
future = producer.send('evaluator', msg)
# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
    print "Successfully produced message for {}, partition {}, offset {}.".format(
        record_metadata.topic, 
        record_metadata.partition, 
        record_metadata.offset)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass
