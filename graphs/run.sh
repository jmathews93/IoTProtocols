#!/bin/bash

#COAP
#############

# CoAP LAN Trial1
# python3 cleanData.py ../results/coap/lan/trial1/coap_lan_test1_receiving_jamu.txt ../results/cleaned_data/coap/lan/trial1/
# python3 cleanData.py ../results/coap/lan/trial1/coap_lan_test1_receiving_pi_u.txt ../results/cleaned_data/coap/lan/trial1/
# python3 cleanData.py ../results/coap/lan/trial1/coap_lan_test1_seding_jamU.txt ../results/cleaned_data/coap/lan/trial1/
# python3 cleanData.py ../results/coap/lan/trial1/coap_lan_test1_sending_piu.txt ../results/cleaned_data/coap/lan/trial1/
# python3 cleanData.py ../results/coap/lan/trial1/coap_lan_test2_receiving_pi.txt ../results/cleaned_data/coap/lan/trial1/
# python3 cleanData.py ../results/coap/lan/trial1/coap_lan_test2_receiving_pi.txt ../results/cleaned_data/coap/lan/trial1/

# #CoAP LAN Trial2
# python3 cleanData.py ../results/coap/lan/trial2/coap_lan_tria2_sending_pi.txt ../results/cleaned_data/coap/lan/trial2/
# python3 cleanData.py ../results/coap/lan/trial2/coap_lan_trial2_receiving_jam.txt ../results/cleaned_data/coap/lan/trial2/
# python3 cleanData.py ../results/coap/lan/trial2/coap_lan_trial2_sending_jam.txt ../results/cleaned_data/coap/lan/trial2/
# python3 cleanData.py ../results/coap/lan/trial2/coap_lan_trial_receiving_pi.txt ../results/cleaned_data/coap/lan/trial2/

# #CoAP LAN Trial3
# python3 cleanData.py ../results/coap/lan/trial3/coap_trial3_receiving_jam.txt ../results/cleaned_data/coap/lan/trial3/
# python3 cleanData.py ../results/coap/lan/trial3/coap_trial3_receiving_pi.txt ../results/cleaned_data/coap/lan/trial3/
# python3 cleanData.py ../results/coap/lan/trial3/coap_trial3_sending_jam.txt  ../results/cleaned_data/coap/lan/trial3/
# python3 cleanData.py ../results/coap/lan/trial3/coap_trial3_sending_pi.txt ../results/cleaned_data/coap/lan/trial3/

# UDP
# #############
# #UDP WAN

# #TRIAL 1
# python3 cleanData.py ../results/udp/udp_test_1_30_trials_receiving_pi.txt ../results/cleaned_data/udp/wan/trial1/
# python3 cleanData.py ../results/udp/udp_test_1_30_trials_sending_jgtmac.txt ../results/cleaned_data/udp/wan/trial1/

# #TRIAL 2
# python3 cleanData.py ../results/udp/udp_test_2_30_trials_receiving_pi.txt ../results/cleaned_data/udp/wan/trial2/
# python3 cleanData.py ../results/udp/udp_test_2_30_trials_sending_jgtmac.txt ../results/cleaned_data/udp/wan/trial2/

# #TRIAL 3
# python3 cleanData.py ../results/udp/udp_test_3_30_trials_sending_jgtmac.txt ../results/cleaned_data/udp/wan/trial3/
# python3 cleanData.py ../results/udp/udp_test_3_30_trials_receiving_pi.txt ../results/cleaned_data/udp/wan/trial3/


# UDP LAN
# #TRIAL 1
# python3 cleanData.py ../results/udp/lan/test1/udp_lan_test_1_receiving_jamMac.txt ../results/cleaned_data/udp/lan/trial1/
# python3 cleanData.py ../results/udp/lan/test1/udp_lan_test_1_receiving_pi.txt  ../results/cleaned_data/udp/lan/trial1/
# python3 cleanData.py ../results/udp/lan/test1/udp_lan_test_1_sending_jamMac.txt ../results/cleaned_data/udp/lan/trial1/
# python3 cleanData.py ../results/udp/lan/test1/udp_lan_test_1_sending_pi.txt ../results/cleaned_data/udp/lan/trial1/
   
# #TRIAL 2
# python3 cleanData.py ../results/udp/lan/test2/udp_lan_test_2_receiving_jamMac.txt ../results/cleaned_data/udp/lan/trial2/
# python3 cleanData.py ../results/udp/lan/test2/udp_lan_test_2_receiving_pi.txt  ../results/cleaned_data/udp/lan/trial2/
# python3 cleanData.py ../results/udp/lan/test2/udp_lan_test_2_sending_jamMac.txt ../results/cleaned_data/udp/lan/trial2/
# python3 cleanData.py ../results/udp/lan/test2/udp_lan_test_2_sending_pi.txt ../results/cleaned_data/udp/lan/trial2/


# #TRIAL 3
# python3 cleanData.py ../results/udp/lan/test3/udp_lan_test_3_receiving_jamMac.txt ../results/cleaned_data/udp/lan/trial3/
# python3 cleanData.py ../results/udp/lan/test3/udp_lan_test_3_receiving_pi.txt  ../results/cleaned_data/udp/lan/trial3/
# python3 cleanData.py ../results/udp/lan/test3/udp_lan_test_3_sending_jamMac.txt ../results/cleaned_data/udp/lan/trial3/
# python3 cleanData.py ../results/udp/lan/test3/udp_lan_test_3_sending_pi.txt ../results/cleaned_data/udp/lan/trial3/


#OSC
#############

#OSC WAN

#RANDOM
python3 cleanData.py ../results/osc/test_1_30_trials_sending_pi.txt ../results/cleaned_data/osc/wan/random/
python3 cleanData.py ../results/osc/test_3_30_trials_sending_jgtmac.txt ../results/cleaned_data/osc/wan/random/
python3 cleanData.py ../results/osc/test_1_30_trials_receiving_pi.txt ../results/cleaned_data/osc/wan/random/
python3 cleanData.py ../results/osc/test_2_30_trials_receiving_pi.txt ../results/cleaned_data/osc/wan/random/
python3 cleanData.py ../results/osc/test_1_30_trials_recieving_jgtmac.txt ../results/cleaned_data/osc/wan/random/

python3 cleanData.py ../results/osc/test_2_30_trials_sending_jgtmac.txt ../results/cleaned_data/osc/wan/random/
python3 cleanData.py ../results/osc/test_1_30_trials_sending_jgtmac.txt ../results/cleaned_data/osc/wan/random/
python3 cleanData.py ../results/osc/test_3_30_trials_receiving_pi.txt ../results/cleaned_data/osc/wan/random/
   

#Receiving
# python3 cleanData.py ../results/osc/wan/receiving/osc_wan_recieving_test1.txt ../results/cleaned_data/osc/wan/receiving/

# #Sending
# python3 cleanData.py ../results/osc/wan/sending/osc_wan_tests-semisequential_1.txt ../results/cleaned_data/osc/wan/sending/
# python3 cleanData.py ../results/osc/wan/sending/osc_wan_tests-semisequential_2.txt ../results/cleaned_data/osc/wan/sending/
# python3 cleanData.py ../results/osc/wan/sending/osc_wan_tests-semisequential_3.txt ../results/cleaned_data/osc/wan/sending/


# #LAN
# #TRIAL1
# python3 cleanData.py ../results/osc/lan/test1/lan_test_1_receiving_jamMac.txt ../results/cleaned_data/osc/lan/trial1/
# python3 cleanData.py ../results/osc/lan/test1/lan_test_1_receiving_pi.txt ../results/cleaned_data/osc/lan/trial1/
# python3 cleanData.py ../results/osc/lan/test1/lan_test_1_sending_jamMac.txt ../results/cleaned_data/osc/lan/trial1/
# python3 cleanData.py ../results/osc/lan/test1/lan_test_1_sending_pi.txt ../results/cleaned_data/osc/lan/trial1/

# #TRIAL2
# python3 cleanData.py ../results/osc/lan/test2/lan_test_2_receiving_jamMac.txt ../results/cleaned_data/osc/lan/trial2/
# python3 cleanData.py ../results/osc/lan/test2/lan_test_2_receiving_pi.txt ../results/cleaned_data/osc/lan/trial2/
# python3 cleanData.py ../results/osc/lan/test2/lan_test_2_sending_jamMac.txt ../results/cleaned_data/osc/lan/trial2/
# python3 cleanData.py ../results/osc/lan/test2/lan_test_2_sending_pi.txt ../results/cleaned_data/osc/lan/trial2/

# #TRIAL3
# python3 cleanData.py ../results/osc/lan/test3/lan_test_3_receiving_jamMac.txt ../results/cleaned_data/osc/lan/trial3/
# python3 cleanData.py ../results/osc/lan/test3/lan_test_3_receiving_pi.txt ../results/cleaned_data/osc/lan/trial3/
# python3 cleanData.py ../results/osc/lan/test3/lan_test_3_sending_jamMac.txt ../results/cleaned_data/osc/lan/trial3/
# python3 cleanData.py ../results/osc/lan/test3/lan_test_3_sending_pi.txt ../results/cleaned_data/osc/lan/trial3/

         


         