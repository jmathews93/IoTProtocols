#Graphs needed:

# Protocol 	Test 	Avg Packets/s 	Avg Time 	Total Time 
# UDP Sending 	1 	29335.00 	1.40 	42
# UDP Sending 	2 	13855.03 	2.57 	77
# UDP Sending 	3 	11619.53 	10.00 	300
				
# OSC Sending 	1 	29275.93 	2.73 	82
# OSC Sending 	2 	16912.93 	3.03 	91
# OSC Sending 	3 	6142.73 	5.77 	173
				
# OSC Receiving 	1 	29333.63 	10.57 	317
				
# OSC Receiving Pi 	1 	8427.53 	2.87 	86
# OSC Receiving Pi 	2 	3117.97 	3.17 	96
# OSC Receiving Pi 	3 	634.20 	5.87 	176

import csv, sys
import numpy as np
import matplotlib.pyplot as plt


def avg_packets_per_s(file_name):
    sum = 0

    with open(file_name, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

    for i in range(1, len(data)):
        sum = sum + int(data[i][1])

    avg = sum/len(data)

    return avg

def get_x_and_y(file_name):
    x_axis = []
    y_axis = []

    with open(file_name, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

    for i in range(1, len(data)):
        x_axis.append(int(data[i][0]))
        y_axis.append(int(data[i][1]))

    return x_axis, y_axis

def avg_time():
    pass

def total_time():
    pass


def main():
    #region OSC Stats
    ##################################################################################################################
    #OSC WAN Pi Recv
    osc_wan_recv_pi_test1_avg = avg_packets_per_s('../results/cleaned_data/osc/wan/receiving/test_1_30_trials_receiving_pi.csv')
    print("OSC WAN Rcv pi Test1: " + str(osc_wan_recv_pi_test1_avg))
    osc_wan_recv_pi_test2_avg = avg_packets_per_s('../results/cleaned_data/osc/wan/receiving/test_2_30_trials_receiving_pi.csv')
    print("OSC WAN Rcv pi Test2: " + str(osc_wan_recv_pi_test2_avg))
    osc_wan_recv_pi_test3_avg = avg_packets_per_s('../results/cleaned_data/osc/wan/receiving/test_3_30_trials_receiving_pi.csv')
    print("OSC WAN Rcv pi Test3: " + str(osc_wan_recv_pi_test3_avg))

    #OSC WAN Pi Send
    osc_wan_send_pi_test1_avg = avg_packets_per_s('../results/cleaned_data/osc/wan/sending/test_1_30_trials_sending_pi.csv')
    print("OSC WAN Send pi Test1: " + str(osc_wan_send_pi_test1_avg))

    #OSC WAN PC Recv
    osc_wan_recv_pc_test1_avg = avg_packets_per_s('../results/cleaned_data/osc/wan/receiving/test_1_30_trials_recieving_jgtmac.csv')
    print("OSC WAN Rcv PC Test1: " + str(osc_wan_recv_pc_test1_avg))

    #OSC WAN PC Send
    osc_wan_send_pc_test1_avg = avg_packets_per_s('../results/cleaned_data/osc/wan/sending/test_1_30_trials_sending_jgtmac.csv')
    print("OSC WAN Send PC Test1: " + str(osc_wan_send_pc_test1_avg))
    osc_wan_send_pc_test2_avg = avg_packets_per_s('../results/cleaned_data/osc/wan/sending/test_2_30_trials_sending_jgtmac.csv')
    print("OSC WAN Send PC Test2: " + str(osc_wan_send_pc_test2_avg))
    osc_wan_send_pc_test3_avg = avg_packets_per_s('../results/cleaned_data/osc/wan/sending/test_3_30_trials_sending_jgtmac.csv')
    print("OSC WAN Send PC Test3: " + str(osc_wan_send_pc_test3_avg))

    #OSC LAN
    #################
    #OSC LAN Pi Recv
    osc_lan_recv_pi_test1_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial1/lan_test_1_receiving_pi.csv')
    print("OSC LAN Rcv pi Test1: " + str(osc_lan_recv_pi_test1_avg))
    osc_lan_recv_pi_test2_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial2/lan_test_2_receiving_pi.csv')
    print("OSC LAN Rcv pi Test2: " + str(osc_lan_recv_pi_test2_avg))
    osc_lan_recv_pi_test3_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial3/lan_test_3_receiving_pi.csv')
    print("OSC LAN Rcv pi Test3: " + str(osc_lan_recv_pi_test3_avg))

    #OSC LAN Pi Send
    osc_lan_send_pi_test1_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial1/lan_test_1_sending_pi.csv')
    print("OSC LAN Rcv pi Test1: " + str(osc_lan_send_pi_test1_avg))
    osc_lan_send_pi_test2_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial2/lan_test_2_sending_pi.csv')
    print("OSC LAN Rcv pi Test2: " + str(osc_lan_send_pi_test2_avg))
    osc_lan_send_pi_test3_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial3/lan_test_3_sending_pi.csv')
    print("OSC LAN Rcv pi Test3: " + str(osc_lan_send_pi_test3_avg))

    #OSC LAN PC Recv
    osc_lan_recv_pc_test1_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial1/lan_test_1_receiving_jamMac.csv')
    print("OSC LAN Rcv PC Test1: " + str(osc_lan_recv_pc_test1_avg))
    osc_lan_recv_pc_test2_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial2/lan_test_2_receiving_jamMac.csv')
    print("OSC LAN Rcv PC Test2: " + str(osc_lan_recv_pc_test2_avg))
    osc_lan_recv_pc_test3_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial3/lan_test_3_receiving_jamMac.csv')
    print("OSC LAN Rcv PC Test3: " + str(osc_lan_recv_pc_test3_avg))

    #OSC LAN PC Send
    osc_lan_send_pc_test1_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial1/lan_test_1_sending_jamMac.csv')
    print("OSC LAN Send PC Test1: " + str(osc_lan_send_pc_test1_avg))
    osc_lan_send_pc_test2_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial2/lan_test_2_sending_jamMac.csv')
    print("OSC LAN Send PC Test2: " + str(osc_lan_send_pc_test2_avg))
    osc_lan_send_pc_test3_avg = avg_packets_per_s('../results/cleaned_data/osc/lan/trial3/lan_test_3_sending_jamMac.csv')
    print("OSC LAN Send PC Test3: " + str(osc_lan_send_pc_test3_avg))

    #endregion
    ##################################################################################################################
    
    #region UDP Stats
    #######################################################################################################################################################
    #UDP WAN Pi Recv
    udp_wan_recv_pi_test1_avg = avg_packets_per_s('../results/cleaned_data/udp/wan/trial1/udp_test_1_30_trials_receiving_pi.csv')
    print("UDP WAN Rcv pi Test1: " + str(udp_wan_recv_pi_test1_avg))
    udp_wan_recv_pi_test2_avg = avg_packets_per_s('../results/cleaned_data/udp/wan/trial2/udp_test_2_30_trials_receiving_pi.csv')
    print("UDP WAN Rcv pi Test2: " + str(udp_wan_recv_pi_test2_avg))
    udp_wan_recv_pi_test3_avg = avg_packets_per_s('../results/cleaned_data/udp/wan/trial3/udp_test_3_30_trials_receiving_pi.csv')
    print("UDP WAN Rcv pi Test3: " + str(udp_wan_recv_pi_test3_avg))

    #UDP WAN Pc Send
    udp_wan_send_pc_test1_avg = avg_packets_per_s('../results/cleaned_data/udp/wan/trial1/udp_test_1_30_trials_sending_jgtmac.csv')
    print("UDP WAN send pc Test1: " + str(udp_wan_send_pc_test1_avg))
    udp_wan_send_pc_test2_avg = avg_packets_per_s('../results/cleaned_data/udp/wan/trial2/udp_test_2_30_trials_sending_jgtmac.csv')
    print("UDP WAN send pc Test2: " + str(udp_wan_send_pc_test2_avg))
    udp_wan_send_pc_test3_avg = avg_packets_per_s('../results/cleaned_data/udp/wan/trial3/udp_test_3_30_trials_sending_jgtmac.csv')
    print("UDP WAN send pc Test3: " + str(udp_wan_send_pc_test3_avg))

    #UDP LAN
    ###################################
    #UDP LAN Pi Recv
    udp_lan_recv_pi_test1_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial1/udp_lan_test_1_receiving_pi.csv')
    print("UDP LAN Rcv pi Test1: " + str(udp_lan_recv_pi_test1_avg))
    udp_lan_recv_pi_test2_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial2/udp_lan_test_2_receiving_pi.csv')
    print("UDP LAN Rcv pi Test2: " + str(udp_lan_recv_pi_test2_avg))
    udp_lan_recv_pi_test3_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial3/udp_lan_test_3_receiving_pi.csv')
    print("UDP LAN Rcv pi Test3: " + str(udp_lan_recv_pi_test3_avg))

    #UDP LAN Pi Send
    udp_lan_send_pi_test1_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial1/udp_lan_test_1_sending_pi.csv')
    print("UDP LAN Send pi Test1: " + str(udp_lan_send_pi_test1_avg))
    udp_lan_send_pi_test2_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial2/udp_lan_test_2_sending_pi.csv')
    print("UDP LAN Send pi Test2: " + str(udp_lan_send_pi_test2_avg))
    udp_lan_send_pi_test3_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial3/udp_lan_test_3_sending_pi.csv')
    print("UDP LAN Send pi Test3: " + str(udp_lan_send_pi_test3_avg))

    #UDP LAN PC Recv
    udp_lan_recv_pc_test1_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial1/udp_lan_test_1_receiving_jamMac.csv')
    print("UDP LAN Rcv pc Test1: " + str(udp_lan_recv_pc_test1_avg))
    udp_lan_recv_pc_test2_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial2/udp_lan_test_2_receiving_jamMac.csv')
    print("UDP LAN Rcv pc Test2: " + str(udp_lan_recv_pc_test2_avg))
    udp_lan_recv_pc_test3_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial3/udp_lan_test_3_receiving_jamMac.csv')
    print("UDP LAN Rcv pc Test3: " + str(udp_lan_recv_pc_test3_avg))

    #UDP LAN PC Send
    udp_lan_send_pc_test1_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial1/udp_lan_test_1_sending_jamMac.csv')
    print("UDP LAN Send pc Test1: " + str(udp_lan_send_pc_test1_avg))
    udp_lan_send_pc_test2_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial2/udp_lan_test_2_sending_jamMac.csv')
    print("UDP LAN Send pc Test2: " + str(udp_lan_send_pc_test2_avg))
    udp_lan_send_pc_test3_avg = avg_packets_per_s('../results/cleaned_data/udp/lan/trial3/udp_lan_test_3_sending_jamMac.csv')
    print("Udp LAN Send pc Test3: " + str(udp_lan_send_pc_test3_avg))

    #endregion

    #region COAP Stats
    #######################################################################################################################################################
    #COap WAN Pi Recv
    coap_wan_recv_pi_test1_avg = avg_packets_per_s('../results/cleaned_data/coap/wan/wancoap_test_1_30_trials_sending_pi.csv')
    print("Coap WAN Rcv pi Test1: " + str(coap_wan_recv_pi_test1_avg * 30))

    #COap LAN Pi Recv
    coap_lan_recv_pi_test1_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial1/coap_lan_test1_receiving_pi_u.csv')
    print("COAP LAN Rcv pi Test1: " + str(coap_lan_recv_pi_test1_avg * 30))
    coap_lan_recv_pi_test2_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial2/coap_lan_trial_receiving_pi.csv')
    print("COAP LAN Rcv pi Test2: " + str(coap_lan_recv_pi_test2_avg * 30))
    coap_lan_recv_pi_test3_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial3/coap_trial3_receiving_pi.csv')
    print("COAP LAN Rcv pi Test3: " + str(coap_lan_recv_pi_test3_avg * 30))

    #COap LAN Pi Send
    coap_lan_send_pi_test1_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial1/coap_lan_test1_sending_piu.csv')
    print("COAP LAN Send pi Test1: " + str(coap_lan_send_pi_test1_avg * 30))
    coap_lan_send_pi_test2_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial2/coap_lan_tria2_sending_pi.csv')
    print("COAP LAN Send pi Test2: " + str(coap_lan_send_pi_test2_avg * 30))
    coap_lan_send_pi_test3_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial3/coap_trial3_sending_pi.csv')
    print("COAP LAN Send pi Test3: " + str(coap_lan_send_pi_test3_avg * 30))

    #COap LAN PC Send
    coap_lan_send_pc_test1_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial1/coap_lan_test1_seding_jamU.csv')
    print("COAP LAN Send pc Test1: " + str(coap_lan_send_pc_test1_avg * 30))
    coap_lan_send_pc_test2_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial2/coap_lan_trial2_sending_jam.csv')
    print("COAP LAN Send pc Test2: " + str(coap_lan_send_pc_test2_avg * 30))
    coap_lan_send_pc_test3_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial3/coap_trial3_sending_jam.csv')
    print("COAP LAN Send pc Test3: " + str(coap_lan_send_pc_test3_avg * 30))

    #COap LAN PC Recv
    coap_lan_recv_pc_test1_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial1/coap_lan_test1_receiving_jamu.csv')
    print("COAP LAN Rcv pc Test1: " + str(coap_lan_recv_pc_test1_avg * 30))
    coap_lan_recv_pc_test2_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial2/coap_lan_trial2_receiving_jam.csv')
    print("COAP LAN Rcv pc Test2: " + str(coap_lan_recv_pc_test2_avg * 30))
    coap_lan_recv_pc_test3_avg = avg_packets_per_s('../results/cleaned_data/coap/lan/trial3/coap_trial3_receiving_jam.csv')
    print("COAP LAN Rcv pc Test3: " + str(coap_lan_recv_pc_test3_avg * 30))
    #endregion

    ##################################################################################################################
    #GRAPHS
    #############
    #region Bar Charts
    #WAN PI RECV
    #================================================================================================================================
    # data to plot
    # n_groups = 3
    # means_osc = (osc_wan_recv_pi_test1_avg, osc_wan_recv_pi_test2_avg, osc_wan_recv_pi_test3_avg, )
    # means_udp = (udp_wan_recv_pi_test1_avg, udp_wan_recv_pi_test2_avg, udp_wan_recv_pi_test3_avg)
    # means_coap = (coap_wan_recv_pi_test1_avg, 0, 0)

    # # create plot
    # fig, ax = plt.subplots()
    # index = np.arange(n_groups)
    # bar_width = 0.15
    # opacity = 0.8

    # rects1 = plt.bar(index, means_osc, bar_width,
    # alpha=opacity,
    # color='b',
    # label='OSC')

    # rects2 = plt.bar(index + bar_width, means_udp, bar_width,
    # alpha=opacity,
    # color='g',
    # label='UDP')

    # rects3 = plt.bar(index + (bar_width*2), means_coap, bar_width,
    # alpha=opacity,
    # color='r',
    # label='COaP')

    # plt.xlabel('Trial')
    # plt.ylabel('Packets/s')
    # plt.title('Packets Received by Pi over WAN')
    # plt.xticks(index + bar_width, ('Trial 1', 'Trial 2', 'Trial 3'))
    # plt.legend()

    # plt.tight_layout()
    # # plt.show()
    # plt.savefig('generated_graphs/wan_packets_received_by_pi.png')
    #================================================================================================================================

    #LAN PI RECV
    #================================================================================================================================
    # data to plot
    # n_groups = 3
    # means_osc = (osc_lan_recv_pi_test1_avg, osc_lan_recv_pi_test2_avg, osc_lan_recv_pi_test3_avg, )
    # means_udp = (udp_lan_recv_pi_test1_avg, udp_lan_recv_pi_test2_avg, udp_lan_recv_pi_test3_avg)
    # means_coap = (coap_lan_recv_pi_test1_avg, coap_lan_recv_pi_test2_avg, coap_lan_recv_pi_test3_avg)

    # # create plot
    # fig, ax = plt.subplots()
    # index = np.arange(n_groups)
    # bar_width = 0.15
    # opacity = 0.8

    # rects1 = plt.bar(index, means_osc, bar_width,
    # alpha=opacity,
    # color='b',
    # label='OSC')

    # rects2 = plt.bar(index + bar_width, means_udp, bar_width,
    # alpha=opacity,
    # color='g',
    # label='UDP')

    # rects3 = plt.bar(index + (bar_width*2), means_coap, bar_width,
    # alpha=opacity,
    # color='r',
    # label='COaP')

    # plt.xlabel('Trial')
    # plt.ylabel('Packets/s')
    # plt.title('Packets Received by Pi over LAN')
    # plt.xticks(index + bar_width, ('Trial 1', 'Trial 2', 'Trial 3'))
    # plt.legend()

    # plt.tight_layout()
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_received_by_pi.png')

    #LAN PI SEND
    #================================================================================================================================
    # data to plot
    # n_groups = 3
    # means_osc = (osc_lan_send_pi_test1_avg, osc_lan_send_pi_test2_avg, osc_lan_send_pi_test3_avg, )
    # means_udp = (udp_lan_send_pi_test1_avg, udp_lan_send_pi_test2_avg, udp_lan_send_pi_test3_avg)
    # means_coap = (coap_lan_send_pi_test1_avg, coap_lan_send_pi_test2_avg, coap_lan_send_pi_test3_avg)

    # # create plot
    # fig, ax = plt.subplots()
    # index = np.arange(n_groups)
    # bar_width = 0.15
    # opacity = 0.8

    # rects1 = plt.bar(index, means_osc, bar_width,
    # alpha=opacity,
    # color='b',
    # label='OSC')

    # rects2 = plt.bar(index + bar_width, means_udp, bar_width,
    # alpha=opacity,
    # color='g',
    # label='UDP')

    # rects3 = plt.bar(index + (bar_width*2), means_coap, bar_width,
    # alpha=opacity,
    # color='r',
    # label='COaP')

    # plt.xlabel('Trial')
    # plt.ylabel('Packets/s')
    # plt.title('Packets Sent by Pi over LAN')
    # plt.xticks(index + bar_width, ('Trial 1', 'Trial 2', 'Trial 3'))
    # plt.legend()

    # plt.tight_layout()
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pi.png')

    #LAN PC SEND
    #================================================================================================================================
    # data to plot
    # n_groups = 3
    # means_osc = (osc_lan_send_pc_test1_avg, osc_lan_send_pc_test2_avg, osc_lan_send_pc_test3_avg, )
    # means_udp = (udp_lan_send_pc_test1_avg, udp_lan_send_pc_test2_avg, udp_lan_send_pc_test3_avg)
    # means_coap = (coap_lan_send_pc_test1_avg, coap_lan_send_pc_test2_avg, coap_lan_send_pc_test3_avg)

    # # create plot
    # fig, ax = plt.subplots()
    # index = np.arange(n_groups)
    # bar_width = 0.15
    # opacity = 0.8

    # rects1 = plt.bar(index, means_osc, bar_width,
    # alpha=opacity,
    # color='b',
    # label='OSC')

    # rects2 = plt.bar(index + bar_width, means_udp, bar_width,
    # alpha=opacity,
    # color='g',
    # label='UDP')

    # rects3 = plt.bar(index + (bar_width*2), means_coap, bar_width,
    # alpha=opacity,
    # color='r',
    # label='COaP')

    # plt.xlabel('Trial')
    # plt.ylabel('Packets/s')
    # plt.title('Packets Sent by PC over LAN')
    # plt.xticks(index + bar_width, ('Trial 1', 'Trial 2', 'Trial 3'))
    # plt.legend()

    # plt.tight_layout()
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pc.png')

    #LAN PC RECV
    #================================================================================================================================
    # data to plot
    # n_groups = 3
    # means_osc = (osc_lan_recv_pc_test1_avg, osc_lan_recv_pc_test2_avg, osc_lan_recv_pc_test3_avg, )
    # means_udp = (udp_lan_recv_pc_test1_avg, udp_lan_recv_pc_test2_avg, udp_lan_recv_pc_test3_avg)
    # means_coap = (coap_lan_recv_pc_test1_avg, coap_lan_recv_pc_test2_avg, coap_lan_recv_pc_test3_avg)

    # # create plot
    # fig, ax = plt.subplots()
    # index = np.arange(n_groups)
    # bar_width = 0.15
    # opacity = 0.8

    # rects1 = plt.bar(index, means_osc, bar_width,
    # alpha=opacity,
    # color='b',
    # label='OSC')

    # rects2 = plt.bar(index + bar_width, means_udp, bar_width,
    # alpha=opacity,
    # color='g',
    # label='UDP')

    # rects3 = plt.bar(index + (bar_width*2), means_coap, bar_width,
    # alpha=opacity,
    # color='r',
    # label='COaP')

    # plt.xlabel('Trial')
    # plt.ylabel('Packets/s')
    # plt.title('Packets Received by PC over LAN')
    # plt.xticks(index + bar_width, ('Trial 1', 'Trial 2', 'Trial 3'))
    # plt.legend()

    # plt.tight_layout()
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_recvd_by_pc.png')
    #endregion
    #===============================================================
    
    #region LINE GRAPHS
    #############################
    #LAN Pi Recv Trial 1
    # osc_x1, osc_y1 = get_x_and_y('../results/cleaned_data/osc/lan/trial1/lan_test_1_receiving_pi.csv')
    # udp_x2, udp_y2 = get_x_and_y('../results/cleaned_data/udp/lan/trial1/udp_lan_test_1_receiving_pi.csv')
    # coap_x3, coap_y3 = get_x_and_y('../results/cleaned_data/coap/lan/trial1/coap_lan_test1_receiving_pi_u.csv')
    

    # list_of_x = [osc_x1, udp_x2, coap_x3]
    # min_len = min(len(i) for i in list_of_x) - 1 
    # print(min_len) 
    # list_of_x_num = [osc_y1[min_len], udp_y2[min_len], coap_y3[min_len]]
    # min_num = min(i for i in list_of_x_num)
    # print(min_num)

    # plt.plot(osc_x1[0:min_num], osc_y1[0:min_num], label = "OSC")
    # plt.plot(udp_x2[0:min_num], udp_y2[0:min_num], label = "UDP")
    # plt.plot(coap_x3[0:min_num], coap_y3[0:min_num], label = "CoAP")

    # plt.xlabel('time (s)')
    # plt.ylabel('packets/s')
    # plt.title('LAN Pi Receiving Trial 1')
    # plt.legend(loc='upper right')
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_received_by_pi_line_chart.png')


    # #LAN Pi Send Trial 1
    # osc_x1, osc_y1 = get_x_and_y('../results/cleaned_data/osc/lan/trial1/lan_test_1_sending_pi.csv')
    # udp_x2, udp_y2 = get_x_and_y('../results/cleaned_data/udp/lan/trial1/udp_lan_test_1_sending_pi.csv')
    # coap_x3, coap_y3 = get_x_and_y('../results/cleaned_data/coap/lan/trial1/coap_lan_test1_sending_piu.csv')
    

    # list_of_x = [osc_x1, udp_x2, coap_x3]
    # min_len = min(len(i) for i in list_of_x) - 1 
    # print(min_len) 
    # list_of_x_num = [osc_y1[min_len], udp_y2[min_len], coap_y3[min_len], len(osc_x1), len(udp_x2), len(coap_x3)]
    # min_num = min(i for i in list_of_x_num)
    # print(min_num)

    # plt.plot(osc_x1[0:min_num], osc_y1[0:min_num], label = "OSC")
    # plt.plot(udp_x2[0:min_num], udp_y2[0:min_num], label = "UDP")
    # plt.plot(coap_x3[0:min_num], coap_y3[0:min_num], label = "CoAP")

    # plt.xlabel('time (s)')
    # plt.ylabel('packets/s')
    # plt.title('LAN Pi Sending Trial 1')
    # plt.legend(loc='upper right')
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pi_line_chart.png')

    #LAN PC Recv Trial 1
    # osc_x1, osc_y1 = get_x_and_y('../results/cleaned_data/osc/lan/trial1/lan_test_1_receiving_jamMac.csv')
    # udp_x2, udp_y2 = get_x_and_y('../results/cleaned_data/udp/lan/trial1/udp_lan_test_1_receiving_jamMac.csv')
    # coap_x3, coap_y3 = get_x_and_y('../results/cleaned_data/coap/lan/trial1/coap_lan_test1_receiving_jamu.csv')
    

    # list_of_x = [osc_x1, udp_x2, coap_x3]
    # min_len = min(len(i) for i in list_of_x) - 1 
    # print(min_len) 
    # list_of_x_num = [osc_y1[min_len], udp_y2[min_len], coap_y3[min_len], len(osc_x1), len(udp_x2), len(coap_x3)]
    # min_num = min(i for i in list_of_x_num)
    # print(min_num)

    # plt.plot(osc_x1[0:min_num], osc_y1[0:min_num], label = "OSC")
    # plt.plot(udp_x2[0:min_num], udp_y2[0:min_num], label = "UDP")
    # plt.plot(coap_x3[0:min_num], coap_y3[0:min_num], label = "CoAP")

    # plt.xlabel('time (s)')
    # plt.ylabel('packets/s')
    # plt.title('LAN Pi Sending Trial 1')
    # plt.legend(loc='upper right')
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_recvd_by_pc_line_chart.png')


    #LAN PC Send Trial 1
    osc_x1, osc_y1 = get_x_and_y('../results/cleaned_data/osc/lan/trial1/lan_test_1_sending_jamMac.csv')
    udp_x2, udp_y2 = get_x_and_y('../results/cleaned_data/udp/lan/trial1/udp_lan_test_1_sending_jamMac.csv')
    coap_x3, coap_y3 = get_x_and_y('../results/cleaned_data/coap/lan/trial1/coap_lan_test1_receiving_jamu.csv')
    

    list_of_x = [osc_x1, udp_x2, coap_x3]
    min_len = min(len(i) for i in list_of_x) - 1 
    print(min_len) 
    list_of_x_num = [osc_y1[min_len], udp_y2[min_len], coap_y3[min_len], len(osc_x1), len(udp_x2), len(coap_x3)]
    min_num = min(i for i in list_of_x_num)
    print(min_num)

    plt.plot(osc_x1[0:min_num], osc_y1[0:min_num], label = "OSC")
    plt.plot(udp_x2[0:min_num], udp_y2[0:min_num], label = "UDP")
    plt.plot(coap_x3[0:min_num], coap_y3[0:min_num], label = "CoAP")

    plt.xlabel('time (s)')
    plt.ylabel('packets/s')
    plt.title('LAN Pi Sending Trial 1')
    plt.legend(loc='upper right')
    # plt.show()
    plt.savefig('generated_graphs/lan_packets_sent_by_pc_line_chart.png')


    #LAN Pi Recv Trial 2
    # osc_x1, osc_y1 = get_x_and_y('../results/cleaned_data/osc/lan/trial2/lan_test_2_receiving_pi.csv')
    # udp_x2, udp_y2 = get_x_and_y('../results/cleaned_data/udp/lan/trial2/udp_lan_test_2_receiving_pi.csv')
    # coap_x3, coap_y3 = get_x_and_y('../results/cleaned_data/coap/lan/trial2/coap_lan_trial_receiving_pi.csv')
    

    # list_of_x = [osc_x1, udp_x2, coap_x3]
    # min_len = min(len(i) for i in list_of_x) - 1 
    # print(min_len) 
    # list_of_x_num = [osc_y1[min_len], udp_y2[min_len], coap_y3[min_len]]
    # min_num = min(i for i in list_of_x_num)
    # print(min_num)

    # plt.plot(osc_x1[0:min_num], osc_y1[0:min_num], label = "OSC")
    # plt.plot(udp_x2[0:min_num], udp_y2[0:min_num], label = "UDP")
    # plt.plot(coap_x3[0:min_num], coap_y3[0:min_num], label = "CoAP")

    # plt.xlabel('time (s)')
    # plt.ylabel('packets/s')
    # plt.title('LAN Pi Receiving Trial 1')
    # plt.legend(loc='upper right')
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_received_by_pi_line_chart_test2.png')


    #LAN Pi Send Trial 2
    # osc_x1, osc_y1 = get_x_and_y('../results/cleaned_data/osc/lan/trial2/lan_test_2_sending_pi.csv')
    # udp_x2, udp_y2 = get_x_and_y('../results/cleaned_data/udp/lan/trial2/udp_lan_test_2_sending_pi.csv')
    # coap_x3, coap_y3 = get_x_and_y('../results/cleaned_data/coap/lan/trial2/coap_lan_tria2_sending_pi.csv')
    

    # list_of_x = [osc_x1, udp_x2, coap_x3]
    # min_len = min(len(i) for i in list_of_x) - 1 
    # print(min_len) 
    # list_of_x_num = [osc_y1[min_len], udp_y2[min_len], coap_y3[min_len], len(osc_x1), len(udp_x2), len(coap_x3)]
    # min_num = min(i for i in list_of_x_num)
    # print(min_num)

    # plt.plot(osc_x1[0:min_num], osc_y1[0:min_num], label = "OSC")
    # plt.plot(udp_x2[0:min_num], udp_y2[0:min_num], label = "UDP")
    # plt.plot(coap_x3[0:min_num], coap_y3[0:min_num], label = "CoAP")

    # plt.xlabel('time (s)')
    # plt.ylabel('packets/s')
    # plt.title('LAN Pi Sending Trial 1')
    # plt.legend(loc='upper right')
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pi_line_chart_test2.png')


    #LAN PC Recv Trial 2
    # osc_x1, osc_y1 = get_x_and_y('../results/cleaned_data/osc/lan/trial2/lan_test_2_receiving_jamMac.csv')
    # udp_x2, udp_y2 = get_x_and_y('../results/cleaned_data/udp/lan/trial2/udp_lan_test_2_receiving_jamMac.csv')
    # coap_x3, coap_y3 = get_x_and_y('../results/cleaned_data/coap/lan/trial2/coap_lan_trial2_sending_jam.csv')
    

    # list_of_x = [osc_x1, udp_x2, coap_x3]
    # min_len = min(len(i) for i in list_of_x) - 1 
    # print(min_len) 
    # list_of_x_num = [osc_y1[min_len], udp_y2[min_len], coap_y3[min_len], len(osc_x1), len(udp_x2), len(coap_x3)]
    # min_num = min(i for i in list_of_x_num)
    # print(min_num)

    # plt.plot(osc_x1[0:min_num], osc_y1[0:min_num], label = "OSC")
    # plt.plot(udp_x2[0:min_num], udp_y2[0:min_num], label = "UDP")
    # plt.plot(coap_x3[0:min_num], coap_y3[0:min_num], label = "CoAP")

    # plt.xlabel('time (s)')
    # plt.ylabel('packets/s')
    # plt.title('LAN Pi Sending Trial 1')
    # plt.legend(loc='upper right')
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_recvd_by_pc_line_chart_test2.png')


    #LAN PC Send Trial 2
    # osc_x1, osc_y1 = get_x_and_y('../results/cleaned_data/osc/lan/trial2/lan_test_2_sending_jamMac.csv')
    # udp_x2, udp_y2 = get_x_and_y('../results/cleaned_data/udp/lan/trial2/udp_lan_test_2_sending_jamMac.csv')
    # coap_x3, coap_y3 = get_x_and_y('../results/cleaned_data/coap/lan/trial2/coap_lan_trial2_sending_jam.csv')
    

    # list_of_x = [osc_x1, udp_x2, coap_x3]
    # min_len = min(len(i) for i in list_of_x) - 1 
    # print(min_len) 
    # list_of_x_num = [osc_y1[min_len], udp_y2[min_len], coap_y3[min_len], len(osc_x1), len(udp_x2), len(coap_x3)]
    # min_num = min(i for i in list_of_x_num)
    # print(min_num)

    # plt.plot(osc_x1[0:min_num], osc_y1[0:min_num], label = "OSC")
    # plt.plot(udp_x2[0:min_num], udp_y2[0:min_num], label = "UDP")
    # plt.plot(coap_x3[0:min_num], coap_y3[0:min_num], label = "CoAP")

    # plt.xlabel('time (s)')
    # plt.ylabel('packets/s')
    # plt.title('LAN Pi Sending Trial 1')
    # plt.legend(loc='upper right')
    # # plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pc_line_chart_test_2.png')
    #endregion


if __name__ == '__main__':
    main()