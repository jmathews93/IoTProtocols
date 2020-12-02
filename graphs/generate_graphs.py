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

def get_length_no_zeroes(list_of_csv):
    length = 0

    for i in range(len(list_of_csv)):
        if list_of_csv[i][1] != '0':
            length += 1
    
    return length

def get_index_of_num_in_list_closest_to_another(list_ofvalues, num):
    absolute_val_array = []

    for i in list_ofvalues:
        absolute_val_array.append(abs(i - num))

    return absolute_val_array.index(min(absolute_val_array))


def avg_packets_per_s(file_name):
    sum = 0.0

    with open(file_name, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
    
    data_no_blanks = []

    #Cause some of the file have blanks at the ends
    for line in data:
        if line: 
            data_no_blanks.append(line)

    for i in range(1, len(data_no_blanks)):
        sum = sum + float(data_no_blanks[i][1])

    # avg = sum/len(data)
    # print(f"\n\nLength: {len(data_no_blanks)}\nLen - 0: {get_length_no_zeroes(data_no_blanks)}\n\n")
    avg = sum/get_length_no_zeroes(data_no_blanks)

    return avg

def get_x_and_y(file_name):
    x_axis = []
    y_axis = []

    with open(file_name, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

    data_no_blanks = []

    #Cause some of the file have blanks at the ends
    for line in data:
        if line: 
            data_no_blanks.append(line)

    # print(data_no_blanks)
    for i in range(1, len(data_no_blanks)):
        if data_no_blanks[i][1] != '0':
            x_axis.append(float(data_no_blanks[i][0]))
            y_axis.append(int(data_no_blanks[i][1]))

    # print(x_axis)
    # print(y_axis)
    return x_axis, y_axis

def avg_time():
    pass

def total_time():
    pass


def main():
    save = False
    show = False

    #command line argument to save or show. You can do both. IDK why though cause it'll be cancer...
    if len(sys.argv) > 2:
        if sys.argv[1] == '1':
            save = True
        if sys.argv[2] == '1':
            show = True
    #region Stats
    #region OSC Stats
    ##################################################################################################################
    #OSC WAN Pi Recv
    osc_wan_recv_pi_test1_avg = avg_packets_per_s('../updated_results/osc/osc_test1_wan_receiving_pi.txt')
    osc_wan_recv_pi_test2_avg = avg_packets_per_s('../updated_results/osc/osc_test2_wan_receiving_pi.txt')
    osc_wan_recv_pi_test3_avg = avg_packets_per_s('../updated_results/osc/osc_test3_wan_receiving_pi.txt')

    #OSC WAN Pi Send
    osc_wan_send_pi_test1_avg = avg_packets_per_s('../updated_results/osc/osc_test1_wan_sending_pi.txt')

    #OSC WAN PC Recv
    osc_wan_recv_pc_test1_avg = avg_packets_per_s('../updated_results/osc/osc_test1_wan_receiving_jgtmac.txt')

    #OSC WAN PC Send
    osc_wan_send_pc_test1_avg = avg_packets_per_s('../updated_results/osc/osc_test1_wan_sending_jgtmac.txt')
    osc_wan_send_pc_test2_avg = avg_packets_per_s('../updated_results/osc/osc_test2_wan_sending_jgtmac.txt')
    osc_wan_send_pc_test3_avg = avg_packets_per_s('../updated_results/osc/osc_test3_wan_sending_jgtmac.txt')

    #OSC LAN
    #############################################################################################################################################################
    #OSC LAN Pi Recv
    osc_lan_recv_pi_test1_avg = avg_packets_per_s('../updated_results/lan/osc/test1/osc_test1_lan_receiving_pi.txt')
    osc_lan_recv_pi_test2_avg = avg_packets_per_s('../updated_results/lan/osc/test2/osc_test2_lan_receiving_pi.txt')
    osc_lan_recv_pi_test3_avg = avg_packets_per_s('../updated_results/lan/osc/test3/osc_test3_lan_receiving_pi.txt')

    #OSC LAN Pi Send
    osc_lan_send_pi_test1_avg = avg_packets_per_s('../updated_results/lan/osc/test1/osc_test1_lan_sending_pi.txt')
    osc_lan_send_pi_test2_avg = avg_packets_per_s('../updated_results/lan/osc/test2/osc_test2_lan_sending_pi.txt')
    osc_lan_send_pi_test3_avg = avg_packets_per_s('../updated_results/lan/osc/test3/osc_test3_lan_sending_pi.txt')

    #OSC LAN PC Recv
    osc_lan_recv_pc_test1_avg = avg_packets_per_s('../updated_results/lan/osc/test1/osc_test1_lan_receiving_jammac.txt')
    osc_lan_recv_pc_test2_avg = avg_packets_per_s('../updated_results/lan/osc/test2/osc_test2_lan_receiving_jammac.txt')
    osc_lan_recv_pc_test3_avg = avg_packets_per_s('../updated_results/lan/osc/test3/osc_test3_lan_receiving_jammac.txt')

    #OSC LAN PC Send
    osc_lan_send_pc_test1_avg = avg_packets_per_s('../updated_results/lan/osc/test1/osc_test1_lan_sending_jammac.txt')
    osc_lan_send_pc_test2_avg = avg_packets_per_s('../updated_results/lan/osc/test2/osc_test2_lan_sending_jammac.txt')
    osc_lan_send_pc_test3_avg = avg_packets_per_s('../updated_results/lan/osc/test3/osc_test3_lan_sending_jammac.txt')

    #endregion
    ##################################################################################################################
    
    #region UDP Stats
    #######################################################################################################################################################
    #UDP WAN Pi Recv
    udp_wan_recv_pi_test1_avg = avg_packets_per_s('../updated_results/udp/udp_trial1_wan_recevivng_pi.txt')
    udp_wan_recv_pi_test2_avg = avg_packets_per_s('../updated_results/udp/udp_trial2_wan_recevivng_pi.txt')
    udp_wan_recv_pi_test3_avg = avg_packets_per_s('../updated_results/udp/udp_trial3_wan_recevivng_pi.txt')

    #UDP WAN Pc Send
    udp_wan_send_pc_test1_avg = avg_packets_per_s('../updated_results/udp/udp_test1_wan_sending_jgtmac.txt')
    udp_wan_send_pc_test2_avg = avg_packets_per_s('../updated_results/udp/udp_test2_wan_sending_jgtmac.txt')
    udp_wan_send_pc_test3_avg = avg_packets_per_s('../updated_results/udp/udp_test3_wan_sending_jgtmac.txt')

    #UDP LAN
    ############################################################################################################################################
    #UDP LAN Pi Recv
    udp_lan_recv_pi_test1_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test1_lan_receiving_pi.txt')
    udp_lan_recv_pi_test2_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test2_lan_receiving_pi.txt')
    udp_lan_recv_pi_test3_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test3_lan_receiving_pi.txt')

    #UDP LAN Pi Send
    udp_lan_send_pi_test1_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test1_lan_sending_pi.txt')
    udp_lan_send_pi_test2_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test2_lan_sending_pi.txt')
    udp_lan_send_pi_test3_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test3_lan_sending_pi.txt')

    #UDP LAN PC Recv
    udp_lan_recv_pc_test1_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test1_lan_receiving_jammac.txt')
    udp_lan_recv_pc_test2_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test2_lan_receiving_jammac.txt')
    udp_lan_recv_pc_test3_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test3_lan_receiving_jammac.txt')

    #UDP LAN PC Send
    udp_lan_send_pc_test1_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test1_lan_sending_jammac.txt')
    udp_lan_send_pc_test2_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test2_lan_sending_jammac.txt')
    udp_lan_send_pc_test3_avg = avg_packets_per_s('../updated_results/lan/udp/udp_test3_lan_sending_jammac.txt')

    #endregion
    ##################################################################################################################


    #region COAP Stats
    #######################################################################################################################################################
    #COap WAN Pi Recv
    coap_wan_recv_pi_test1_avg = avg_packets_per_s('../updated_results/coap/coap_test1_wan_receiving_pi.txt')
    print("Coap WAN Rcv pi Test1: " + str(coap_wan_recv_pi_test1_avg))
    coap_wan_recv_pc_test1_avg = avg_packets_per_s('../updated_results/coap/coap_test1_wan_receiving_jgtmac.txt')
    print("Coap WAN Rcv pc Test1: " + str(coap_wan_recv_pc_test1_avg))
    coap_wan_send_pc_test1_avg = avg_packets_per_s('../updated_results/coap/coap_test1_wan_sending_jgtmac.txt')
    print("Coap WAN Send pc Test1: " + str(coap_wan_send_pc_test1_avg))
    coap_wan_send_pi_test1_avg = avg_packets_per_s('../updated_results/coap/coap_test1_wan_sending_pi.txt')
    print("Coap WAN Send pi Test1: " + str(coap_wan_send_pi_test1_avg))

    #LAN COAP
    ##################
    #COap LAN Pi Recv
    coap_lan_recv_pi_test1_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test1_lan_receiving_pi.txt')
    print("COAP LAN Rcv pi Test1: " + str(coap_lan_recv_pi_test1_avg))
    coap_lan_recv_pi_test2_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test2_lan_receiving_pi.txt')
    print("COAP LAN Rcv pi Test2: " + str(coap_lan_recv_pi_test2_avg))
    coap_lan_recv_pi_test3_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test3_lan_receiving_pi.txt')
    print("COAP LAN Rcv pi Test3: " + str(coap_lan_recv_pi_test3_avg))

    #COap LAN Pi Send
    coap_lan_send_pi_test1_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test1_lan_sending_pi.txt')
    print("COAP LAN Send pi Test1: " + str(coap_lan_send_pi_test1_avg))
    coap_lan_send_pi_test2_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test2_lan_sending_pi.txt')
    print("COAP LAN Send pi Test2: " + str(coap_lan_send_pi_test2_avg))
    coap_lan_send_pi_test3_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test3_lan_sending_pi.txt')
    print("COAP LAN Send pi Test3: " + str(coap_lan_send_pi_test3_avg))

    #COap LAN PC Send
    coap_lan_send_pc_test1_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test1_lan_sending_jammac.txt')
    print("COAP LAN Send pc Test1: " + str(coap_lan_send_pc_test1_avg))
    coap_lan_send_pc_test2_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test2_lan_sending_jammac.txt')
    print("COAP LAN Send pc Test2: " + str(coap_lan_send_pc_test2_avg))
    coap_lan_send_pc_test3_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test3_lan_sending_jammac.txt')
    print("COAP LAN Send pc Test3: " + str(coap_lan_send_pc_test3_avg))

    #COap LAN PC Recv
    coap_lan_recv_pc_test1_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test1_lan_receiving_jammac.txt')
    print("COAP LAN Rcv pc Test1: " + str(coap_lan_recv_pc_test1_avg))
    coap_lan_recv_pc_test2_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test2_lan_receiving_jammac.txt')
    print("COAP LAN Rcv pc Test2: " + str(coap_lan_recv_pc_test2_avg))
    coap_lan_recv_pc_test3_avg = avg_packets_per_s('../updated_results/lan/coap/coap_test3_lan_receiving_jammac.txt')
    print("COAP LAN Rcv pc Test3: " + str(coap_lan_recv_pc_test3_avg))
    #endregion

    ##################################################################################################################
    #endregion

    #region GRAPHS
    ######################################################################################################################
    #region Bar Charts
    #region WAN PI RECV
    #================================================================================================================================
    # data to plot
    n_groups = 3
    means_osc = (osc_wan_recv_pi_test1_avg, osc_wan_recv_pi_test2_avg, osc_wan_recv_pi_test3_avg, )
    means_udp = (udp_wan_recv_pi_test1_avg, udp_wan_recv_pi_test2_avg, udp_wan_recv_pi_test3_avg)
    means_coap = (coap_wan_recv_pi_test1_avg, 0, 0)

    # # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_osc, bar_width,
    alpha=opacity,
    color='b',
    label='OSC')

    rects2 = plt.bar(index + bar_width, means_udp, bar_width,
    alpha=opacity,
    color='g',
    label='UDP')

    rects3 = plt.bar(index + (bar_width*2), means_coap, bar_width,
    alpha=opacity,
    color='r',
    label='COaP')

    plt.xlabel('Trial')
    plt.ylabel('Packets/10 ms')
    plt.title('Packets Received by Pi over WAN')
    plt.xticks(index + bar_width, ('Trial 1', 'Trial 2', 'Trial 3'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/wan_packets_received_by_pi.png')
    #================================================================================================================================
    #endregion

    #region LAN PI RECV
    #================================================================================================================================
    # data to plot
    n_groups = 3
    means_osc = (osc_lan_recv_pi_test1_avg, osc_lan_recv_pi_test2_avg, osc_lan_recv_pi_test3_avg, )
    means_udp = (udp_lan_recv_pi_test1_avg, udp_lan_recv_pi_test2_avg, udp_lan_recv_pi_test3_avg)
    means_coap = (coap_lan_recv_pi_test1_avg, coap_lan_recv_pi_test2_avg, coap_lan_recv_pi_test3_avg)

    # # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_osc, bar_width,
    alpha=opacity,
    color='b',
    label='OSC')

    rects2 = plt.bar(index + bar_width, means_udp, bar_width,
    alpha=opacity,
    color='g',
    label='UDP')

    rects3 = plt.bar(index + (bar_width*2), means_coap, bar_width,
    alpha=opacity,
    color='r',
    label='COaP')

    plt.xlabel('Trial')
    plt.ylabel('Packets/10 ms')
    plt.title('Packets Received by Pi over LAN')
    plt.xticks(index + bar_width, ('Trial 1', 'Trial 2', 'Trial 3'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_packets_received_by_pi.png')
    #endregion

    #region LAN PI SEND
    #================================================================================================================================
    # data to plot
    n_groups = 3
    means_osc = (osc_lan_send_pi_test1_avg, osc_lan_send_pi_test2_avg, osc_lan_send_pi_test3_avg, )
    means_udp = (udp_lan_send_pi_test1_avg, udp_lan_send_pi_test2_avg, udp_lan_send_pi_test3_avg)
    means_coap = (coap_lan_send_pi_test1_avg, coap_lan_send_pi_test2_avg, coap_lan_send_pi_test3_avg)

    # # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_osc, bar_width,
    alpha=opacity,
    color='b',
    label='OSC')

    rects2 = plt.bar(index + bar_width, means_udp, bar_width,
    alpha=opacity,
    color='g',
    label='UDP')

    rects3 = plt.bar(index + (bar_width*2), means_coap, bar_width,
    alpha=opacity,
    color='r',
    label='COaP')

    plt.xlabel('Trial')
    plt.ylabel('Packets/s')
    plt.title('Packets Sent by Pi over LAN')
    plt.xticks(index + bar_width, ('Trial 1', 'Trial 2', 'Trial 3'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_packets_sent_by_pi.png')
    #endregion

    #region LAN PC SEND
    #================================================================================================================================
    # data to plot
    n_groups = 3
    means_osc = (osc_lan_send_pc_test1_avg, osc_lan_send_pc_test2_avg, osc_lan_send_pc_test3_avg, )
    means_udp = (udp_lan_send_pc_test1_avg, udp_lan_send_pc_test2_avg, udp_lan_send_pc_test3_avg)
    means_coap = (coap_lan_send_pc_test1_avg, coap_lan_send_pc_test2_avg, coap_lan_send_pc_test3_avg)

    # # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_osc, bar_width,
    alpha=opacity,
    color='b',
    label='OSC')

    rects2 = plt.bar(index + bar_width, means_udp, bar_width,
    alpha=opacity,
    color='g',
    label='UDP')

    rects3 = plt.bar(index + (bar_width*2), means_coap, bar_width,
    alpha=opacity,
    color='r',
    label='COaP')

    plt.xlabel('Trial')
    plt.ylabel('Packets/10 ms')
    plt.title('Packets Sent by PC over LAN')
    plt.xticks(index + bar_width, ('Trial 1', 'Trial 2', 'Trial 3'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_packets_sent_by_pc.png')
    #endregion

    #region LAN PC RECV
    #================================================================================================================================
    # data to plot
    n_groups = 3
    means_osc = (osc_lan_recv_pc_test1_avg, osc_lan_recv_pc_test2_avg, osc_lan_recv_pc_test3_avg, )
    means_udp = (udp_lan_recv_pc_test1_avg, udp_lan_recv_pc_test2_avg, udp_lan_recv_pc_test3_avg)
    means_coap = (coap_lan_recv_pc_test1_avg, coap_lan_recv_pc_test2_avg, coap_lan_recv_pc_test3_avg)

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_osc, bar_width,
    alpha=opacity,
    color='b',
    label='OSC')

    rects2 = plt.bar(index + bar_width, means_udp, bar_width,
    alpha=opacity,
    color='g',
    label='UDP')

    rects3 = plt.bar(index + (bar_width*2), means_coap, bar_width,
    alpha=opacity,
    color='r',
    label='COaP')

    plt.xlabel('Trial')
    plt.ylabel('Packets/10 ms')
    plt.title('Packets Received by PC over LAN')
    plt.xticks(index + bar_width, ('Trial 1', 'Trial 2', 'Trial 3'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_packets_recvd_by_pc.png')
    #endregion
    #endregion
    #===============================================================
    
    #region LINE GRAPHS
    #############################
    #region LAN Pi Recv Trial 1
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test1/osc_test1_lan_receiving_pi.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test1_lan_receiving_pi.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test1_lan_receiving_pi.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    #get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC")
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP")
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP")

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN Pi Receiving Trial 1')
    plt.title('LAN Pi Receiving Trial 1 OSC')
    plt.title('LAN Pi Receiving Trial 1 UDP')
    plt.title('LAN Pi Receiving Trial 1 CoAP')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_received_by_pi_line_chart.png')
    # plt.savefig('generated_graphs/OSC_lan_packets_received_by_pi_line_chart.png')
    # plt.savefig('generated_graphs/UDP_lan_packets_received_by_pi_line_chart.png')
    # plt.savefig('generated_graphs/COAP_lan_packets_received_by_pi_line_chart.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_received_by_pi_line_chart.png')
    #endregion

    #region LAN Pi Send Trial 1
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test1/osc_test1_lan_sending_pi.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test1_lan_sending_pi.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test1_lan_sending_pi.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP", linewidth=1)
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN Pi Sending Trial 1')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pi_line_chart.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_sent_by_pi_line_chart.png')
    #endregion

    #region LAN PC Send Trial 1
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test1/osc_test1_lan_sending_jammac.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test1_lan_sending_jammac.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test1_lan_sending_jammac.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # #get dem bois all the same length
    # num = 100
    # plt.plot(osc_x1[0:num], osc_y1[0:num], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:num], udp_y2[0:num], label = "UDP")
    # plt.plot(coap_x3[0:num], coap_y3[0:num], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN PC Sent Trial 1')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # # plt.savefig('generated_graphs/lan_packets_sent_by_pc_line_chart.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_sent_by_pc_line_chart.png')
    #endregion

    #region LAN PC Recv Trial 1
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test1/osc_test1_lan_receiving_jammac.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test1_lan_receiving_jammac.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test1_lan_receiving_jammac.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # #get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP", linewidth=1)
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN Pi Receiving Trial 1')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_recvd_by_pc_line_chart.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_recvd_by_pc_line_chart.png')
    #endregion

    #region LAN Pi Recv Trial 2
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test2/osc_test2_lan_receiving_pi.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test2_lan_receiving_pi.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test2_lan_receiving_pi.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # #get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP", linewidth=1)
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN Pi Receiving Trial 2')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_received_by_pi_line_chart_test2.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_received_by_pi_line_chart_test2.png')
    #endregion

    #region LAN Pi Send Trial 2
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test2/osc_test2_lan_sending_pi.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test2_lan_sending_pi.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test2_lan_sending_pi.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # #get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP", linewidth=1)
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN Pi Sending Trial 2')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pi_line_chart_test2.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_sent_by_pi_line_chart_test2.png')
    #endregion

    #region LAN PC Recv Trial 2
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test2/osc_test2_lan_receiving_jammac.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test2_lan_receiving_jammac.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test2_lan_receiving_jammac.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # #get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP", linewidth=1)
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN PC Receiving Trial 2')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_recvd_by_pc_line_chart_test2.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_recvd_by_pc_line_chart_test2.png')
    #endregion

    #region LAN PC Send Trial 2
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test2/osc_test2_lan_sending_jammac.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test2_lan_sending_jammac.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test2_lan_sending_jammac.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 
    # print(min_len) 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # #get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP", linewidth=1)
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN PC Sending Trial 2')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pc_line_chart_test_2.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_sent_by_pc_line_chart_test_2.png')
    #endregion
    
    #region LAN Pi Recv Trial 3
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test3/osc_test3_lan_receiving_pi.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test3_lan_receiving_pi.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test3_lan_receiving_pi.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # #get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP", linewidth=1)
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN pi Receiving Trial 3')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pc_line_chart_test_2.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_recvd_by_pi_line_chart_test_3.png')
    #endregion
    
    #region LAN Pi Send Trial 3
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test3/osc_test3_lan_sending_pi.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test3_lan_sending_pi.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test3_lan_sending_pi.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 
    # print(min_len) 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # #get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP", linewidth=1)
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN pi Sending Trial 3')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pc_line_chart_test_2.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_sent_by_pi_line_chart_test_3.png')
    #endregion
    
    #region LAN PC Recv Trial 3
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test3/osc_test3_lan_receiving_jammac.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test3_lan_receiving_jammac.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test3_lan_receiving_jammac.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # #get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP", linewidth=1)
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN PC Receiving Trial 3')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pc_line_chart_test_2.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_recvd_by_pc_line_chart_test_3.png')

    #endregion
    
    #region LAN PC Sent Trial 3
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test3/osc_test3_lan_sending_jammac.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/lan/udp/udp_test3_lan_sending_jammac.txt')
    coap_x3, coap_y3 = get_x_and_y('../updated_results/lan/coap/coap_test3_lan_sending_jammac.txt')
    

    # list_of_x = [osc_x1[len(osc_x1) - 1], udp_x2[len(udp_x2) -1 ], coap_x3[len(coap_x3) - 1]]
    # min_len = min(i for i in list_of_x) - 1 
    # print(min_len) 

    # osc_min = get_index_of_num_in_list_closest_to_another(osc_x1, min_len)
    # udp_min = get_index_of_num_in_list_closest_to_another(udp_x2, min_len)
    # coap_min = get_index_of_num_in_list_closest_to_another(coap_x3, min_len)

    # #get dem bois all the same length
    # plt.plot(osc_x1[0:osc_min], osc_y1[0:osc_min], label = "OSC", linewidth=1)
    # plt.plot(udp_x2[0:udp_min], udp_y2[0:udp_min], label = "UDP", linewidth=1)
    # plt.plot(coap_x3[0:coap_min], coap_y3[0:coap_min], label = "CoAP", linewidth=1)

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP")
    plt.plot(coap_x3[start:num], coap_y3[start:num], label = "CoAP", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('LAN PC Sending Trial 3')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    # plt.savefig('generated_graphs/lan_packets_sent_by_pc_line_chart_test_2.png')
    if save:
        plt.savefig('generated_graphs/cleaner/lan_packets_sent_by_pc_line_chart_test_3.png')

    #endregion

    #region LAN vs WAN LineCharts
    ###################################################################################################################################
    #region OSC WAN V LAN
    #region OSC trial 1 PI Recv
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test1/osc_test1_lan_receiving_pi.txt')
    osc_x2, osc_y2 = get_x_and_y('../updated_results/osc/osc_test1_wan_receiving_pi.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC LAN", linewidth=1)
    plt.plot(osc_x2[start:num], osc_y2[start:num], label = "OSC WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('OSC Trial 1 Pi Receiving WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/osc_recv_pi_trial1_lan_v_wan.png')
    #endregion

    #region OSC trial 1 PI Send
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test1/osc_test1_lan_sending_pi.txt')
    osc_x2, osc_y2 = get_x_and_y('../updated_results/osc/osc_test1_wan_sending_pi.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC LAN", linewidth=1)
    plt.plot(osc_x2[start:num], osc_y2[start:num], label = "OSC WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('OSC Trial 1 Pi Send WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/osc_send_pi_trial1_lan_v_wan.png')
    #endregion

    #region OSC trial 1 PC Recv
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test1/osc_test1_lan_receiving_jammac.txt')
    osc_x2, osc_y2 = get_x_and_y('../updated_results/osc/osc_test1_wan_receiving_jgtmac.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC LAN", linewidth=1)
    plt.plot(osc_x2[start:num], osc_y2[start:num], label = "OSC WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('OSC Trial 1 PC Receive WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/osc_recv_pc_trial1_lan_v_wan.png')
    #endregion

    #region OSC trial 1 PC Send
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test1/osc_test1_lan_sending_jammac.txt')
    osc_x2, osc_y2 = get_x_and_y('../updated_results/osc/osc_test1_wan_sending_jgtmac.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC LAN", linewidth=1)
    plt.plot(osc_x2[start:num], osc_y2[start:num], label = "OSC WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('OSC Trial 1 PC Send WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/osc_send_pc_trial1_lan_v_wan.png')
    #endregion

    #region OSC trial 2 PI Recv
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test2/osc_test2_lan_receiving_pi.txt')
    osc_x2, osc_y2 = get_x_and_y('../updated_results/osc/osc_test2_wan_receiving_pi.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC LAN", linewidth=1)
    plt.plot(osc_x2[start:num], osc_y2[start:num], label = "OSC WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('OSC Trial 2 Pi Receiving WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/osc_recv_pi_trial2_lan_v_wan.png')
    #endregion

    #region OSC trial 2 PC Send
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test2/osc_test2_lan_sending_jammac.txt')
    osc_x2, osc_y2 = get_x_and_y('../updated_results/osc/osc_test2_wan_sending_jgtmac.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC LAN", linewidth=1)
    plt.plot(osc_x2[start:num], osc_y2[start:num], label = "OSC WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('OSC Trial 2 PC Send WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/osc_send_pc_trial2_lan_v_wan.png')
    #endregion

    #region OSC trial 3 PC Send
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test3/osc_test3_lan_sending_jammac.txt')
    osc_x2, osc_y2 = get_x_and_y('../updated_results/osc/osc_test3_wan_sending_jgtmac.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC LAN", linewidth=1)
    plt.plot(osc_x2[start:num], osc_y2[start:num], label = "OSC WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('OSC Trial 3 PC Send WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/osc_send_pc_trial3_lan_v_wan.png')
    #endregion
    
    #region OSC trial 3 Pi Recv
    osc_x1, osc_y1 = get_x_and_y('../updated_results/lan/osc/test3/osc_test3_lan_receiving_pi.txt')
    osc_x2, osc_y2 = get_x_and_y('../updated_results/osc/osc_test3_wan_receiving_pi.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(osc_x1[start:num], osc_y1[start:num], label = "OSC LAN", linewidth=1)
    plt.plot(osc_x2[start:num], osc_y2[start:num], label = "OSC WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('OSC Trial 3 Pi Receiving WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/osc_recv_pi_trial3_lan_v_wan.png')
    #endregion
    #endregion
    
    #region UDP WAN V LAN
    #region UDP trial 1 Pi Recv
    udp_x1, udp_y1 = get_x_and_y('../updated_results/lan/udp/udp_test1_lan_receiving_pi.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/udp/udp_trial1_wan_recevivng_pi.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(udp_x1[start:num], udp_y1[start:num], label = "UDP LAN", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('UDP Trial 1 Pi Receiving WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/udp_recv_pi_trial1_lan_v_wan.png')
    #endregion

    #region UDP trial 1 Pi Send
    udp_x1, udp_y1 = get_x_and_y('../updated_results/lan/udp/udp_test1_lan_sending_pi.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/udp/udp_trial1_wan_sending_pi.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(udp_x1[start:num], udp_y1[start:num], label = "UDP LAN", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('UDP Trial 1 Pi Sending WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/udp_send_pi_trial1_lan_v_wan.png')
    #endregion

    #region UDP trial 1 PC Recv
    udp_x1, udp_y1 = get_x_and_y('../updated_results/lan/udp/udp_test1_lan_receiving_jammac.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/udp/udp_trial1_wan_recevivng_jgtmac.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(udp_x1[start:num], udp_y1[start:num], label = "UDP LAN", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('UDP Trial 1 PC Receiving WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/udp_recv_pc_trial1_lan_v_wan.png')
    #endregion

    #region UDP trial 1 PC Send
    udp_x1, udp_y1 = get_x_and_y('../updated_results/lan/udp/udp_test1_lan_sending_jammac.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/udp/udp_test1_wan_sending_jgtmac.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(udp_x1[start:num], udp_y1[start:num], label = "UDP LAN", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('UDP Trial 1 PC Sending WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/udp_send_pc_trial1_lan_v_wan.png')
    #endregion

    #region UDP trial 2 Pi Recv
    udp_x1, udp_y1 = get_x_and_y('../updated_results/lan/udp/udp_test2_lan_receiving_pi.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/udp/udp_trial2_wan_recevivng_pi.txt')
    

    #cleaner
    start = 20
    num = 200
    plt.plot(udp_x1[start:num], udp_y1[start:num], label = "UDP LAN", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('UDP Trial 2 Pi Receiving WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/udp_recv_pi_trial2_lan_v_wan.png')
    #endregion

    #region UDP trial 2 PC Send
    udp_x1, udp_y1 = get_x_and_y('../updated_results/lan/udp/udp_test2_lan_sending_jammac.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/udp/udp_test2_wan_sending_jgtmac.txt')
    

    # #cleaner
    start = 20
    num = 200
    plt.plot(udp_x1[start:num], udp_y1[start:num], label = "UDP LAN", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('UDP Trial 2 PC Sending WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/udp_send_pc_trial2_lan_v_wan.png')
    #endregion

    #region UDP trial 3 PC Send
    udp_x1, udp_y1 = get_x_and_y('../updated_results/lan/udp/udp_test3_lan_sending_jammac.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/udp/udp_test3_wan_sending_jgtmac.txt')
    

    # #cleaner
    start = 20
    num = 200
    plt.plot(udp_x1[start:num], udp_y1[start:num], label = "UDP LAN", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('UDP Trial 3 PC Sending WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/udp_send_pc_trial3_lan_v_wan.png')
    #endregion

    #region UDP trial 3 Pi Recv
    udp_x1, udp_y1 = get_x_and_y('../updated_results/lan/udp/udp_test3_lan_receiving_pi.txt')
    udp_x2, udp_y2 = get_x_and_y('../updated_results/udp/udp_trial3_wan_recevivng_pi.txt')
    

    # #cleaner
    start = 20
    num = 200
    plt.plot(udp_x1[start:num], udp_y1[start:num], label = "UDP LAN", linewidth=1)
    plt.plot(udp_x2[start:num], udp_y2[start:num], label = "UDP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('UDP Trial 3 Pi Receiving WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/udp_recv_pi_trial3_lan_v_wan.png')
    #endregion
    #endregion
    
    #region COAP WAN V LAN
    #region COAP trial 1 Pi Recv
    coap_x1, coap_y1 = get_x_and_y('../updated_results/lan/coap/coap_test1_lan_receiving_pi.txt')
    coap_x2, coap_y2 = get_x_and_y('../updated_results/coap/coap_test1_wan_receiving_pi.txt')
    

    # #cleaner
    start = 20
    num = 200
    plt.plot(coap_x1[start:num], coap_y1[start:num], label = "COAP LAN", linewidth=1)
    plt.plot(coap_x2[start:num], coap_y2[start:num], label = "COAP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('COAP Trial 1 Pi Receiving WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/coap_recv_pi_trial1_lan_v_wan.png')
    #endregion

    #region COAP trial 1 Pi Send
    coap_x1, coap_y1 = get_x_and_y('../updated_results/lan/coap/coap_test1_lan_sending_pi.txt')
    coap_x2, coap_y2 = get_x_and_y('../updated_results/coap/coap_test1_wan_sending_pi.txt')
    

    # #cleaner
    start = 20
    num = 200
    plt.plot(coap_x1[start:num], coap_y1[start:num], label = "COAP LAN", linewidth=1)
    plt.plot(coap_x2[start:num], coap_y2[start:num], label = "COAP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('COAP Trial 1 Pi Sending WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/coap_send_pi_trial1_lan_v_wan.png')
    #endregion

    #region COAP trial 1 Pc Recv
    coap_x1, coap_y1 = get_x_and_y('../updated_results/lan/coap/coap_test1_lan_receiving_jammac.txt')
    coap_x2, coap_y2 = get_x_and_y('../updated_results/coap/coap_test1_wan_receiving_jgtmac.txt')
    

    # #cleaner
    start = 20
    num = 200
    plt.plot(coap_x1[start:num], coap_y1[start:num], label = "COAP LAN", linewidth=1)
    plt.plot(coap_x2[start:num], coap_y2[start:num], label = "COAP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('COAP Trial 1 PC Receiving WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/coap_recv_pc_trial1_lan_v_wan.png')
    #endregion

    #region COAP trial 1 PC Send
    coap_x1, coap_y1 = get_x_and_y('../updated_results/lan/coap/coap_test1_lan_sending_jammac.txt')
    coap_x2, coap_y2 = get_x_and_y('../updated_results/coap/coap_test1_wan_sending_jgtmac.txt')
    

    # #cleaner
    start = 20
    num = 200
    plt.plot(coap_x1[start:num], coap_y1[start:num], label = "COAP LAN", linewidth=1)
    plt.plot(coap_x2[start:num], coap_y2[start:num], label = "COAP WAN", linewidth=1)

    plt.xlabel('time (s)')
    plt.ylabel('packets/10 ms')
    plt.title('COAP Trial 1 PC Sending WAN vs LAN')
    plt.legend(loc='upper right')
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/lan_v_wan/coap_send_pc_trial1_lan_v_wan.png')
    #endregion

    #endregion

    #endregion
    
    #endregion

    #region WAN V LAN Bar
    
    #region WAN V LAN PI RECV Trial 1
    #================================================================================================================================
    # data to plot
    n_groups = 3
    means_wan = (osc_wan_recv_pi_test1_avg, udp_wan_recv_pi_test1_avg, coap_wan_recv_pi_test1_avg)
    means_lan = (osc_lan_recv_pi_test1_avg, udp_lan_recv_pi_test1_avg, coap_lan_recv_pi_test1_avg)

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_wan, bar_width,
    alpha=opacity,
    color='b',
    label='WAN')

    rects2 = plt.bar(index + bar_width, means_lan, bar_width,
    alpha=opacity,
    color='g',
    label='LAN')

    plt.xlabel('Trial')
    plt.ylabel('Packets/10 ms')
    plt.title('Packets Received by Pi Trial 1 over WAN v LAN')
    plt.xticks(index + bar_width, ('OSC', 'UDP', 'CoAP'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/bars/wan_v_lan_packets_received_by_pi_trial1.png')
    
    #endregion

    #region WAN V LAN PC Recv Trial 1
    #================================================================================================================================
    # data to plot
    n_groups = 3
    means_wan = (osc_wan_send_pc_test1_avg, udp_wan_send_pc_test1_avg, coap_wan_send_pc_test1_avg)
    means_lan = (osc_lan_send_pc_test1_avg, udp_lan_send_pc_test1_avg, coap_lan_send_pc_test1_avg)

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_wan, bar_width,
    alpha=opacity,
    color='b',
    label='WAN')

    rects2 = plt.bar(index + bar_width, means_lan, bar_width,
    alpha=opacity,
    color='g',
    label='LAN')

    plt.xlabel('Trial')
    plt.ylabel('Packets/10 ms')
    plt.title('Packets Received by PC Trial 1 over WAN v LAN')
    plt.xticks(index + bar_width, ('OSC', 'UDP', 'CoAP'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/bars/wan_v_lan_packets_recvd_by_pc_trial1.png')
    
    #endregion
    
    #region WAN V LAN PC Send Trial 2
    #================================================================================================================================
    # data to plot
    n_groups = 3
    means_wan = (osc_wan_send_pc_test2_avg, udp_wan_send_pc_test2_avg, 0)
    means_lan = (osc_lan_send_pc_test2_avg, udp_lan_send_pc_test2_avg, 0)

    # # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_wan, bar_width,
    alpha=opacity,
    color='b',
    label='WAN')

    rects2 = plt.bar(index + bar_width, means_lan, bar_width,
    alpha=opacity,
    color='g',
    label='LAN')

    plt.xlabel('Trial')
    plt.ylabel('Packets/10 ms')
    plt.title('Packets Sent by PC Trial 2 over WAN v LAN')
    plt.xticks(index + bar_width, ('OSC', 'UDP', 'CoAP'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/bars/wan_v_lan_packets_sent_by_pc_trial2.png')
    
    #endregion
    
    #region WAN V LAN PI RECVD Trial 2
    #================================================================================================================================
    # data to plot
    n_groups = 3
    means_wan = (osc_wan_recv_pi_test2_avg, udp_wan_recv_pi_test2_avg, 0)
    means_lan = (osc_lan_recv_pi_test2_avg, udp_lan_recv_pc_test2_avg, coap_lan_recv_pi_test2_avg)

    # # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_wan, bar_width,
    alpha=opacity,
    color='b',
    label='WAN')

    rects2 = plt.bar(index + bar_width, means_lan, bar_width,
    alpha=opacity,
    color='g',
    label='LAN')

    plt.xlabel('Trial')
    plt.ylabel('Packets/10 ms')
    plt.title('Packets Received by Pi Trial 2 over WAN v LAN')
    plt.xticks(index + bar_width, ('OSC', 'UDP', 'CoAP'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/bars/wan_v_lan_packets_recvd_by_pi_trial2.png')
    
    #endregion

    #region WAN V LAN PI RECVD Trial 3
    #================================================================================================================================
    # # data to plot
    n_groups = 3
    means_wan = (osc_wan_recv_pi_test3_avg, udp_wan_recv_pi_test3_avg, 0)
    means_lan = (osc_lan_recv_pi_test3_avg, udp_lan_recv_pc_test3_avg, coap_lan_recv_pi_test3_avg)

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_wan, bar_width,
    alpha=opacity,
    color='b',
    label='WAN')

    rects2 = plt.bar(index + bar_width, means_lan, bar_width,
    alpha=opacity,
    color='g',
    label='LAN')

    plt.xlabel('Trial')
    plt.ylabel('Packets/10 ms')
    plt.title('Packets Received by Pi Trial 3 over WAN v LAN')
    plt.xticks(index + bar_width, ('OSC', 'UDP', 'CoAP'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/bars/wan_v_lan_packets_recvd_by_pi_trial3.png')
    
    #endregion

    #region WAN V LAN PC Sent Trial 3
    #================================================================================================================================
    # data to plot
    n_groups = 3
    means_wan = (osc_wan_send_pc_test3_avg, udp_wan_send_pc_test3_avg, 0)
    means_lan = (osc_lan_send_pc_test3_avg, udp_lan_send_pc_test3_avg, coap_lan_send_pc_test3_avg)

    # # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, means_wan, bar_width,
    alpha=opacity,
    color='b',
    label='WAN')

    rects2 = plt.bar(index + bar_width, means_lan, bar_width,
    alpha=opacity,
    color='g',
    label='LAN')

    plt.xlabel('Trial')
    plt.ylabel('Packets/10 ms')
    plt.title('Packets Sent by PC Trial 3 over WAN v LAN')
    plt.xticks(index + bar_width, ('OSC', 'UDP', 'CoAP'))
    plt.legend()

    plt.tight_layout()
    if show:
        plt.show()
    if save:
        plt.savefig('generated_graphs/bars/wan_v_lan_packets_sent_by_pc_trial3.png')
    
    #endregion

    #endregion
    #endregion
if __name__ == '__main__':
    main()
